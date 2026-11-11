# Системные вызовы по блокам сценария scenario.cmd

## [0] Инициализация cmd.exe (до первой строки сценария)

Системных вызовов: 976

| Вызов | Кол-во |
|---|---:|
| NtProtectVirtualMemory | 118 |
| NtClose | 102 |
| NtOpenKey | 74 |
| NtQueryVirtualMemory | 67 |
| NtAllocateVirtualMemory | 54 |
| NtDeviceIoControlFile | 48 |
| NtOpenFile | 44 |
| NtTraceControl | 40 |
| NtSetInformationFile | 38 |
| NtQueryValueKey | 33 |
| NtQueryInformationToken | 32 |
| NtQueryVolumeInformationFile | 29 |
| NtQueryKey | 27 |
| NtQueryInformationFile | 27 |
| NtQuerySystemInformation | 25 |

Ключевые вызовы:

```
NtQueryValueKey(h=0000000000000064;value=) = STATUS_SUCCESS
NtQueryValueKey(h=0000000000000064;value=000605xx) = STATUS_SUCCESS
NtQueryValueKey(h=0000000000000068;value=SmtDelaySleepLoopWindowSize) = STATUS_OBJECT_NAME_NOT_FOUND
NtQueryValueKey(h=0000000000000068;value=SmtDelaySpinCountThreshold) = STATUS_OBJECT_NAME_NOT_FOUND
NtQueryValueKey(h=0000000000000068;value=SmtDelayBaseYield) = STATUS_OBJECT_NAME_NOT_FOUND
NtQueryValueKey(h=0000000000000068;value=SmtFactorYield) = STATUS_OBJECT_NAME_NOT_FOUND
NtQueryValueKey(h=0000000000000068;value=SmtDelayMaxYield) = STATUS_OBJECT_NAME_NOT_FOUND
NtQueryValueKey(h=00000000000000b4;value=PreferredUILanguages) = STATUS_OBJECT_NAME_NOT_FOUND
NtQueryValueKey(h=0000000000000068;value=MachinePreferredUILanguages) = STATUS_BUFFER_OVERFLOW
NtQueryValueKey(h=0000000000000068;value=MachinePreferredUILanguages) = STATUS_SUCCESS
NtQueryValueKey(h=00000000000000b4;value=PreferredUILanguages) = STATUS_OBJECT_NAME_NOT_FOUND
NtQueryValueKey(h=00000000000000bc;value=DisableUNCCheck) = STATUS_OBJECT_NAME_NOT_FOUND
NtQueryValueKey(h=00000000000000bc;value=EnableExtensions) = STATUS_SUCCESS
NtQueryValueKey(h=00000000000000bc;value=DelayedExpansion) = STATUS_OBJECT_NAME_NOT_FOUND
NtQueryValueKey(h=00000000000000bc;value=DefaultColor) = STATUS_SUCCESS
NtQueryValueKey(h=00000000000000bc;value=CompletionChar) = STATUS_SUCCESS
NtQueryValueKey(h=00000000000000bc;value=PathCompletionChar) = STATUS_SUCCESS
NtQueryValueKey(h=00000000000000bc;value=InteractiveExtensionLevel) = STATUS_SUCCESS
NtQueryValueKey(h=00000000000000bc;value=LockBatchFilesWhenInUse) = STATUS_SUCCESS
NtQueryValueKey(h=00000000000000bc;value=AutoRun) = STATUS_OBJECT_NAME_NOT_FOUND
NtQueryValueKey(h=00000000000000bc;value=SafeDllSearchMode) = STATUS_OBJECT_NAME_NOT_FOUND
NtQueryAttributesFile(root=0000000000000000;name=C:\WINDOWS\System32\Wldp.dll) = STATUS_SUCCESS
NtOpenFile(root=0000000000000000;access=100021;share=5;opts=60;name=C:\WINDOWS\System32\Wldp.dll) = STATUS_SUCCESS, h=0xc0
NtQueryValueKey(h=00000000000000c8;value=PageAllocatorUseSystemHeap) = STATUS_OBJECT_NAME_NOT_FOUND
NtQueryValueKey(h=00000000000000c0;value=PageAllocatorSystemHeapIsPrivate) = STATUS_OBJECT_NAME_NOT_FOUND
NtQueryValueKey(h=00000000000000c4;value=AggressiveMTATesting) = STATUS_OBJECT_NAME_NOT_FOUND
NtWaitForSingleObject(h=0000000000000118) = STATUS_SUCCESS
NtWaitForSingleObject(h=000000000000011c) = STATUS_SUCCESS
NtWaitForSingleObject(h=0000000000000120) = STATUS_SUCCESS
NtWaitForSingleObject(h=0000000000000134) = STATUS_SUCCESS
NtQueryValueKey(h=0000000000000144;value=Type) = STATUS_SUCCESS
NtQueryValueKey(h=0000000000000144;value=Latest) = STATUS_SUCCESS
NtOpenFile(root=0000000000000000;access=100001;share=5;opts=60;name=C:\Program Files\WindowsApps\Microsoft.LanguageExperiencePackru-RU_26100.173.281.0_neutral__8wekyb3d8bbwe\Windows\SYSTEM32\ru-RU\7a3ed5582884d5a8ddb01b818196742f\ntdll.dll.mui) = STATUS_SUCCESS, h=0x148
NtQueryAttributesFile(root=0000000000000000;name=C:\Users\sokol\AppData\Local\Temp\lab1_trace\run) = STATUS_SUCCESS
NtOpenFile(root=0000000000000000;access=100001;share=7;opts=4021;name=C:\) = STATUS_SUCCESS, h=0x144
NtQueryDirectoryFileEx(h=0000000000000144;class=3;mask=Users) = STATUS_SUCCESS
NtOpenFile(root=0000000000000000;access=100001;share=7;opts=4021;name=C:\Users\) = STATUS_SUCCESS, h=0x14c
NtQueryDirectoryFileEx(h=000000000000014c;class=3;mask=sokol) = STATUS_SUCCESS
NtOpenFile(root=0000000000000000;access=100001;share=7;opts=4021;name=C:\Users\sokol\) = STATUS_SUCCESS, h=0x144
NtQueryDirectoryFileEx(h=0000000000000144;class=3;mask=AppData) = STATUS_SUCCESS
```

## [1] environment variables (process environment block)

Команды: `set LAB_VAR=lab1`; `echo LAB_VAR=%LAB_VAR%`

Системных вызовов: 91

| Вызов | Кол-во |
|---|---:|
| NtSetInformationFile | 24 |
| NtDeviceIoControlFile | 17 |
| NtQueryInformationFile | 16 |
| NtQuerySystemInformation | 12 |
| NtQueryVolumeInformationFile | 9 |
| NtReadFile | 4 |
| NtClose | 4 |
| NtCreateFile | 4 |
| NtWriteFile | 1 |

Ключевые вызовы:

```
NtReadFile(h=0000000000000188;len=8191) = STATUS_SUCCESS
NtCreateFile(root=0000000000000000;access=80100080;disp=1;opts=60;name=C:\Users\sokol\AppData\Local\Temp\lab1_trace\run\scenario.cmd) = STATUS_SUCCESS, h=0x188
NtReadFile(h=0000000000000188;len=8191) = STATUS_SUCCESS
NtCreateFile(root=0000000000000000;access=80100080;disp=1;opts=60;name=C:\Users\sokol\AppData\Local\Temp\lab1_trace\run\scenario.cmd) = STATUS_SUCCESS, h=0x184
NtReadFile(h=0000000000000184;len=8191) = STATUS_SUCCESS
NtWriteFile(h=0000000000000c64;len=14) = STATUS_SUCCESS
NtCreateFile(root=0000000000000000;access=80100080;disp=1;opts=60;name=C:\Users\sokol\AppData\Local\Temp\lab1_trace\run\scenario.cmd) = STATUS_SUCCESS, h=0x150
NtReadFile(h=0000000000000150;len=8191) = STATUS_SUCCESS
NtCreateFile(root=0000000000000000;access=80100080;disp=1;opts=60;name=C:\Users\sokol\AppData\Local\Temp\lab1_trace\run\scenario.cmd) = STATUS_SUCCESS, h=0x188
```

## [2] directories: create + change current directory

Команды: `mkdir sandbox`; `cd sandbox`

Системных вызовов: 120

| Вызов | Кол-во |
|---|---:|
| NtSetInformationFile | 24 |
| NtDeviceIoControlFile | 17 |
| NtQueryInformationFile | 16 |
| NtClose | 14 |
| NtQuerySystemInformation | 12 |
| NtQueryVolumeInformationFile | 9 |
| NtOpenFile | 9 |
| NtQueryDirectoryFileEx | 8 |
| NtCreateFile | 5 |
| NtReadFile | 4 |
| NtQueryAttributesFile | 2 |

Ключевые вызовы:

```
NtReadFile(h=0000000000000188;len=8191) = STATUS_SUCCESS
NtCreateFile(root=0000000000000000;access=80100080;disp=1;opts=60;name=C:\Users\sokol\AppData\Local\Temp\lab1_trace\run\scenario.cmd) = STATUS_SUCCESS, h=0x184
NtReadFile(h=0000000000000184;len=8191) = STATUS_SUCCESS
NtCreateFile(root=000000000000005c;access=100001;disp=2;opts=204021;name=sandbox) = STATUS_SUCCESS, h=0x184
NtCreateFile(root=0000000000000000;access=80100080;disp=1;opts=60;name=C:\Users\sokol\AppData\Local\Temp\lab1_trace\run\scenario.cmd) = STATUS_SUCCESS, h=0x178
NtReadFile(h=0000000000000178;len=8191) = STATUS_SUCCESS
NtQueryAttributesFile(root=0000000000000000;name=C:\Users\sokol\AppData\Local\Temp\lab1_trace\run\sandbox) = STATUS_SUCCESS
NtOpenFile(root=0000000000000000;access=100001;share=7;opts=4021;name=C:\) = STATUS_SUCCESS, h=0x18c
NtQueryDirectoryFileEx(h=000000000000018c;class=3;mask=Users) = STATUS_SUCCESS
NtOpenFile(root=0000000000000000;access=100001;share=7;opts=4021;name=C:\Users\) = STATUS_SUCCESS, h=0x14c
NtQueryDirectoryFileEx(h=000000000000014c;class=3;mask=sokol) = STATUS_SUCCESS
NtOpenFile(root=0000000000000000;access=100001;share=7;opts=4021;name=C:\Users\sokol\) = STATUS_SUCCESS, h=0x14c
NtQueryDirectoryFileEx(h=000000000000014c;class=3;mask=AppData) = STATUS_SUCCESS
NtOpenFile(root=0000000000000000;access=100001;share=7;opts=4021;name=C:\Users\sokol\AppData\) = STATUS_SUCCESS, h=0x18c
NtQueryDirectoryFileEx(h=000000000000018c;class=3;mask=Local) = STATUS_SUCCESS
NtOpenFile(root=0000000000000000;access=100001;share=7;opts=4021;name=C:\Users\sokol\AppData\Local\) = STATUS_SUCCESS, h=0x18c
NtQueryDirectoryFileEx(h=000000000000018c;class=3;mask=Temp) = STATUS_SUCCESS
NtOpenFile(root=0000000000000000;access=100001;share=7;opts=4021;name=C:\Users\sokol\AppData\Local\Temp\) = STATUS_SUCCESS, h=0x178
NtQueryDirectoryFileEx(h=0000000000000178;class=3;mask=lab1_trace) = STATUS_SUCCESS
NtOpenFile(root=0000000000000000;access=100001;share=7;opts=4021;name=C:\Users\sokol\AppData\Local\Temp\lab1_trace\) = STATUS_SUCCESS, h=0x188
NtQueryDirectoryFileEx(h=0000000000000188;class=3;mask=run) = STATUS_SUCCESS
NtOpenFile(root=0000000000000000;access=100001;share=7;opts=4021;name=C:\Users\sokol\AppData\Local\Temp\lab1_trace\run\) = STATUS_SUCCESS, h=0x170
NtQueryDirectoryFileEx(h=0000000000000170;class=3;mask=sandbox) = STATUS_SUCCESS
NtQueryAttributesFile(root=0000000000000000;name=C:\Users\sokol\AppData\Local\Temp\lab1_trace\run\sandbox) = STATUS_SUCCESS
NtOpenFile(root=0000000000000000;access=100020;share=3;opts=21;name=C:\Users\sokol\AppData\Local\Temp\lab1_trace\run\sandbox) = STATUS_SUCCESS, h=0x170
NtCreateFile(root=0000000000000000;access=80100080;disp=1;opts=60;name=C:\Users\sokol\AppData\Local\Temp\lab1_trace\run\scenario.cmd) = STATUS_SUCCESS, h=0x5c
NtReadFile(h=000000000000005c;len=8191) = STATUS_SUCCESS
NtCreateFile(root=0000000000000000;access=80100080;disp=1;opts=60;name=C:\Users\sokol\AppData\Local\Temp\lab1_trace\run\scenario.cmd) = STATUS_SUCCESS, h=0x5c
```

## [3] file create / write / append (redirection > and >>)

Команды: `echo Hello from cmd.exe> a.txt`; `echo second line>> a.txt`

Системных вызовов: 120

| Вызов | Кол-во |
|---|---:|
| NtSetInformationFile | 27 |
| NtQueryInformationFile | 20 |
| NtQueryVolumeInformationFile | 17 |
| NtDeviceIoControlFile | 17 |
| NtQuerySystemInformation | 12 |
| NtClose | 10 |
| NtCreateFile | 6 |
| NtReadFile | 5 |
| NtDuplicateObject | 4 |
| NtWriteFile | 2 |

Ключевые вызовы:

```
NtReadFile(h=000000000000005c;len=8191) = STATUS_SUCCESS
NtCreateFile(root=0000000000000000;access=80100080;disp=1;opts=60;name=C:\Users\sokol\AppData\Local\Temp\lab1_trace\run\scenario.cmd) = STATUS_SUCCESS, h=0x150
NtReadFile(h=0000000000000150;len=8191) = STATUS_SUCCESS
NtCreateFile(root=0000000000000170;access=40100080;disp=5;opts=60;name=a.txt) = STATUS_SUCCESS, h=0xc64
NtWriteFile(h=0000000000000c64;len=20) = STATUS_SUCCESS
NtCreateFile(root=0000000000000000;access=80100080;disp=1;opts=60;name=C:\Users\sokol\AppData\Local\Temp\lab1_trace\run\scenario.cmd) = STATUS_SUCCESS, h=0x184
NtReadFile(h=0000000000000184;len=8191) = STATUS_SUCCESS
NtCreateFile(root=0000000000000170;access=c0100080;disp=1;opts=60;name=a.txt) = STATUS_SUCCESS, h=0x174
NtReadFile(h=0000000000000174;len=1) = STATUS_SUCCESS
NtWriteFile(h=0000000000000174;len=13) = STATUS_SUCCESS
NtCreateFile(root=0000000000000000;access=80100080;disp=1;opts=60;name=C:\Users\sokol\AppData\Local\Temp\lab1_trace\run\scenario.cmd) = STATUS_SUCCESS, h=0x18c
NtReadFile(h=000000000000018c;len=8191) = STATUS_SUCCESS
NtCreateFile(root=0000000000000000;access=80100080;disp=1;opts=60;name=C:\Users\sokol\AppData\Local\Temp\lab1_trace\run\scenario.cmd) = STATUS_SUCCESS, h=0x18c
```

## [4] file read + console output

Команды: `type a.txt`

Системных вызовов: 82

| Вызов | Кол-во |
|---|---:|
| NtSetInformationFile | 20 |
| NtQueryInformationFile | 14 |
| NtDeviceIoControlFile | 11 |
| NtQueryVolumeInformationFile | 10 |
| NtQuerySystemInformation | 9 |
| NtClose | 5 |
| NtReadFile | 4 |
| NtCreateFile | 4 |
| NtQueryDirectoryFileEx | 2 |
| NtOpenFile | 1 |
| NtQueryAttributesFile | 1 |
| NtWriteFile | 1 |

Ключевые вызовы:

```
NtReadFile(h=000000000000018c;len=8191) = STATUS_SUCCESS
NtCreateFile(root=0000000000000000;access=80100080;disp=1;opts=60;name=C:\Users\sokol\AppData\Local\Temp\lab1_trace\run\scenario.cmd) = STATUS_SUCCESS, h=0xc64
NtReadFile(h=0000000000000c64;len=8191) = STATUS_SUCCESS
NtOpenFile(root=0000000000000000;access=100001;share=7;opts=4021;name=C:\Users\sokol\AppData\Local\Temp\lab1_trace\run\sandbox\) = STATUS_SUCCESS, h=0xc64
NtQueryDirectoryFileEx(h=0000000000000c64;class=2;mask=a.txt) = STATUS_SUCCESS
NtQueryAttributesFile(root=0000000000000000;name=C:\Users\sokol\AppData\Local\Temp\lab1_trace\run\sandbox\a.txt) = STATUS_SUCCESS
NtCreateFile(root=0000000000000170;access=80100080;disp=1;opts=60;name=a.txt) = STATUS_SUCCESS, h=0x150
NtReadFile(h=0000000000000150;len=512) = STATUS_SUCCESS
NtWriteFile(h=0000000000000188;len=33) = STATUS_SUCCESS
NtQueryDirectoryFileEx(h=0000000000000c64;class=2;mask=) = STATUS_NO_MORE_FILES
NtCreateFile(root=0000000000000000;access=80100080;disp=1;opts=60;name=C:\Users\sokol\AppData\Local\Temp\lab1_trace\run\scenario.cmd) = STATUS_SUCCESS, h=0x17c
NtReadFile(h=000000000000017c;len=8191) = STATUS_SUCCESS
NtCreateFile(root=0000000000000000;access=80100080;disp=1;opts=60;name=C:\Users\sokol\AppData\Local\Temp\lab1_trace\run\scenario.cmd) = STATUS_SUCCESS, h=0x17c
```

## [5] copy, rename, directory listing

Команды: `copy a.txt b.txt >nul`; `ren b.txt c.txt`; `dir /b`

Системных вызовов: 314

| Вызов | Кол-во |
|---|---:|
| NtSetInformationFile | 35 |
| NtQueryInformationFile | 32 |
| NtQueryVolumeInformationFile | 27 |
| NtClose | 27 |
| NtDeviceIoControlFile | 25 |
| NtSetInformationProcess | 18 |
| NtQueryInformationProcess | 16 |
| NtQuerySystemInformation | 15 |
| NtProtectVirtualMemory | 15 |
| NtQueryVirtualMemory | 14 |
| NtQueryAttributesFile | 11 |
| NtCreateFile | 9 |
| NtAllocateVirtualMemory | 9 |
| NtOpenFile | 8 |
| NtCreateSemaphore | 8 |

Ключевые вызовы:

```
NtReadFile(h=000000000000017c;len=8191) = STATUS_SUCCESS
NtCreateFile(root=0000000000000000;access=80100080;disp=1;opts=60;name=C:\Users\sokol\AppData\Local\Temp\lab1_trace\run\scenario.cmd) = STATUS_SUCCESS, h=0x150
NtReadFile(h=0000000000000150;len=8191) = STATUS_SUCCESS
NtCreateFile(root=0000000000000000;access=40100080;disp=5;opts=60;name=nul) = STATUS_SUCCESS, h=0x188
NtQueryAttributesFile(root=0000000000000000;name=C:\Users\sokol\AppData\Local\Temp\lab1_trace\run\sandbox\a.txt) = STATUS_SUCCESS
NtOpenFile(root=0000000000000000;access=100001;share=7;opts=4021;name=C:\Users\sokol\AppData\Local\Temp\lab1_trace\run\sandbox\) = STATUS_SUCCESS, h=0x184
NtQueryDirectoryFileEx(h=0000000000000184;class=2;mask=a.txt) = STATUS_SUCCESS
NtCreateFile(root=0000000000000170;access=80100080;disp=1;opts=64;name=a.txt) = STATUS_SUCCESS, h=0x150
NtReadFile(h=0000000000000150;len=512) = STATUS_SUCCESS
NtQueryAttributesFile(root=0000000000000000;name=C:\Users\sokol\AppData\Local\Temp\lab1_trace\run\sandbox\b.txt) = STATUS_OBJECT_NAME_NOT_FOUND
NtQueryAttributesFile(root=0000000000000000;name=C:\Users\sokol\AppData\Local\Temp\lab1_trace\run\sandbox\b.txt) = STATUS_OBJECT_NAME_NOT_FOUND
NtQueryValueKey(h=0000000000000c64;value=CopyFileBufferedSynchronousIo) = STATUS_OBJECT_NAME_NOT_FOUND
NtCreateFile(root=0000000000000000;access=80100080;disp=1;opts=10200044;name=C:\Users\sokol\AppData\Local\Temp\lab1_trace\run\sandbox\a.txt) = STATUS_SUCCESS, h=0xc64
NtCreateFile(root=0000000000000000;access=c0150081;disp=5;opts=10000044;name=C:\Users\sokol\AppData\Local\Temp\lab1_trace\run\sandbox\b.txt) = STATUS_SUCCESS, h=0x18c
NtQueryAttributesFile(root=0000000000000000;name=C:\WINDOWS\SYSTEM32\ntmarta.dll) = STATUS_SUCCESS
NtOpenFile(root=0000000000000000;access=100021;share=5;opts=60;name=C:\WINDOWS\SYSTEM32\ntmarta.dll) = STATUS_SUCCESS, h=0x174
NtSetInformationFile(h=000000000000018c; FileEndOfFileInformation) = STATUS_SUCCESS
NtQueryValueKey(h=000000000000019c;value=CopyFileChunkSize) = STATUS_OBJECT_NAME_NOT_FOUND
NtQueryValueKey(h=000000000000019c;value=CopyFileOverlappedCount) = STATUS_OBJECT_NAME_NOT_FOUND
NtSetInformationFile(h=000000000000018c; FileBasicInformation) = STATUS_SUCCESS
NtQueryAttributesFile(root=0000000000000000;name=C:\Users\sokol\AppData\Local\Temp\lab1_trace\run\sandbox\b.txt) = STATUS_SUCCESS
NtOpenFile(root=0000000000000170;access=100100;share=7;opts=204020;name=b.txt) = STATUS_SUCCESS, h=0xc64
NtSetInformationFile(h=0000000000000c64; FileBasicInformation) = STATUS_SUCCESS
NtQueryDirectoryFileEx(h=0000000000000184;class=2;mask=) = STATUS_NO_MORE_FILES
NtQueryValueKey(h=0000000000000150;value=Type) = STATUS_SUCCESS
NtQueryValueKey(h=0000000000000150;value=Latest) = STATUS_SUCCESS
NtOpenFile(root=0000000000000000;access=100001;share=5;opts=60;name=C:\Program Files\WindowsApps\Microsoft.LanguageExperiencePackru-RU_26100.173.281.0_neutral__8wekyb3d8bbwe\Windows\System32\ru-RU\d16a9991ff1a65d4c8a53640d31325fd\cmd.exe.mui) = STATUS_SUCCESS, h=0x184
NtWriteFile(h=0000000000000188;len=32) = STATUS_SUCCESS
NtCreateFile(root=0000000000000000;access=80100080;disp=1;opts=60;name=C:\Users\sokol\AppData\Local\Temp\lab1_trace\run\scenario.cmd) = STATUS_SUCCESS, h=0x17c
NtReadFile(h=000000000000017c;len=8191) = STATUS_SUCCESS
NtQueryAttributesFile(root=0000000000000000;name=C:\Users\sokol\AppData\Local\Temp\lab1_trace\run\sandbox\b.txt) = STATUS_SUCCESS
NtQueryAttributesFile(root=0000000000000000;name=C:\Users\sokol\AppData\Local\Temp\lab1_trace\run\sandbox\b.txt) = STATUS_SUCCESS
NtQueryAttributesFile(root=0000000000000000;name=C:\Users\sokol\AppData\Local\Temp\lab1_trace\run\sandbox\b.txt) = STATUS_SUCCESS
NtOpenFile(root=0000000000000000;access=100001;share=7;opts=4021;name=C:\Users\sokol\AppData\Local\Temp\lab1_trace\run\sandbox\) = STATUS_SUCCESS, h=0x188
NtQueryDirectoryFileEx(h=0000000000000188;class=2;mask=b.txt) = STATUS_SUCCESS
NtOpenFile(root=0000000000000000;access=110080;share=7;opts=204020;name=C:\Users\sokol\AppData\Local\Temp\lab1_trace\run\sandbox\b.txt) = STATUS_SUCCESS, h=0xc64
NtSetInformationFile(h=0000000000000c64; FileRenameInformation) = STATUS_SUCCESS
NtQueryDirectoryFileEx(h=0000000000000188;class=2;mask=) = STATUS_NO_MORE_FILES
NtCreateFile(root=0000000000000000;access=80100080;disp=1;opts=60;name=C:\Users\sokol\AppData\Local\Temp\lab1_trace\run\scenario.cmd) = STATUS_SUCCESS, h=0x17c
NtReadFile(h=000000000000017c;len=8191) = STATUS_SUCCESS
```

## [6] start an external program (child process) and wait for it

Команды: `hostname`

Системных вызовов: 165

| Вызов | Кол-во |
|---|---:|
| NtClose | 21 |
| NtSetInformationFile | 18 |
| NtQueryInformationProcess | 15 |
| NtDeviceIoControlFile | 14 |
| NtQueryInformationFile | 12 |
| NtOpenKey | 12 |
| NtQuerySystemInformation | 9 |
| NtQueryValueKey | 9 |
| NtQueryDirectoryFileEx | 8 |
| NtQueryVolumeInformationFile | 7 |
| NtSetInformationProcess | 6 |
| NtOpenFile | 6 |
| NtQueryInformationToken | 5 |
| NtCreateFile | 4 |
| NtReadFile | 3 |

Ключевые вызовы:

```
NtReadFile(h=000000000000019c;len=8191) = STATUS_SUCCESS
NtCreateFile(root=0000000000000000;access=80100080;disp=1;opts=60;name=C:\Users\sokol\AppData\Local\Temp\lab1_trace\run\scenario.cmd) = STATUS_SUCCESS, h=0x150
NtReadFile(h=0000000000000150;len=8191) = STATUS_SUCCESS
NtOpenFile(root=0000000000000000;access=100001;share=7;opts=4021;name=C:\Users\sokol\AppData\Local\Temp\lab1_trace\run\sandbox\) = STATUS_SUCCESS, h=0x198
NtQueryDirectoryFileEx(h=0000000000000198;class=2;mask=hostname"*) = STATUS_NO_SUCH_FILE
NtOpenFile(root=0000000000000000;access=100001;share=7;opts=4021;name=C:\Program Files\WindowsApps\Microsoft.WinDbg_1.2611.4001.0_x64__8wekyb3d8bbwe\amd64\) = STATUS_SUCCESS, h=0xc64
NtQueryDirectoryFileEx(h=0000000000000c64;class=2;mask=hostname"*) = STATUS_NO_SUCH_FILE
NtOpenFile(root=0000000000000000;access=100001;share=7;opts=4021;name=C:\WINDOWS\system32\) = STATUS_SUCCESS, h=0x5c
NtQueryDirectoryFileEx(h=000000000000005c;class=2;mask=hostname"*) = STATUS_SUCCESS
NtQueryDirectoryFileEx(h=000000000000005c;class=2;mask=) = STATUS_NO_MORE_FILES
NtOpenFile(root=0000000000000000;access=100001;share=7;opts=4021;name=C:\Users\sokol\AppData\Local\Temp\lab1_trace\run\sandbox\) = STATUS_SUCCESS, h=0x150
NtQueryDirectoryFileEx(h=0000000000000150;class=2;mask=hostname"*) = STATUS_NO_SUCH_FILE
NtOpenFile(root=0000000000000000;access=100001;share=7;opts=4021;name=C:\Program Files\WindowsApps\Microsoft.WinDbg_1.2611.4001.0_x64__8wekyb3d8bbwe\amd64\) = STATUS_SUCCESS, h=0x19c
NtQueryDirectoryFileEx(h=000000000000019c;class=2;mask=hostname"*) = STATUS_NO_SUCH_FILE
NtOpenFile(root=0000000000000000;access=100001;share=7;opts=4021;name=C:\WINDOWS\system32\) = STATUS_SUCCESS, h=0x198
NtQueryDirectoryFileEx(h=0000000000000198;class=2;mask=hostname"*) = STATUS_SUCCESS
NtQueryDirectoryFileEx(h=0000000000000198;class=2;mask=) = STATUS_NO_MORE_FILES
NtQueryValueKey(h=0000000000000064;value=000605xx) = STATUS_SUCCESS
NtCreateFile(root=0000000000000000;access=80100080;disp=1;opts=60;name=C:\WINDOWS\Globalization\Sorting\sortdefault.nls) = STATUS_SUCCESS, h=0x198
NtQueryValueKey(h=0000000000000198;value=ru-RU) = STATUS_OBJECT_NAME_NOT_FOUND
NtQueryValueKey(h=0000000000000198;value=ru) = STATUS_SUCCESS
NtQueryAttributesFile(root=0000000000000000;name=C:\Users\sokol\AppData\Local\Temp\lab1_trace\run\sandbox) = STATUS_SUCCESS
NtQueryValueKey(h=000000000000019c;value=HotPatchRestrictions) = STATUS_OBJECT_NAME_NOT_FOUND
NtCreateUserProcess(image=C:\WINDOWS\system32\HOSTNAME.EXE;cmdline=hostname) = STATUS_SUCCESS, h=0xc64
NtQueryValueKey(h=000000000000017c;value=TransparentEnabled) = STATUS_OBJECT_NAME_NOT_FOUND
NtQueryValueKey(h=000000000000017c;value=AuthenticodeEnabled) = STATUS_SUCCESS
NtQueryValueKey(h=000000000000019c;value=Cache) = STATUS_SUCCESS
NtQueryValueKey(h=00000000000001a0;value=C:\WINDOWS\system32\HOSTNAME.EXE) = STATUS_OBJECT_NAME_NOT_FOUND
NtQueryValueKey(h=00000000000001a0;value=PreferExternalManifest) = STATUS_OBJECT_NAME_NOT_FOUND
NtWaitForSingleObject(h=0000000000000c64) = STATUS_SUCCESS
NtCreateFile(root=0000000000000000;access=80100080;disp=1;opts=60;name=C:\Users\sokol\AppData\Local\Temp\lab1_trace\run\scenario.cmd) = STATUS_SUCCESS, h=0x188
NtReadFile(h=0000000000000188;len=8191) = STATUS_SUCCESS
NtCreateFile(root=0000000000000000;access=80100080;disp=1;opts=60;name=C:\Users\sokol\AppData\Local\Temp\lab1_trace\run\scenario.cmd) = STATUS_SUCCESS, h=0x150
```

## [7] delete files and directory

Команды: `del a.txt c.txt`; `cd ..`; `rmdir sandbox`

Системных вызовов: 281

| Вызов | Кол-во |
|---|---:|
| NtClose | 63 |
| NtSetInformationFile | 36 |
| NtQueryInformationFile | 28 |
| NtDeviceIoControlFile | 28 |
| NtQueryVolumeInformationFile | 17 |
| NtQuerySystemInformation | 16 |
| NtOpenFile | 16 |
| NtProtectVirtualMemory | 13 |
| NtQueryDirectoryFileEx | 11 |
| NtReadFile | 7 |
| NtQueryAttributesFile | 7 |
| NtSetInformationProcess | 7 |
| NtQueryInformationProcess | 6 |
| NtQueryVirtualMemory | 6 |
| NtCreateFile | 5 |

Ключевые вызовы:

```
NtReadFile(h=0000000000000150;len=8191) = STATUS_SUCCESS
NtCreateFile(root=0000000000000000;access=80100080;disp=1;opts=60;name=C:\Users\sokol\AppData\Local\Temp\lab1_trace\run\scenario.cmd) = STATUS_SUCCESS, h=0x1a0
NtReadFile(h=00000000000001a0;len=8191) = STATUS_SUCCESS
NtOpenFile(root=0000000000000000;access=100000;share=3;opts=4021;name=C:\) = STATUS_SUCCESS, h=0x1a4
NtQueryAttributesFile(root=0000000000000000;name=C:\Users\sokol\AppData\Local\Temp\lab1_trace\run\sandbox\a.txt) = STATUS_SUCCESS
NtQueryAttributesFile(root=0000000000000000;name=C:\Users\sokol\AppData\Local\Temp\lab1_trace\run\sandbox\a.txt) = STATUS_SUCCESS
NtOpenFile(root=0000000000000000;access=100000;share=3;opts=4021;name=C:\) = STATUS_SUCCESS, h=0x1a8
NtQueryAttributesFile(root=0000000000000000;name=C:\Users\sokol\AppData\Local\Temp\lab1_trace\run\sandbox\c.txt) = STATUS_SUCCESS
NtQueryAttributesFile(root=0000000000000000;name=C:\Users\sokol\AppData\Local\Temp\lab1_trace\run\sandbox\c.txt) = STATUS_SUCCESS
NtOpenFile(root=0000000000000000;access=100001;share=7;opts=4021;name=C:\Users\sokol\AppData\Local\Temp\lab1_trace\run\sandbox\) = STATUS_SUCCESS, h=0x1a4
NtQueryDirectoryFileEx(h=00000000000001a4;class=3;mask=a.txt) = STATUS_SUCCESS
NtOpenFile(root=0000000000000000;access=10000;share=4;opts=5040;name=C:\Users\sokol\AppData\Local\Temp\lab1_trace\run\sandbox\a.txt) = STATUS_SUCCESS, h=0x1a8
NtQueryDirectoryFileEx(h=00000000000001a4;class=3;mask=) = STATUS_NO_MORE_FILES
NtOpenFile(root=0000000000000000;access=100001;share=7;opts=4021;name=C:\Users\sokol\AppData\Local\Temp\lab1_trace\run\sandbox\) = STATUS_SUCCESS, h=0x1a8
NtQueryDirectoryFileEx(h=00000000000001a8;class=3;mask=c.txt) = STATUS_SUCCESS
NtOpenFile(root=0000000000000000;access=10000;share=4;opts=5040;name=C:\Users\sokol\AppData\Local\Temp\lab1_trace\run\sandbox\c.txt) = STATUS_SUCCESS, h=0x1ac
NtQueryDirectoryFileEx(h=00000000000001a8;class=3;mask=) = STATUS_NO_MORE_FILES
NtCreateFile(root=0000000000000000;access=80100080;disp=1;opts=60;name=C:\Users\sokol\AppData\Local\Temp\lab1_trace\run\scenario.cmd) = STATUS_SUCCESS, h=0x1a8
NtReadFile(h=00000000000001a8;len=8191) = STATUS_SUCCESS
NtQueryAttributesFile(root=0000000000000000;name=C:\Users\sokol\AppData\Local\Temp\lab1_trace\run) = STATUS_SUCCESS
NtOpenFile(root=0000000000000000;access=100001;share=7;opts=4021;name=C:\) = STATUS_SUCCESS, h=0x1ac
NtQueryDirectoryFileEx(h=00000000000001ac;class=3;mask=Users) = STATUS_SUCCESS
NtOpenFile(root=0000000000000000;access=100001;share=7;opts=4021;name=C:\Users\) = STATUS_SUCCESS, h=0x1a4
NtQueryDirectoryFileEx(h=00000000000001a4;class=3;mask=sokol) = STATUS_SUCCESS
NtOpenFile(root=0000000000000000;access=100001;share=7;opts=4021;name=C:\Users\sokol\) = STATUS_SUCCESS, h=0x1ac
NtQueryDirectoryFileEx(h=00000000000001ac;class=3;mask=AppData) = STATUS_SUCCESS
NtOpenFile(root=0000000000000000;access=100001;share=7;opts=4021;name=C:\Users\sokol\AppData\) = STATUS_SUCCESS, h=0x188
NtQueryDirectoryFileEx(h=0000000000000188;class=3;mask=Local) = STATUS_SUCCESS
NtOpenFile(root=0000000000000000;access=100001;share=7;opts=4021;name=C:\Users\sokol\AppData\Local\) = STATUS_SUCCESS, h=0x1a8
NtQueryDirectoryFileEx(h=00000000000001a8;class=3;mask=Temp) = STATUS_SUCCESS
NtOpenFile(root=0000000000000000;access=100001;share=7;opts=4021;name=C:\Users\sokol\AppData\Local\Temp\) = STATUS_SUCCESS, h=0x1ac
NtQueryDirectoryFileEx(h=00000000000001ac;class=3;mask=lab1_trace) = STATUS_SUCCESS
NtOpenFile(root=0000000000000000;access=100001;share=7;opts=4021;name=C:\Users\sokol\AppData\Local\Temp\lab1_trace\) = STATUS_SUCCESS, h=0x1a4
NtQueryDirectoryFileEx(h=00000000000001a4;class=3;mask=run) = STATUS_SUCCESS
NtQueryAttributesFile(root=0000000000000000;name=C:\Users\sokol\AppData\Local\Temp\lab1_trace\run) = STATUS_SUCCESS
NtOpenFile(root=0000000000000000;access=100020;share=3;opts=21;name=C:\Users\sokol\AppData\Local\Temp\lab1_trace\run) = STATUS_SUCCESS, h=0x1a8
NtCreateFile(root=0000000000000000;access=80100080;disp=1;opts=60;name=C:\Users\sokol\AppData\Local\Temp\lab1_trace\run\scenario.cmd) = STATUS_SUCCESS, h=0x1a4
NtReadFile(h=00000000000001a4;len=8191) = STATUS_SUCCESS
NtOpenFile(root=00000000000001a8;access=110080;share=7;opts=204021;name=sandbox) = STATUS_SUCCESS, h=0x1ac
NtSetInformationFile(h=00000000000001ac; FileDispositionInformationEx) = STATUS_SUCCESS
```

## [fin] exit /b 0 — завершение

Системных вызовов: 31

| Вызов | Кол-во |
|---|---:|
| NtSetInformationFile | 6 |
| NtDeviceIoControlFile | 6 |
| NtQuerySystemInformation | 6 |
| NtQueryInformationFile | 5 |
| NtQueryVolumeInformationFile | 3 |
| NtClose | 2 |
| NtCreateFile | 2 |
| NtReadFile | 1 |

Ключевые вызовы:

```
NtReadFile(h=0000000000000170;len=8191) = STATUS_SUCCESS
NtCreateFile(root=0000000000000000;access=80100080;disp=1;opts=60;name=C:\Users\sokol\AppData\Local\Temp\lab1_trace\run\scenario.cmd) = STATUS_SUCCESS, h=0x1a4
NtCreateFile(root=0000000000000000;access=80100080;disp=1;opts=60;name=C:\Users\sokol\AppData\Local\Temp\lab1_trace\run\scenario.cmd) = STATUS_SUCCESS, h=0x1a4
```
