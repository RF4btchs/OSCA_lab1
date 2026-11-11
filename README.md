# ЛР 1. Профиль системных вызовов cmd.exe

Отчёт: `Отчет_ЛР1_Соколов_М80-202БВ-25.docx`

- `scenario/scenario.cmd` — тестовый сценарий для cmd.exe
- `scripts/run_trace.ps1` — трасса всех системных вызовов отладчиком cdb (нужен WinDbg: `winget install Microsoft.WinDbg`)
- `scripts/snapshot_handles.ps1` — дескрипторы живого cmd.exe (Handle.exe + `cdb -pv`)
- `scripts/run_procmon.ps1` — запись Process Monitor (попросит права администратора)
- `scripts/demo_cdb.cmd` — показ ключевых вызовов в момент выполнения (для защиты)
- `logs/` — результаты: `trace.tsv`, `profile.md`, `steps.md`, `handle_cmd.txt`, `procmon_profile.md`
- `tools/` — Sysinternals Handle, Process Monitor, Process Explorer (в репозиторий не входят, скачать с https://learn.microsoft.com/sysinternals и распаковать в `tools/Handle`, `tools/ProcessMonitor`, `tools/ProcessExplorer`) (в репозиторий не входят, скачать с https://learn.microsoft.com/sysinternals и распаковать в `tools/Handle`, `tools/ProcessMonitor`, `tools/ProcessExplorer`)
