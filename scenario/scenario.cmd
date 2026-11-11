@echo off
rem ------------------------------------------------------------------
rem  Lab 1. Test scenario for cmd.exe: every block exercises one
rem  functional area of the command interpreter.
rem ------------------------------------------------------------------

rem [1] environment variables (process environment block)
set LAB_VAR=lab1
echo LAB_VAR=%LAB_VAR%

rem [2] directories: create + change current directory
mkdir sandbox
cd sandbox

rem [3] file create / write / append (redirection > and >>)
echo Hello from cmd.exe> a.txt
echo second line>> a.txt

rem [4] file read + console output
type a.txt

rem [5] copy, rename, directory listing
copy a.txt b.txt >nul
ren b.txt c.txt
dir /b

rem [6] start an external program (child process) and wait for it
hostname

rem [7] delete files and directory
del a.txt c.txt
cd ..
rmdir sandbox

exit /b 0
