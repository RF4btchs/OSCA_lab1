<#
  Лабораторная работа №1. Запись активности cmd.exe через Sysinternals Process Monitor.

  Procmon загружает драйвер-фильтр ядра, поэтому требует прав администратора:
  скрипт сам запрашивает повышение (UAC).

  1. Procmon запускается в фоне и пишет все события в logs\procmon.pml.
  2. Выполняется тот же сценарий scenario.cmd (без отладчика).
  3. Procmon останавливается, журнал конвертируется в CSV.
  4. procmon_profile.py оставляет события cmd.exe и его потомков и строит профиль.

  Запуск:  powershell -ExecutionPolicy Bypass -File scripts\run_procmon.ps1
#>
$ErrorActionPreference = 'Stop'

$principal = [Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()
if (-not $principal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
    Write-Host 'Нужны права администратора — запрашиваю повышение (UAC)...'
    $p = Start-Process powershell -Verb RunAs -Wait -PassThru -ArgumentList @(
            '-NoProfile', '-ExecutionPolicy', 'Bypass', '-File', "`"$PSCommandPath`"")
    exit $p.ExitCode
}

$Lab     = Split-Path -Parent $PSScriptRoot
$Logs    = Join-Path $Lab 'logs'
$Procmon = Join-Path $Lab 'tools\ProcessMonitor\Procmon64.exe'
$Work    = Join-Path $env:TEMP 'lab1_procmon'
$RunDir  = Join-Path $Work 'run'
$py      = (Get-Command python -ErrorAction Stop).Source
if (-not (Test-Path $Procmon)) { throw "не найден $Procmon" }
New-Item -ItemType Directory -Force $Work, $RunDir, $Logs | Out-Null
Copy-Item (Join-Path $Lab 'scenario\scenario.cmd') $RunDir -Force

$pml = Join-Path $Work 'procmon.pml'
$csv = Join-Path $Work 'procmon.csv'
Remove-Item $pml, $csv -ErrorAction SilentlyContinue

try {
    # 1. старт захвата
    Start-Process $Procmon -ArgumentList '/AcceptEula', '/Quiet', '/Minimized', '/BackingFile', "`"$pml`""
    Start-Sleep -Seconds 4                                     # драйвер должен успеть загрузиться

    # 2. сценарий
    $env:PATH    = "$env:SystemRoot\system32;$env:SystemRoot;$env:SystemRoot\System32\Wbem"
    $env:PATHEXT = '.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC'
    # стандартное поведение поиска программ: сначала текущий каталог, затем PATH
    Remove-Item Env:NoDefaultCurrentDirectoryInExePath -ErrorAction SilentlyContinue
    $cmd = Start-Process "$env:SystemRoot\System32\cmd.exe" -WorkingDirectory $RunDir -PassThru -Wait `
              -NoNewWindow -RedirectStandardOutput (Join-Path $Work 'scenario_out.txt') `
              -ArgumentList '/c', (Join-Path $RunDir 'scenario.cmd')
    "cmd.exe PID=$($cmd.Id) ExitCode=$($cmd.ExitCode)" | Set-Content -Encoding utf8 (Join-Path $Logs 'procmon_pid.txt')
    Start-Sleep -Seconds 2
} finally {
    # 3. остановка (вызывается даже при ошибке, чтобы драйвер не остался писать журнал)
    Start-Process $Procmon -ArgumentList '/Terminate' -Wait
}
Start-Process $Procmon -ArgumentList '/AcceptEula', '/Quiet', '/OpenLog', "`"$pml`"", '/SaveAs', "`"$csv`"" -Wait
if (-not (Test-Path $csv)) { throw 'Procmon не создал CSV' }

# 4. профиль
& $py (Join-Path $PSScriptRoot 'procmon_profile.py') $csv $cmd.Id $Logs
if ($LASTEXITCODE -ne 0) { throw "procmon_profile.py завершился с кодом $LASTEXITCODE" }
Copy-Item (Join-Path $Work 'scenario_out.txt') (Join-Path $Logs 'procmon_scenario_out.txt') -Force
