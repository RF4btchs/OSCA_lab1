<#
  Лабораторная работа №1. Трассировка системных вызовов cmd.exe отладчиком cdb (WinDbg).

  1. Из ntdll.dll извлекается список заглушек системных вызовов (ntdll_syscalls.py).
  2. Генерируется bps.wds — по точке останова на каждую заглушку. Для важных вызовов
     используется скрипт, печатающий аргументы (имя файла, ключ реестра, командная строка
     дочернего процесса и т.д.); остальные печатают только имя. На адрес возврата
     ставится одноразовая точка останова, которая печатает NTSTATUS результата.
  3. cdb запускает cmd.exe /c scenario.cmd, лог пишется в logs\cdb_raw.log.
  4. analyze.py строит профиль (группы системных вызовов) по логу.

  Запуск:  powershell -ExecutionPolicy Bypass -File scripts\run_trace.ps1
#>
$ErrorActionPreference = 'Stop'

$Lab     = Split-Path -Parent $PSScriptRoot
$Work    = Join-Path $env:TEMP 'lab1_trace'      # путь без пробелов и кириллицы — cdb так надёжнее
$CdbDir  = Join-Path $Work 'cdb'
$RunDir  = Join-Path $Work 'run'
$Logs    = Join-Path $Lab 'logs'
$py      = (Get-Command python -ErrorAction Stop).Source

# --- поиск cdb.exe (пакет WinDbg из Microsoft Store/winget или Windows SDK) ----------
$cdb = $null
$pkg = Get-AppxPackage Microsoft.WinDbg -ErrorAction SilentlyContinue
if ($pkg) { $cdb = Join-Path $pkg.InstallLocation 'amd64\cdb.exe' }
if (-not $cdb -or -not (Test-Path $cdb)) {
    $cdb = 'C:\Program Files (x86)\Windows Kits\10\Debuggers\x64\cdb.exe'
}
if (-not (Test-Path $cdb)) { throw "cdb.exe не найден. Установите: winget install Microsoft.WinDbg" }

# --- подготовка каталогов ------------------------------------------------------------
foreach ($d in $Work, $CdbDir, $RunDir, $Logs) { New-Item -ItemType Directory -Force $d | Out-Null }
$dirFwd = $CdbDir -replace '\\', '/'

Get-ChildItem (Join-Path $PSScriptRoot 'cdb') -Filter *.wds | ForEach-Object {
    (Get-Content $_.FullName -Raw) -replace '@@DIR@@', $dirFwd |
        Set-Content -Encoding ascii (Join-Path $CdbDir $_.Name)
}
Copy-Item (Join-Path $Lab 'scenario\scenario.cmd') $RunDir -Force

# --- список системных вызовов из ntdll.dll ----------------------------------------------
$tsv = Join-Path $Logs 'ntdll_syscalls.tsv'
& $py (Join-Path $PSScriptRoot 'ntdll_syscalls.py') "$env:SystemRoot\System32\ntdll.dll" |
    Set-Content -Encoding utf8 $tsv
if ($LASTEXITCODE -ne 0) { throw "ntdll_syscalls.py завершился с кодом $LASTEXITCODE" }

# Вызовы, для которых печатаются аргументы (имя -> скрипт cdb)
$special = @{
    'NtCreateFile'='file_create'; 'NtOpenFile'='file_open'; 'NtOpenKey'='oa_r8'; 'NtOpenKeyEx'='oa_r8'
    'NtCreateKey'='oa_r8'; 'NtOpenSection'='oa_r8'; 'NtOpenDirectoryObject'='oa_r8'
    'NtOpenSymbolicLinkObject'='oa_r8'; 'NtOpenEvent'='oa_r8'; 'NtOpenSemaphore'='oa_r8'
    'NtQueryAttributesFile'='oa_rcx'; 'NtQueryFullAttributesFile'='oa_rcx'; 'NtDeleteFile'='oa_rcx'
    'NtQueryValueKey'='us_rdx'; 'NtSetValueKey'='us_rdx'; 'NtDeleteValueKey'='us_rdx'
    'NtCreateUserProcess'='proc'
    'NtQueryInformationFile'='fileinfo'; 'NtSetInformationFile'='fileinfo'
    'NtReadFile'='rw'; 'NtWriteFile'='rw'
    'NtDeviceIoControlFile'='ioctl'; 'NtFsControlFile'='ioctl'
    'NtQueryDirectoryFile'='dir'; 'NtQueryDirectoryFileEx'='dir'
    'NtClose'='handle'; 'NtWaitForSingleObject'='handle'; 'NtQueryVolumeInformationFile'='handle'
    'NtAllocateVirtualMemory'='alloc'
}

$bps = foreach ($line in Get-Content $tsv) {
    $name = ($line -split "`t")[0]
    $script = if ($special.ContainsKey($name)) { $special[$name] } else { 'gen' }
    "bp ntdll!$name `"`$`$<$dirFwd/$script.wds`""
}
Set-Content -Encoding ascii (Join-Path $CdbDir 'bps.wds') $bps
Write-Host "Точек останова: $($bps.Count)"

# --- запуск cmd.exe под отладчиком ---------------------------------------------------------
$env:_NT_SYMBOL_PATH = "srv*$env:TEMP\symcache*https://msdl.microsoft.com/download/symbols"
# Стандартное окружение Windows, чтобы cmd.exe нашёл системные программы, а не их аналоги
# из сторонних каталогов PATH (Git, MSYS и т.п.).
$env:PATH    = "$env:SystemRoot\system32;$env:SystemRoot;$env:SystemRoot\System32\Wbem;$env:SystemRoot\System32\WindowsPowerShell\v1.0"
$env:PATHEXT = '.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC'
# стандартное поведение поиска программ: сначала текущий каталог, затем PATH
Remove-Item Env:NoDefaultCurrentDirectoryInExePath -ErrorAction SilentlyContinue
$raw = Join-Path $Work 'cdb_raw.log'
Remove-Item $raw -ErrorAction SilentlyContinue
$console = Join-Path $Work 'cdb_console.txt'
# -G   : не останавливаться на финальной точке останова (cdb выходит вместе с cmd.exe)
# -logou: лог в UTF-16, чтобы не терять кириллицу в путях
# Рабочий каталог задаётся явно: cmd.exe ищет scenario.cmd и создаёт sandbox в нём.
$p = Start-Process -FilePath $cdb -WorkingDirectory $RunDir -NoNewWindow -Wait -PassThru `
        -RedirectStandardOutput $console `
        -ArgumentList @('-G', '-logou', $raw, '-c', "`"`$`$<$dirFwd/main.wds`"",
                        "$env:SystemRoot\System32\cmd.exe", '/c', (Join-Path $RunDir 'scenario.cmd'))
Write-Host "cdb завершился с кодом $($p.ExitCode)"
if (-not (Test-Path $raw)) { throw 'cdb не создал лог' }
Copy-Item $raw (Join-Path $Logs 'cdb_raw.log') -Force
Copy-Item $console (Join-Path $Logs 'cdb_console.txt') -Force

# --- анализ --------------------------------------------------------------------------------
& $py (Join-Path $PSScriptRoot 'analyze.py') (Join-Path $Logs 'cdb_raw.log') $tsv $Logs
if ($LASTEXITCODE -ne 0) { throw "analyze.py завершился с кодом $LASTEXITCODE" }
