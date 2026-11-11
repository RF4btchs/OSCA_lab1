# Профиль cmd.exe по данным Process Monitor

Событий: **1774**

## Процессы

| Процесс | Событий |
|---|---:|
| cmd.exe (PID 29596) | 1164 |
| HOSTNAME.EXE (PID 28060) | 610 |

## Классы операций

| Класс | Событий |
|---|---:|
| Файловая система | 993 |
| Реестр | 723 |
| Процессы и потоки | 58 |

## Операции

| Класс | Операция | Событий |
|---|---|---:|
| Реестр | RegOpenKey | 270 |
| Реестр | RegQueryValue | 237 |
| Файловая система | CreateFile | 201 |
| Файловая система | CloseFile | 190 |
| Файловая система | IRP_MJ_CLOSE | 185 |
| Реестр | RegCloseKey | 127 |
| Реестр | RegQueryKey | 72 |
| Файловая система | QueryDirectory | 49 |
| Файловая система | ReadFile | 48 |
| Файловая система | WriteFile | 44 |
| Файловая система | QueryBasicInformationFile | 39 |
| Файловая система | QueryOpen | 36 |
| Процессы и потоки | Load Image | 35 |
| Файловая система | CreateFileMapping | 34 |
| Файловая система | FASTIO_RELEASE_FOR_SECTION_SYNCHRONIZATION | 34 |
| Файловая система | FASTIO_ACQUIRE_FOR_CC_FLUSH | 24 |
| Файловая система | FASTIO_RELEASE_FOR_CC_FLUSH | 24 |
| Файловая система | DeviceIoControl | 16 |
| Файловая система | FileSystemControl | 14 |
| Файловая система | QueryStandardInformationFile | 12 |
| Файловая система | QueryNameInformationFile | 12 |
| Процессы и потоки | Thread Create | 8 |
| Реестр | RegCreateKey | 8 |
| Процессы и потоки | Thread Exit | 8 |
| Файловая система | QueryStatInformation | 6 |
| Файловая система | QueryAttributeInformationVolume | 5 |
| Файловая система | QueryEAFile | 4 |
| Реестр | RegEnumValue | 4 |
| Реестр | RegEnumKey | 3 |
| Файловая система | QueryAttributeTagFile | 3 |
| Файловая система | QuerySecurityFile | 3 |
| Процессы и потоки | Process Start | 2 |
| Файловая система | QueryRemoteProtocolInformation | 2 |
| Файловая система | SetBasicInformationFile | 2 |
| Процессы и потоки | Process Profiling | 2 |
| Процессы и потоки | Process Exit | 2 |
| Реестр | RegSetInfoKey | 1 |
| Файловая система | QueryInformationVolume | 1 |
| Файловая система | QueryStreamInformationFile | 1 |
| Файловая система | QueryEaInformationFile | 1 |
| Файловая система | SetEndOfFileInformationFile | 1 |
| Файловая система | SetRenameInformationFile | 1 |
| Процессы и потоки | Process Create | 1 |
| Файловая система | SetDispositionInformationEx | 1 |
| Реестр | RegSetValue | 1 |

## Результаты

| Result | Событий |
|---|---:|
| SUCCESS | 1402 |
| NAME NOT FOUND | 177 |
| FAST IO DISALLOWED | 52 |
| REPARSE | 49 |
| BUFFER OVERFLOW | 28 |
| FILE LOCKED WITH ONLY READERS | 17 |
| NOT REPARSE POINT | 14 |
| INVALID PARAMETER | 10 |
| NO MORE FILES | 8 |
| IS DIRECTORY | 7 |
| BUFFER TOO SMALL | 3 |
| NO SUCH FILE | 2 |
| END OF FILE | 2 |
| NO MORE ENTRIES | 1 |
| NOT A DIRECTORY | 1 |
| NAME INVALID | 1 |

## Ключевые события сценария

```
19:22:33,9958331  cmd.exe:29596  Process Start                  SUCCESS
19:22:34,0439979  cmd.exe:29596  WriteFile                    C:\Users\sokol\AppData\Local\Temp\lab1_procmon\scenario_out.txt  SUCCESS
19:22:34,0440460  cmd.exe:29596  WriteFile                    C:\$LogFile  SUCCESS
19:22:34,0441741  cmd.exe:29596  WriteFile                    C:\$LogFile  SUCCESS
19:22:34,0442884  cmd.exe:29596  WriteFile                    C:\Users\sokol\AppData\Local\Temp\lab1_procmon\scenario_out.txt  SUCCESS
19:22:34,0454959  cmd.exe:29596  WriteFile                    C:\$Mft  SUCCESS
19:22:34,0469333  cmd.exe:29596  CreateFile                   C:\Users\sokol\AppData\Local\Temp\lab1_procmon\run\sandbox  SUCCESS
19:22:34,0483656  cmd.exe:29596  CreateFile                   C:\Users\sokol\AppData\Local\Temp\lab1_procmon\run\sandbox  SUCCESS
19:22:34,0511476  cmd.exe:29596  CreateFile                   C:\Users\sokol\AppData\Local\Temp\lab1_procmon\run\sandbox  SUCCESS
19:22:34,0513563  cmd.exe:29596  CreateFile                   C:\Users\sokol\AppData\Local\Temp\lab1_procmon\run\sandbox  SUCCESS
19:22:34,0528712  cmd.exe:29596  CreateFile                   C:\Users\sokol\AppData\Local\Temp\lab1_procmon\run\sandbox\a.txt  SUCCESS
19:22:34,0533090  cmd.exe:29596  WriteFile                    C:\Users\sokol\AppData\Local\Temp\lab1_procmon\run\sandbox\a.txt  SUCCESS
19:22:34,0539496  cmd.exe:29596  CreateFile                   C:\Users\sokol\AppData\Local\Temp\lab1_procmon\run\sandbox\a.txt  SUCCESS
19:22:34,0554416  cmd.exe:29596  WriteFile                    C:\Users\sokol\AppData\Local\Temp\lab1_procmon\run\sandbox\a.txt  FAST IO DISALLOWED
19:22:34,0554596  cmd.exe:29596  WriteFile                    C:\Users\sokol\AppData\Local\Temp\lab1_procmon\run\sandbox\a.txt  SUCCESS
19:22:34,0566404  cmd.exe:29596  CreateFile                   C:\Users\sokol\AppData\Local\Temp\lab1_procmon\run\sandbox  SUCCESS
19:22:34,0568962  cmd.exe:29596  CreateFile                   C:\Users\sokol\AppData\Local\Temp\lab1_procmon\run\sandbox\a.txt  SUCCESS
19:22:34,0570639  cmd.exe:29596  CreateFile                   C:\Users\sokol\AppData\Local\Temp\lab1_procmon\run\sandbox\a.txt  SUCCESS
19:22:34,0572076  cmd.exe:29596  WriteFile                    C:\Users\sokol\AppData\Local\Temp\lab1_procmon\scenario_out.txt  FAST IO DISALLOWED
19:22:34,0572284  cmd.exe:29596  WriteFile                    C:\Users\sokol\AppData\Local\Temp\lab1_procmon\scenario_out.txt  SUCCESS
19:22:34,0572532  cmd.exe:29596  WriteFile                    C:\$LogFile  SUCCESS
19:22:34,0573710  cmd.exe:29596  WriteFile                    C:\Users\sokol\AppData\Local\Temp\lab1_procmon\scenario_out.txt  SUCCESS
19:22:34,0582956  cmd.exe:29596  WriteFile                    C:\$Mft  SUCCESS
19:22:34,0596701  cmd.exe:29596  CreateFile                   C:\Users\sokol\AppData\Local\Temp\lab1_procmon\run\sandbox\a.txt  SUCCESS
19:22:34,0601461  cmd.exe:29596  CreateFile                   C:\Users\sokol\AppData\Local\Temp\lab1_procmon\run\sandbox  SUCCESS
19:22:34,0603736  cmd.exe:29596  CreateFile                   C:\Users\sokol\AppData\Local\Temp\lab1_procmon\run\sandbox\a.txt  SUCCESS
19:22:34,0606784  cmd.exe:29596  CreateFile                   C:\Users\sokol\AppData\Local\Temp\lab1_procmon\run\sandbox\b.txt  NAME NOT FOUND
19:22:34,0608537  cmd.exe:29596  CreateFile                   C:\Users\sokol\AppData\Local\Temp\lab1_procmon\run\sandbox\b.txt  NAME NOT FOUND
19:22:34,0610471  cmd.exe:29596  CreateFile                   C:\Users\sokol\AppData\Local\Temp\lab1_procmon\run\sandbox\a.txt  SUCCESS
19:22:34,0613428  cmd.exe:29596  CreateFile                   C:\Users\sokol\AppData\Local\Temp\lab1_procmon\run\sandbox\b.txt  SUCCESS
19:22:34,0641013  cmd.exe:29596  CreateFile                   C:\Users\sokol\AppData\Local\Temp\lab1_procmon\run\sandbox\b.txt  SUCCESS
19:22:34,0643368  cmd.exe:29596  CreateFile                   C:\Users\sokol\AppData\Local\Temp\lab1_procmon\run\sandbox\b.txt  SUCCESS
19:22:34,0661373  cmd.exe:29596  CreateFile                   C:\Users\sokol\AppData\Local\Temp\lab1_procmon\run\sandbox\b.txt  SUCCESS
19:22:34,0664759  cmd.exe:29596  CreateFile                   C:\Users\sokol\AppData\Local\Temp\lab1_procmon\run\sandbox\b.txt  SUCCESS
19:22:34,0667565  cmd.exe:29596  CreateFile                   C:\Users\sokol\AppData\Local\Temp\lab1_procmon\run\sandbox\b.txt  SUCCESS
19:22:34,0669590  cmd.exe:29596  CreateFile                   C:\Users\sokol\AppData\Local\Temp\lab1_procmon\run\sandbox  SUCCESS
19:22:34,0672652  cmd.exe:29596  CreateFile                   C:\Users\sokol\AppData\Local\Temp\lab1_procmon\run\sandbox\b.txt  SUCCESS
19:22:34,0676121  cmd.exe:29596  CreateFile                   C:\Users\sokol\AppData\Local\Temp\lab1_procmon\run\sandbox  SUCCESS
19:22:34,0677161  cmd.exe:29596  SetRenameInformationFile     C:\Users\sokol\AppData\Local\Temp\lab1_procmon\run\sandbox\b.txt  SUCCESS
19:22:34,0695093  cmd.exe:29596  CreateFile                   C:\Users\sokol\AppData\Local\Temp\lab1_procmon\run\sandbox  SUCCESS
19:22:34,0698358  cmd.exe:29596  CreateFile                   C:\Users\sokol\AppData\Local\Temp\lab1_procmon\run\sandbox  SUCCESS
19:22:34,0700692  cmd.exe:29596  CreateFile                   C:\Users\sokol\AppData\Local\Temp\lab1_procmon\run\sandbox\.  NAME INVALID
19:22:34,0703373  cmd.exe:29596  CreateFile                   C:\Users\sokol\AppData\Local\Temp\lab1_procmon\run\sandbox  SUCCESS
19:22:34,0705906  cmd.exe:29596  WriteFile                    C:\Users\sokol\AppData\Local\Temp\lab1_procmon\scenario_out.txt  FAST IO DISALLOWED
19:22:34,0706101  cmd.exe:29596  WriteFile                    C:\Users\sokol\AppData\Local\Temp\lab1_procmon\scenario_out.txt  SUCCESS
19:22:34,0706401  cmd.exe:29596  WriteFile                    C:\$LogFile  SUCCESS
19:22:34,0707634  cmd.exe:29596  WriteFile                    C:\Users\sokol\AppData\Local\Temp\lab1_procmon\scenario_out.txt  SUCCESS
19:22:34,0716971  cmd.exe:29596  WriteFile                    C:\$Mft  SUCCESS
19:22:34,0718138  cmd.exe:29596  WriteFile                    C:\Users\sokol\AppData\Local\Temp\lab1_procmon\scenario_out.txt  FAST IO DISALLOWED
19:22:34,0718432  cmd.exe:29596  WriteFile                    C:\Users\sokol\AppData\Local\Temp\lab1_procmon\scenario_out.txt  SUCCESS
19:22:34,0718666  cmd.exe:29596  WriteFile                    C:\$LogFile  SUCCESS
19:22:34,0719576  cmd.exe:29596  WriteFile                    C:\Users\sokol\AppData\Local\Temp\lab1_procmon\scenario_out.txt  SUCCESS
19:22:34,0728399  cmd.exe:29596  WriteFile                    C:\$Mft  SUCCESS
19:22:34,0729921  cmd.exe:29596  WriteFile                    C:\Users\sokol\AppData\Local\Temp\lab1_procmon\scenario_out.txt  FAST IO DISALLOWED
19:22:34,0730129  cmd.exe:29596  WriteFile                    C:\Users\sokol\AppData\Local\Temp\lab1_procmon\scenario_out.txt  SUCCESS
19:22:34,0730356  cmd.exe:29596  WriteFile                    C:\$LogFile  SUCCESS
19:22:34,0731377  cmd.exe:29596  WriteFile                    C:\Users\sokol\AppData\Local\Temp\lab1_procmon\scenario_out.txt  SUCCESS
19:22:34,0740024  cmd.exe:29596  WriteFile                    C:\$Mft  SUCCESS
19:22:34,0741188  cmd.exe:29596  WriteFile                    C:\Users\sokol\AppData\Local\Temp\lab1_procmon\scenario_out.txt  FAST IO DISALLOWED
19:22:34,0741375  cmd.exe:29596  WriteFile                    C:\Users\sokol\AppData\Local\Temp\lab1_procmon\scenario_out.txt  SUCCESS
19:22:34,0741574  cmd.exe:29596  WriteFile                    C:\$LogFile  SUCCESS
19:22:34,0742426  cmd.exe:29596  WriteFile                    C:\Users\sokol\AppData\Local\Temp\lab1_procmon\scenario_out.txt  SUCCESS
19:22:34,0751025  cmd.exe:29596  WriteFile                    C:\$Mft  SUCCESS
19:22:34,0765160  cmd.exe:29596  CreateFile                   C:\Users\sokol\AppData\Local\Temp\lab1_procmon\run\sandbox  SUCCESS
19:22:34,0771986  cmd.exe:29596  CreateFile                   C:\Users\sokol\AppData\Local\Temp\lab1_procmon\run\sandbox  SUCCESS
19:22:34,0783448  cmd.exe:29596  CreateFile                   C:\Users\sokol\AppData\Local\Temp\lab1_procmon\run\sandbox  SUCCESS
19:22:34,0878412  cmd.exe:29596  Process Create               C:\WINDOWS\system32\HOSTNAME.EXE  SUCCESS
19:22:34,0878514  HOSTNAME.EXE:28060  Process Start                  SUCCESS
19:22:34,1006398  HOSTNAME.EXE:28060  CreateFile                   C:\Users\sokol\AppData\Local\Temp\lab1_procmon\run\sandbox  SUCCESS
19:22:34,1289294  HOSTNAME.EXE:28060  WriteFile                    C:\Users\sokol\AppData\Local\Temp\lab1_procmon\scenario_out.txt  FAST IO DISALLOWED
19:22:34,1289487  HOSTNAME.EXE:28060  WriteFile                    C:\Users\sokol\AppData\Local\Temp\lab1_procmon\scenario_out.txt  SUCCESS
19:22:34,1289774  HOSTNAME.EXE:28060  WriteFile                    C:\$LogFile  SUCCESS
19:22:34,1291682  HOSTNAME.EXE:28060  WriteFile                    C:\Users\sokol\AppData\Local\Temp\lab1_procmon\scenario_out.txt  SUCCESS
19:22:34,1303918  HOSTNAME.EXE:28060  WriteFile                    C:\$Mft  SUCCESS
19:22:34,1306451  HOSTNAME.EXE:28060  WriteFile                    C:\Users\sokol\AppData\Local\Temp\lab1_procmon\scenario_out.txt  FAST IO DISALLOWED
19:22:34,1306769  HOSTNAME.EXE:28060  WriteFile                    C:\Users\sokol\AppData\Local\Temp\lab1_procmon\scenario_out.txt  SUCCESS
19:22:34,1307160  HOSTNAME.EXE:28060  WriteFile                    C:\$LogFile  SUCCESS
19:22:34,1308412  HOSTNAME.EXE:28060  WriteFile                    C:\Users\sokol\AppData\Local\Temp\lab1_procmon\scenario_out.txt  SUCCESS
19:22:34,1318657  HOSTNAME.EXE:28060  WriteFile                    C:\$Mft  SUCCESS
19:22:34,1389006  HOSTNAME.EXE:28060  Process Exit                   SUCCESS
19:22:34,1743751  cmd.exe:29596  CreateFile                   C:\Users\sokol\AppData\Local\Temp\lab1_procmon\run\sandbox\a.txt  SUCCESS
19:22:34,1766808  cmd.exe:29596  CreateFile                   C:\Users\sokol\AppData\Local\Temp\lab1_procmon\run\sandbox\a.txt  SUCCESS
19:22:34,1795096  cmd.exe:29596  CreateFile                   C:\Users\sokol\AppData\Local\Temp\lab1_procmon\run\sandbox\c.txt  SUCCESS
19:22:34,1812924  cmd.exe:29596  CreateFile                   C:\Users\sokol\AppData\Local\Temp\lab1_procmon\run\sandbox\c.txt  SUCCESS
19:22:34,1840054  cmd.exe:29596  CreateFile                   C:\Users\sokol\AppData\Local\Temp\lab1_procmon\run\sandbox  SUCCESS
19:22:34,1848469  cmd.exe:29596  CreateFile                   C:\Users\sokol\AppData\Local\Temp\lab1_procmon\run\sandbox\a.txt  SUCCESS
19:22:34,1870103  cmd.exe:29596  CreateFile                   C:\Users\sokol\AppData\Local\Temp\lab1_procmon\run\sandbox  SUCCESS
19:22:34,1873062  cmd.exe:29596  CreateFile                   C:\Users\sokol\AppData\Local\Temp\lab1_procmon\run\sandbox\c.txt  SUCCESS
19:22:34,1963145  cmd.exe:29596  CreateFile                   C:\Users\sokol\AppData\Local\Temp\lab1_procmon\run\sandbox  SUCCESS
19:22:34,1964025  cmd.exe:29596  SetDispositionInformationEx  C:\Users\sokol\AppData\Local\Temp\lab1_procmon\run\sandbox  SUCCESS
19:22:34,2014412  cmd.exe:29596  Process Exit                   SUCCESS
19:22:34,2135642  cmd.exe:29596  WriteFile                    C:\$LogFile  SUCCESS
```