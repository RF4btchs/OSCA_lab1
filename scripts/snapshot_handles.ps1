<#
  Лабораторная работа №1. Снимок дескрипторов и состояния работающего cmd.exe.

  Запускается cmd.exe, который перенаправляет вывод в файл held.txt и ждёт
  дочерний процесс (ping). Пока cmd.exe ждёт, снимаются:
    * handle64.exe -a -p <PID>  — все дескрипторы процесса (Sysinternals Handle);
    * cdb -pv -p <PID>          — неинвазивное подключение WinDbg: модули (lm),
                                  стеки потоков (~*k), PEB (!peb), дескрипторы (!handle).
  Результаты: logs\handle_cmd.txt, logs\windbg_session.txt.

  Запуск:  powershell -ExecutionPolicy Bypass -File scripts\snapshot_handles.ps1
#>
$ErrorActionPreference = 'Stop'

$Lab    = Split-Path -Parent $PSScriptRoot
$Logs   = Join-Path $Lab 'logs'
$Handle = Join-Path $Lab 'tools\Handle\handle64.exe'
$Work   = Join-Path $env:TEMP 'lab1_handles'
New-Item -ItemType Directory -Force $Work, $Logs | Out-Null
if (-not (Test-Path $Handle)) { throw "не найден $Handle" }

$cdb = $null
$pkg = Get-AppxPackage Microsoft.WinDbg -ErrorAction SilentlyContinue
if ($pkg) { $cdb = Join-Path $pkg.InstallLocation 'amd64\cdb.exe' }
if (-not $cdb -or -not (Test-Path $cdb)) { throw 'cdb.exe не найден (winget install Microsoft.WinDbg)' }

$env:PATH    = "$env:SystemRoot\system32;$env:SystemRoot;$env:SystemRoot\System32\Wbem"
$env:PATHEXT = '.COM;.EXE;.BAT;.CMD'
# стандартное поведение поиска программ: сначала текущий каталог, затем PATH
Remove-Item Env:NoDefaultCurrentDirectoryInExePath -ErrorAction SilentlyContinue
$env:_NT_SYMBOL_PATH = "srv*$env:TEMP\symcache*https://msdl.microsoft.com/download/symbols"

# cmd.exe держит открытым held.txt (перенаправление) и ждёт ping ~8 секунд
$cmdLine = '/c "(echo held by cmd.exe & ping -n 9 127.0.0.1 >nul) > held.txt"'
$proc = Start-Process "$env:SystemRoot\System32\cmd.exe" -ArgumentList $cmdLine `
            -WorkingDirectory $Work -WindowStyle Hidden -PassThru
Start-Sleep -Seconds 2
if ($proc.HasExited) { throw "cmd.exe завершился раньше времени, код $($proc.ExitCode)" }
$cmdPid = $proc.Id
Write-Host "cmd.exe PID = $cmdPid"

$child = Get-CimInstance Win32_Process -Filter "ParentProcessId = $cmdPid AND Name <> 'conhost.exe'" |
         Select-Object -First 1 ProcessId, Name, CommandLine

# --- Sysinternals Handle ---------------------------------------------------------
$h = & $Handle -accepteula -nobanner -a -p $cmdPid 2>&1
if ($LASTEXITCODE -ne 0) { Write-Warning "handle64.exe вернул код $LASTEXITCODE" }
@("# handle64.exe -a -p $cmdPid   (cmd.exe $cmdLine)",
  "# дочерний процесс: $($child.Name) PID=$($child.ProcessId) $($child.CommandLine)",
  '') + $h | Set-Content -Encoding utf8 (Join-Path $Logs 'handle_cmd.txt')

# --- WinDbg (cdb), неинвазивное подключение -----------------------------------------
$dbgCmds = '.echo ===== lm (modules); lm; .echo ===== ~*k (threads); ~*k; ' +
           '.echo ===== !peb; !peb; .echo ===== !handle 0 1; !handle 0 1; ' +
           '.echo ===== !handle 0 f File; !handle 0 f File; qd'
$out = & $cdb -pv -p $cmdPid -c $dbgCmds 2>&1
$out | Set-Content -Encoding utf8 (Join-Path $Logs 'windbg_session.txt')

$proc.WaitForExit(20000) | Out-Null
Write-Host "Готово: logs\handle_cmd.txt, logs\windbg_session.txt"
