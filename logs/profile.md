# Профиль системных вызовов cmd.exe

Всего перехвачено системных вызовов: **2180**, различных: **69** (из 489 заглушек в ntdll.dll), потоков: **1**, завершились ошибкой: **249**.

## Группы системных вызовов

| Группа | Вызовов | Доля | Различных | Функциональность cmd.exe |
|---|---:|---:|---:|---|
| Файловая система | 816 | 37.4% | 11 | поиск командного файла и программ по PATH, создание/запись/чтение файлов (> >> type copy), листинг каталога (dir), переименование (ren), удаление (del, rmdir), чтение самого scenario.cmd построчно |
| Виртуальная память и секции (отображение файлов) | 333 | 15.3% | 8 | куча процесса, загрузка DLL и NLS-таблиц (отображение секций), защита страниц |
| Объекты ядра и дескрипторы | 258 | 11.8% | 4 | закрытие дескрипторов файлов/ключей/процессов, работа с пространством имён объектов |
| Реестр | 189 | 8.7% | 7 | чтение настроек интерпретатора (HKLM/HKCU\Software\Microsoft\Command Processor: EnableExtensions, DelayedExpansion, AutoRun, DefaultColor …), языковых и системных параметров при загрузке DLL |
| Системная информация, локализация, ETW | 185 | 8.5% | 7 | версия/параметры ОС, таймеры, языки интерфейса и MUI-ресурсы (сообщения cmd на русском), WNF-уведомления, трассировка событий |
| Консоль и устройства (ввод-вывод через драйвер condrv) | 183 | 8.4% | 1 | вывод текста команд echo/type/dir в окно консоли, чтение режима консоли, кодовой страницы и цвета |
| Процессы и потоки | 109 | 5.0% | 11 | запуск внешней программы (hostname.exe), получение/изменение параметров собственного процесса, завершение cmd.exe |
| Безопасность и маркеры доступа | 56 | 2.6% | 9 | проверка прав пользователя/процесса (маркер доступа), атрибуты безопасности |
| Синхронизация и ожидание | 47 | 2.2% | 10 | ожидание завершения дочернего процесса, события/мьютексы/семафоры загрузчика DLL и служб локализации |
| Межпроцессное взаимодействие (ALPC) | 4 | 0.2% | 1 | обращение к системным службам (csrss, conhost, службы локализации) через порты ALPC |

### Файловая система

| Системный вызов | Номер | Вызовов | Ошибок |
|---|---:|---:|---:|
| NtSetInformationFile | 0x0027 | 228 | 0 |
| NtQueryInformationFile | 0x0011 | 170 | 2 |
| NtQueryVolumeInformationFile | 0x0049 | 128 | 0 |
| NtOpenFile | 0x0033 | 84 | 7 |
| NtCreateFile | 0x0055 | 64 | 2 |
| NtQueryDirectoryFileEx | 0x014E | 51 | 4 |
| NtReadFile | 0x0006 | 40 | 2 |
| NtQueryAttributesFile | 0x003D | 27 | 3 |
| NtFsControlFile | 0x0039 | 14 | 14 |
| NtWriteFile | 0x0008 | 9 | 0 |
| NtCopyFileChunk | 0x00A7 | 1 | 0 |

### Виртуальная память и секции (отображение файлов)

| Системный вызов | Номер | Вызовов | Ошибок |
|---|---:|---:|---:|
| NtProtectVirtualMemory | 0x0050 | 148 | 0 |
| NtQueryVirtualMemory | 0x0023 | 87 | 0 |
| NtAllocateVirtualMemory | 0x0018 | 64 | 0 |
| NtMapViewOfSection | 0x0028 | 13 | 0 |
| NtOpenSection | 0x0037 | 10 | 4 |
| NtCreateSection | 0x004A | 7 | 0 |
| NtFreeVirtualMemory | 0x001E | 2 | 0 |
| NtWriteVirtualMemory | 0x003A | 2 | 0 |

### Объекты ядра и дескрипторы

| Системный вызов | Номер | Вызовов | Ошибок |
|---|---:|---:|---:|
| NtClose | 0x000F | 248 | 0 |
| NtDuplicateObject | 0x003C | 7 | 0 |
| NtOpenSymbolicLinkObject | 0x0139 | 2 | 1 |
| NtQuerySymbolicLinkObject | 0x016C | 1 | 0 |

### Реестр

| Системный вызов | Номер | Вызовов | Ошибок |
|---|---:|---:|---:|
| NtOpenKey | 0x0012 | 89 | 56 |
| NtQueryValueKey | 0x0017 | 47 | 29 |
| NtQueryKey | 0x0016 | 27 | 0 |
| NtOpenKeyEx | 0x012C | 19 | 9 |
| NtEnumerateKey | 0x0032 | 3 | 0 |
| NtSetInformationKey | 0x01AB | 2 | 0 |
| NtNotifyChangeKey | 0x0124 | 2 | 0 |

### Системная информация, локализация, ETW

| Системный вызов | Номер | Вызовов | Ошибок |
|---|---:|---:|---:|
| NtQuerySystemInformation | 0x0036 | 116 | 1 |
| NtTraceControl | 0x01D7 | 41 | 0 |
| NtApphelpCacheControl | 0x004C | 11 | 0 |
| NtQueryPerformanceCounter | 0x0031 | 10 | 0 |
| NtQueryWnfStateData | 0x0171 | 3 | 0 |
| NtQueryLicenseValue | 0x0161 | 2 | 0 |
| NtGetMUIRegistryInfo | 0x00FF | 2 | 0 |

### Консоль и устройства (ввод-вывод через драйвер condrv)

| Системный вызов | Номер | Вызовов | Ошибок |
|---|---:|---:|---:|
| NtDeviceIoControlFile | 0x0007 | 183 | 101 |

### Процессы и потоки

| Системный вызов | Номер | Вызовов | Ошибок |
|---|---:|---:|---:|
| NtQueryInformationProcess | 0x0019 | 50 | 0 |
| NtSetInformationProcess | 0x001C | 49 | 0 |
| NtTerminateProcess | 0x002C | 2 | 0 |
| NtTestAlert | 0x01D4 | 1 | 0 |
| NtContinue | 0x0043 | 1 | 0 |
| NtOpenThread | 0x013A | 1 | 0 |
| NtQueryInformationThread | 0x0025 | 1 | 0 |
| NtRaiseException | 0x0175 | 1 | 0 |
| NtCreateUserProcess | 0x00D1 | 1 | 0 |
| NtResumeThread | 0x0052 | 1 | 0 |
| NtContinueEx | 0x00A5 | 1 | 0 |

### Безопасность и маркеры доступа

| Системный вызов | Номер | Вызовов | Ошибок |
|---|---:|---:|---:|
| NtQueryInformationToken | 0x0021 | 37 | 0 |
| NtOpenThreadToken | 0x0024 | 7 | 7 |
| NtOpenProcessToken | 0x0134 | 3 | 0 |
| NtDuplicateToken | 0x0042 | 2 | 0 |
| NtAccessCheck | 0x0000 | 2 | 0 |
| NtQuerySecurityAttributesToken | 0x0168 | 2 | 2 |
| NtOpenThreadTokenEx | 0x002F | 1 | 1 |
| NtOpenProcessTokenEx | 0x0030 | 1 | 0 |
| NtQuerySecurityObject | 0x0169 | 1 | 0 |

### Синхронизация и ожидание

| Системный вызов | Номер | Вызовов | Ошибок |
|---|---:|---:|---:|
| NtCreateEvent | 0x0048 | 11 | 0 |
| NtCreateSemaphore | 0x00C7 | 10 | 0 |
| NtSetEvent | 0x000E | 8 | 0 |
| NtWaitForSingleObject | 0x0004 | 5 | 0 |
| NtReleaseSemaphore | 0x000A | 4 | 2 |
| NtOpenSemaphore | 0x0137 | 3 | 1 |
| NtCreateMutant | 0x00BA | 2 | 0 |
| NtReleaseMutant | 0x0020 | 2 | 0 |
| NtSetInformationWorkerFactory | 0x01B2 | 1 | 0 |
| NtOpenEvent | 0x0040 | 1 | 1 |

### Межпроцессное взаимодействие (ALPC)

| Системный вызов | Номер | Вызовов | Ошибок |
|---|---:|---:|---:|
| NtAlpcSendWaitReceivePort | 0x008E | 4 | 0 |

## Коды ошибок

| Вызов | NTSTATUS | Количество |
|---|---|---:|
| NtDeviceIoControlFile | STATUS_INVALID_HANDLE | 92 |
| NtOpenKey | STATUS_OBJECT_NAME_NOT_FOUND | 56 |
| NtQueryValueKey | STATUS_OBJECT_NAME_NOT_FOUND | 29 |
| NtFsControlFile | STATUS_NOT_A_REPARSE_POINT | 14 |
| NtOpenKeyEx | STATUS_OBJECT_NAME_NOT_FOUND | 9 |
| NtDeviceIoControlFile | STATUS_INVALID_PARAMETER | 8 |
| NtOpenThreadToken | STATUS_NO_TOKEN | 7 |
| NtOpenFile | STATUS_FILE_IS_A_DIRECTORY | 7 |
| NtOpenSection | STATUS_OBJECT_NAME_NOT_FOUND | 4 |
| NtQueryDirectoryFileEx | STATUS_NO_SUCH_FILE | 4 |
| NtReleaseSemaphore | STATUS_SEMAPHORE_LIMIT_EXCEEDED | 2 |
| NtQueryAttributesFile | STATUS_OBJECT_NAME_NOT_FOUND | 2 |
| NtQueryInformationFile | STATUS_INVALID_PARAMETER | 2 |
| NtReadFile | STATUS_END_OF_FILE | 2 |
| NtQuerySecurityAttributesToken | STATUS_NOT_FOUND | 2 |
| NtOpenEvent | STATUS_OBJECT_NAME_NOT_FOUND | 1 |
| NtQuerySystemInformation | STATUS_INFO_LENGTH_MISMATCH | 1 |
| NtOpenSemaphore | STATUS_OBJECT_NAME_NOT_FOUND | 1 |
| NtCreateFile | STATUS_OBJECT_NAME_NOT_FOUND | 1 |
| NtOpenThreadTokenEx | STATUS_NO_TOKEN | 1 |
| NtOpenSymbolicLinkObject | STATUS_OBJECT_TYPE_MISMATCH | 1 |
| NtCreateFile | STATUS_NOT_A_DIRECTORY | 1 |
| NtDeviceIoControlFile | 0xC0070006 | 1 |
| NtQueryAttributesFile | STATUS_OBJECT_NAME_INVALID | 1 |

## Примеры аргументов

**Открываемые файлы (NtCreateFile/NtOpenFile)**

- `C:\WINDOWS\System32\Wldp.dll` → STATUS_SUCCESS
- `C:\Program Files\WindowsApps\Microsoft.LanguageExperiencePackru-RU_26100.173.281.0_neutral__8wekyb3d8bbwe\Windows\SYSTEM32\ru-RU\7a3ed5582884d5a8ddb01b818196742f\ntdll.dll.mui` → STATUS_SUCCESS
- `C:\` → STATUS_SUCCESS
- `C:\Users\` → STATUS_SUCCESS
- `C:\Users\sokol\` → STATUS_SUCCESS
- `C:\Users\sokol\AppData\` → STATUS_SUCCESS
- `C:\Users\sokol\AppData\Local\` → STATUS_SUCCESS
- `%TEMP%\` → STATUS_SUCCESS
- `%TEMP%\lab1_trace\` → STATUS_SUCCESS
- `%TEMP%\lab1_trace\run\` → STATUS_SUCCESS
- `C:\WINDOWS\SYSTEM32\cmdext.dll` → STATUS_SUCCESS
- `C:\WINDOWS\System32\AppLocker\MDM` → STATUS_OBJECT_NAME_NOT_FOUND
- `%TEMP%\lab1_trace\run\scenario.cmd` → STATUS_SUCCESS
- `%TEMP%\lab1_trace\run\scenario.cmd\` → STATUS_NOT_A_DIRECTORY
- `%TEMP%\lab1_trace\run` → STATUS_FILE_IS_A_DIRECTORY
- `%TEMP%\lab1_trace` → STATUS_FILE_IS_A_DIRECTORY
- `%TEMP%` → STATUS_FILE_IS_A_DIRECTORY
- `C:\Users\sokol\AppData\Local` → STATUS_FILE_IS_A_DIRECTORY
- `C:\Users\sokol\AppData` → STATUS_FILE_IS_A_DIRECTORY
- `C:\Users\sokol` → STATUS_FILE_IS_A_DIRECTORY
- `C:\Users` → STATUS_FILE_IS_A_DIRECTORY
- `C:` → STATUS_SUCCESS
- `MountPointManager` → STATUS_SUCCESS
- `sandbox` → STATUS_SUCCESS
- `%TEMP%\lab1_trace\run\sandbox` → STATUS_SUCCESS
- `a.txt` → STATUS_SUCCESS
- `%TEMP%\lab1_trace\run\sandbox\` → STATUS_SUCCESS
- `nul` → STATUS_SUCCESS
- `%TEMP%\lab1_trace\run\sandbox\a.txt` → STATUS_SUCCESS
- `%TEMP%\lab1_trace\run\sandbox\b.txt` → STATUS_SUCCESS
- `C:\WINDOWS\SYSTEM32\ntmarta.dll` → STATUS_SUCCESS
- `b.txt` → STATUS_SUCCESS
- `C:\Program Files\WindowsApps\Microsoft.LanguageExperiencePackru-RU_26100.173.281.0_neutral__8wekyb3d8bbwe\Windows\System32\ru-RU\d16a9991ff1a65d4c8a53640d31325fd\cmd.exe.mui` → STATUS_SUCCESS
- `C:\Program Files\WindowsApps\Microsoft.WinDbg_1.2611.4001.0_x64__8wekyb3d8bbwe\amd64\` → STATUS_SUCCESS
- `C:\WINDOWS\system32\` → STATUS_SUCCESS
- `C:\WINDOWS\Globalization\Sorting\sortdefault.nls` → STATUS_SUCCESS
- `%TEMP%\lab1_trace\run\sandbox\c.txt` → STATUS_SUCCESS
- `C:\WINDOWS\SYSTEM32\kernel.appcore.dll` → STATUS_SUCCESS

**Ключи реестра (NtOpenKey/NtOpenKeyEx)**

- `\Registry\Machine\System\CurrentControlSet\Control\Nls\Sorting\Versions` → STATUS_SUCCESS
- `\Registry\MACHINE\System\CurrentControlSet\Control\Session Manager` → STATUS_SUCCESS
- `\REGISTRY\USER\S-1-5-21-3471489291-2559018507-3582910447-1001` → STATUS_SUCCESS
- `Control Panel\Desktop\MuiCached\MachineLanguageConfiguration` → STATUS_OBJECT_NAME_NOT_FOUND
- `\Registry\Machine\Software\Policies\Microsoft\MUI\Settings` → STATUS_OBJECT_NAME_NOT_FOUND
- `Software\Policies\Microsoft\Control Panel\Desktop` → STATUS_OBJECT_NAME_NOT_FOUND
- `Control Panel\Desktop\LanguageConfiguration` → STATUS_OBJECT_NAME_NOT_FOUND
- `Control Panel\Desktop` → STATUS_SUCCESS
- `Control Panel\Desktop\MuiCached` → STATUS_SUCCESS
- `Software\Policies\Microsoft\Windows\System` → STATUS_OBJECT_NAME_NOT_FOUND
- `\Registry\Machine\SOFTWARE\Microsoft\AppModel\Lookaside\machine` → STATUS_SUCCESS
- `\Registry\Machine\SOFTWARE\Microsoft\AppModel\Lookaside\user` → STATUS_OBJECT_NAME_NOT_FOUND
- `\REGISTRY\MACHINE` → STATUS_SUCCESS
- `Software\Microsoft\Command Processor` → STATUS_SUCCESS
- `KnownPackageManagers` → STATUS_SUCCESS
- `System\Software\Microsoft\Command Processor` → STATUS_OBJECT_NAME_NOT_FOUND
- `\Registry\Machine\SOFTWARE\Microsoft\AppModel\Lookaside\machine\System\Software\Microsoft\Command Processor` → STATUS_OBJECT_NAME_NOT_FOUND
- `SOFTWARE\Microsoft\OLE` → STATUS_SUCCESS
- `Software\Microsoft\Ole\FeatureDevelopmentProperties` → STATUS_OBJECT_NAME_NOT_FOUND
- `\Registry\Machine\SOFTWARE\Microsoft\AppModel\Lookaside\machine\Software\Microsoft\Ole\FeatureDevelopmentProperties` → STATUS_OBJECT_NAME_NOT_FOUND
- `Software\Microsoft\Ole` → STATUS_SUCCESS
- `Software\Classes\Local Settings` → STATUS_SUCCESS
- `Software\Microsoft` → STATUS_SUCCESS
- `Software\Microsoft\OLE\Tracing` → STATUS_OBJECT_NAME_NOT_FOUND
- `\Registry\Machine\SOFTWARE\Microsoft\AppModel\Lookaside\machine\Software\Microsoft\OLE\Tracing` → STATUS_OBJECT_NAME_NOT_FOUND
- `\Registry\Machine\Software\Microsoft\LanguageOverlay\OverlayPackages\ru-RU` → STATUS_SUCCESS
- `\Registry\Machine\System\CurrentControlSet\Control\Nls\CustomLocale` → STATUS_SUCCESS
- `\Registry\Machine\System\CurrentControlSet\Control\Nls\ExtendedLocale` → STATUS_SUCCESS
- `\Registry\Machine\Software\Policies\Microsoft\Windows\Safer\LevelObjects` → STATUS_OBJECT_NAME_NOT_FOUND
- `\Registry\Machine\Software\Policies\Microsoft\Windows\Safer\CodeIdentifiers` → STATUS_SUCCESS
- `\Registry\Machine\Software\Policies\Microsoft\Windows\Safer\CodeIdentifiers\0\Paths` → STATUS_OBJECT_NAME_NOT_FOUND
- `\Registry\Machine\Software\Policies\Microsoft\Windows\Safer\CodeIdentifiers\0\Hashes` → STATUS_OBJECT_NAME_NOT_FOUND
- `\Registry\Machine\Software\Policies\Microsoft\Windows\Safer\CodeIdentifiers\0\UrlZones` → STATUS_OBJECT_NAME_NOT_FOUND
- `\Registry\Machine\Software\Policies\Microsoft\Windows\Safer\CodeIdentifiers\4096\Paths` → STATUS_OBJECT_NAME_NOT_FOUND
- `\Registry\Machine\Software\Policies\Microsoft\Windows\Safer\CodeIdentifiers\4096\Hashes` → STATUS_OBJECT_NAME_NOT_FOUND
- `\Registry\Machine\Software\Policies\Microsoft\Windows\Safer\CodeIdentifiers\4096\UrlZones` → STATUS_OBJECT_NAME_NOT_FOUND
- `\Registry\Machine\Software\Policies\Microsoft\Windows\Safer\CodeIdentifiers\65536\Paths` → STATUS_OBJECT_NAME_NOT_FOUND
- `\Registry\Machine\Software\Policies\Microsoft\Windows\Safer\CodeIdentifiers\65536\Hashes` → STATUS_OBJECT_NAME_NOT_FOUND
- `\Registry\Machine\Software\Policies\Microsoft\Windows\Safer\CodeIdentifiers\65536\UrlZones` → STATUS_OBJECT_NAME_NOT_FOUND
- `\Registry\Machine\Software\Policies\Microsoft\Windows\Safer\CodeIdentifiers\131072\Paths` → STATUS_OBJECT_NAME_NOT_FOUND

**Значения реестра (NtQueryValueKey)**

- `000605xx` → STATUS_SUCCESS
- `SmtDelaySleepLoopWindowSize` → STATUS_OBJECT_NAME_NOT_FOUND
- `SmtDelaySpinCountThreshold` → STATUS_OBJECT_NAME_NOT_FOUND
- `SmtDelayBaseYield` → STATUS_OBJECT_NAME_NOT_FOUND
- `SmtFactorYield` → STATUS_OBJECT_NAME_NOT_FOUND
- `SmtDelayMaxYield` → STATUS_OBJECT_NAME_NOT_FOUND
- `PreferredUILanguages` → STATUS_OBJECT_NAME_NOT_FOUND
- `MachinePreferredUILanguages` → STATUS_BUFFER_OVERFLOW
- `DisableUNCCheck` → STATUS_OBJECT_NAME_NOT_FOUND
- `EnableExtensions` → STATUS_SUCCESS
- `DelayedExpansion` → STATUS_OBJECT_NAME_NOT_FOUND
- `DefaultColor` → STATUS_SUCCESS
- `CompletionChar` → STATUS_SUCCESS
- `PathCompletionChar` → STATUS_SUCCESS
- `InteractiveExtensionLevel` → STATUS_SUCCESS
- `LockBatchFilesWhenInUse` → STATUS_SUCCESS
- `AutoRun` → STATUS_OBJECT_NAME_NOT_FOUND
- `SafeDllSearchMode` → STATUS_OBJECT_NAME_NOT_FOUND
- `PageAllocatorUseSystemHeap` → STATUS_OBJECT_NAME_NOT_FOUND
- `PageAllocatorSystemHeapIsPrivate` → STATUS_OBJECT_NAME_NOT_FOUND
- `AggressiveMTATesting` → STATUS_OBJECT_NAME_NOT_FOUND
- `Type` → STATUS_SUCCESS
- `Latest` → STATUS_SUCCESS
- `ru-RU` → STATUS_OBJECT_NAME_NOT_FOUND
- `Levels` → STATUS_OBJECT_NAME_NOT_FOUND
- `DefaultLevel` → STATUS_OBJECT_NAME_NOT_FOUND
- `SaferFlags` → STATUS_OBJECT_NAME_NOT_FOUND
- `RuleCount` → STATUS_OBJECT_NAME_NOT_FOUND
- `LogFileName` → STATUS_OBJECT_NAME_NOT_FOUND
- `CopyFileBufferedSynchronousIo` → STATUS_OBJECT_NAME_NOT_FOUND
- `CopyFileChunkSize` → STATUS_OBJECT_NAME_NOT_FOUND
- `CopyFileOverlappedCount` → STATUS_OBJECT_NAME_NOT_FOUND
- `ru` → STATUS_SUCCESS
- `HotPatchRestrictions` → STATUS_OBJECT_NAME_NOT_FOUND
- `TransparentEnabled` → STATUS_OBJECT_NAME_NOT_FOUND
- `AuthenticodeEnabled` → STATUS_SUCCESS
- `Cache` → STATUS_SUCCESS
- `C:\WINDOWS\system32\HOSTNAME.EXE` → STATUS_OBJECT_NAME_NOT_FOUND
- `PreferExternalManifest` → STATUS_OBJECT_NAME_NOT_FOUND

**Запуск процессов (NtCreateUserProcess)**

- `hostname` → STATUS_SUCCESS
