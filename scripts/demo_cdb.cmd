@echo off
rem Live demo: cmd.exe runs scenario.cmd under cdb, only key syscalls are printed.
rem Usage: set CDB=<path to cdb.exe> & demo_cdb.cmd <dir with demo.wds> <scenario dir>
if "%CDB%"=="" (echo CDB is not set & exit /b 1)
cd /d "%~2" || exit /b 1
echo %CD%^> cdb -G -c "$$<demo.wds" cmd.exe /c scenario.cmd
"%CDB%" -G -c "$$<%~1\demo.wds" cmd.exe /c scenario.cmd | findstr /b /c:"SC|" /c:"LAB_VAR" /c:"Hello" /c:"second" /c:"a.txt" /c:"c.txt" /c:"the-" | findstr /v /c:"scenario.cmd" /c:"printf" /c:"MountPointManager" /c:"AppLocker" /c:"??" | powershell -NoProfile -Command "$input | Where-Object { -not $_.TrimEnd().EndsWith([string][char]92) -and $_.TrimEnd() -notmatch 'len=2$' }"
