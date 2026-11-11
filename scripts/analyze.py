"""
Построение профиля системных вызовов по логу cdb.

Вход:
    cdb_raw.log         — лог отладчика (UTF-16), строки SC|tid|ntdll!Имя (адрес)|аргументы
                          и RET|tid|NTSTATUS[|h=дескриптор]
    ntdll_syscalls.tsv  — имя системного вызова -> номер (из ntdll_syscalls.py)
Выход (в каталог logs):
    trace.tsv           — очищенная трасса: №, TID, вызов, номер, аргументы, NTSTATUS
    profile.md          — профиль: группы вызовов, количество, назначение в cmd.exe
    steps.md            — какие вызовы делает каждый блок сценария scenario.cmd
    profile.json        — те же данные для сборки отчёта

Привязка к строкам сценария: cmd.exe перед выполнением каждой строки .cmd-файла
заново открывает его (NtCreateFile), ставит позицию (NtSetInformationFile,
класс 14 = FilePositionInformation) и читает (NtReadFile). По смещению из
FilePositionInformation определяется строка сценария, к которой относятся
последующие вызовы.
"""
import collections
import json
import os
import re
import sys

# ----------------------------------------------------------------------------- группы
# (ключ, название группы, функциональность cmd.exe, регулярное выражение по имени вызова)
GROUPS = [
    ("proc", "Процессы и потоки",
     "запуск внешней программы (hostname.exe), получение/изменение параметров "
     "собственного процесса, завершение cmd.exe",
     r"^Nt(CreateUserProcess|TerminateProcess|(Query|Set)InformationProcess|OpenProcess$|"
     r"CreateThread|TerminateThread|(Query|Set)InformationThread|OpenThread$|ResumeThread|"
     r"SuspendThread|GetContextThread|SetContextThread|TestAlert|Continue|RaiseException|"
     r"FlushProcessWriteBuffers|GetNextThread|GetNextProcess)"),
    ("file", "Файловая система",
     "поиск командного файла и программ по PATH, создание/запись/чтение файлов "
     "(> >> type copy), листинг каталога (dir), переименование (ren), удаление (del, rmdir), "
     "чтение самого scenario.cmd построчно",
     r"^Nt(CreateFile|OpenFile|ReadFile|WriteFile|Query(Directory)?File|QueryDirectoryFileEx|"
     r"Query(Full)?AttributesFile|(Query|Set)InformationFile|QueryVolumeInformationFile|"
     r"SetVolumeInformationFile|DeleteFile|FlushBuffersFile|FsControlFile|(Query|Set)EaFile|"
     r"LockFile|UnlockFile|CancelIoFile|CopyFileChunk)"),
    ("console", "Консоль и устройства (ввод-вывод через драйвер condrv)",
     "вывод текста команд echo/type/dir в окно консоли, чтение режима консоли, "
     "кодовой страницы и цвета",
     r"^NtDeviceIoControlFile$"),
    ("reg", "Реестр",
     "чтение настроек интерпретатора (HKLM/HKCU\\Software\\Microsoft\\Command Processor: "
     "EnableExtensions, DelayedExpansion, AutoRun, DefaultColor …), языковых и системных "
     "параметров при загрузке DLL",
     r"^Nt(OpenKey|OpenKeyEx|CreateKey|QueryKey|QueryValueKey|EnumerateKey|EnumerateValueKey|"
     r"SetValueKey|DeleteKey|DeleteValueKey|NotifyChangeKey|NotifyChangeMultipleKeys|"
     r"SetInformationKey|QueryMultipleValueKey|FlushKey|OpenKeyTransacted)"),
    ("mem", "Виртуальная память и секции (отображение файлов)",
     "куча процесса, загрузка DLL и NLS-таблиц (отображение секций), защита страниц",
     r"^Nt(AllocateVirtualMemory|AllocateVirtualMemoryEx|FreeVirtualMemory|ProtectVirtualMemory|"
     r"QueryVirtualMemory|ReadVirtualMemory|WriteVirtualMemory|(Create|Open)Section|"
     r"MapViewOfSection|MapViewOfSectionEx|UnmapViewOfSection|UnmapViewOfSectionEx|"
     r"FlushInstructionCache|ExtendSection|QuerySection|LockVirtualMemory|UnlockVirtualMemory|"
     r"SetInformationVirtualMemory)"),
    ("sync", "Синхронизация и ожидание",
     "ожидание завершения дочернего процесса, события/мьютексы/семафоры загрузчика DLL и "
     "служб локализации",
     r"^Nt(WaitFor|Create(Event|Mutant|Semaphore|Timer|Timer2|KeyedEvent|IoCompletion|"
     r"WaitCompletionPacket)|Open(Event|Mutant|Semaphore|KeyedEvent)|Set(Event|Timer|Timer2)|"
     r"Reset(Event)|Clear(Event)|Release(Mutant|Semaphore|KeyedEvent|WorkerFactoryWorker)|"
     r"Pulse(Event)|DelayExecution|Yield(Execution)|AlertThreadByThreadId|SignalAndWait|"
     r"(Create|Set|Query)(Information)?WorkerFactory|Remove(IoCompletion)|"
     r"AssociateWaitCompletionPacket|CancelWaitCompletionPacket)"),
    ("sec", "Безопасность и маркеры доступа",
     "проверка прав пользователя/процесса (маркер доступа), атрибуты безопасности",
     r"^Nt(Open(Process|Thread)Token|Open(Process|Thread)TokenEx|QueryInformationToken|"
     r"SetInformationToken|AccessCheck|DuplicateToken|AdjustPrivilegesToken|PrivilegeCheck|"
     r"QuerySecurityObject|SetSecurityObject|QuerySecurityAttributesToken|FilterToken|"
     r"CompareTokens|ImpersonateThread)"),
    ("obj", "Объекты ядра и дескрипторы",
     "закрытие дескрипторов файлов/ключей/процессов, работа с пространством имён объектов",
     r"^Nt(Close|DuplicateObject|QueryObject|SetInformationObject|MakeTemporaryObject|"
     r"(Open|Create)DirectoryObject|QueryDirectoryObject|(Open|Create)SymbolicLinkObject|"
     r"QuerySymbolicLinkObject|CompareObjects|WaitForAlertByThreadId)"),
    ("sys", "Системная информация, локализация, ETW",
     "версия/параметры ОС, таймеры, языки интерфейса и MUI-ресурсы (сообщения cmd на русском), "
     "WNF-уведомления, трассировка событий",
     r"^Nt(Query(System|Performance|Timer|DefaultLocale|DefaultUILanguage|InstallUILanguage|"
     r"License|WnfStateData|SystemTime|SystemInformationEx|BootOptions|Wnf)|Get(MUIRegistryInfo|"
     r"NlsSectionPtr|CurrentProcessorNumber|CurrentProcessorNumberEx)|InitializeNlsFiles|"
     r"TraceControl|TraceEvent|ApphelpCacheControl|SubscribeWnfStateChange|UpdateWnfStateData|"
     r"SetSystemInformation|PowerInformation|QueryInformationByName|ManageHotPatch)"),
    ("ipc", "Межпроцессное взаимодействие (ALPC)",
     "обращение к системным службам (csrss, conhost, службы локализации) через порты ALPC",
     r"^Nt(Alpc|ConnectPort|SecureConnectPort|RequestWaitReplyPort|ReplyPort|"
     r"RequestPort|ListenPort|AcceptConnectPort|CompleteConnectPort)"),
]
OTHER = ("other", "Прочие", "прочие системные вызовы", r".")
_compiled = [(k, n, d, re.compile(r)) for k, n, d, r in GROUPS + [OTHER]]


def group_of(name):
    for key, _n, _d, rx in _compiled:
        if rx.search(name):
            return key
    return "other"


NTSTATUS = {
    0x00000000: "STATUS_SUCCESS",
    0x00000102: "STATUS_TIMEOUT",
    0x00000103: "STATUS_PENDING",
    0x00000104: "STATUS_REPARSE",
    0x40000000: "STATUS_OBJECT_NAME_EXISTS",
    0x80000005: "STATUS_BUFFER_OVERFLOW",
    0x80000006: "STATUS_NO_MORE_FILES",
    0x8000001A: "STATUS_NO_MORE_ENTRIES",
    0xC0000002: "STATUS_NOT_IMPLEMENTED",
    0xC0000004: "STATUS_INFO_LENGTH_MISMATCH",
    0xC0000008: "STATUS_INVALID_HANDLE",
    0xC000000D: "STATUS_INVALID_PARAMETER",
    0xC000000F: "STATUS_NO_SUCH_FILE",
    0xC0000022: "STATUS_ACCESS_DENIED",
    0xC0000023: "STATUS_BUFFER_TOO_SMALL",
    0xC0000033: "STATUS_OBJECT_NAME_INVALID",
    0xC0000034: "STATUS_OBJECT_NAME_NOT_FOUND",
    0xC0000035: "STATUS_OBJECT_NAME_COLLISION",
    0xC000003A: "STATUS_OBJECT_PATH_NOT_FOUND",
    0xC0000056: "STATUS_DELETE_PENDING",
    0xC0000061: "STATUS_PRIVILEGE_NOT_HELD",
    0xC00000BA: "STATUS_FILE_IS_A_DIRECTORY",
    0xC00000BB: "STATUS_NOT_SUPPORTED",
    0xC0000101: "STATUS_DIRECTORY_NOT_EMPTY",
    0xC0000103: "STATUS_NOT_A_DIRECTORY",
    0xC0000135: "STATUS_DLL_NOT_FOUND",
    0xC0000225: "STATUS_NOT_FOUND",
    0xC0000011: "STATUS_END_OF_FILE",
    0xC0000024: "STATUS_OBJECT_TYPE_MISMATCH",
    0xC0000047: "STATUS_SEMAPHORE_LIMIT_EXCEEDED",
    0xC000007C: "STATUS_NO_TOKEN",
    0xC0000275: "STATUS_NOT_A_REPARSE_POINT",
}

FILE_INFO_CLASS = {4: "FileBasicInformation", 5: "FileStandardInformation",
                   10: "FileRenameInformation", 13: "FileDispositionInformation",
                   14: "FilePositionInformation", 19: "FileAllocationInformation",
                   20: "FileEndOfFileInformation", 64: "FileDispositionInformationEx",
                   65: "FileRenameInformationEx", 18: "FileAllInformation",
                   34: "FileNetworkOpenInformation", 35: "FileAttributeTagInformation",
                   48: "FileIdInformation", 68: "FileStatInformation"}


def status_text(st):
    return NTSTATUS.get(st, f"0x{st:08X}")


def is_error(st):
    return st is not None and (st >> 30) == 3          # severity = error


# ----------------------------------------------------------------------------- разбор лога
SC_RX = re.compile(r"^SC\|([0-9a-f]+)\|ntdll!(\w+)(?: \([^)]*\))?\|(.*)$")
RET_RX = re.compile(r"^RET\|([0-9a-f]+)\|([0-9a-f]+)(?:\|h=([0-9a-f]+))?$")


def parse_log(path):
    with open(path, "rb") as f:
        raw = f.read()
    text = raw.decode("utf-16") if raw[:2] in (b"\xff\xfe", b"\xfe\xff") else raw.decode("cp1251")
    calls, pending = [], {}            # pending: tid -> индекс последнего вызова без RET
    for line in text.splitlines():
        line = line.rstrip()
        m = SC_RX.match(line)
        if m:
            tid, name, args = m.groups()
            if name.startswith("Zw"):
                name = "Nt" + name[2:]
            calls.append({"tid": int(tid, 16), "name": name, "args": args.strip(),
                          "status": None, "handle": None})
            pending[tid] = len(calls) - 1
            continue
        m = RET_RX.match(line)
        if m:
            tid, st, h = m.groups()
            idx = pending.pop(tid, None)
            if idx is not None:
                calls[idx]["status"] = int(st, 16) & 0xFFFFFFFF
                if h is not None:
                    calls[idx]["handle"] = int(h, 16)
    return calls


def parse_args(s):
    out = {}
    for part in s.split(";"):
        if "=" in part:
            k, v = part.split("=", 1)
            out[k] = v
    return out


# ----------------------------------------------------------------------------- сценарий
def load_scenario(path):
    """Возвращает список (смещение_начала_строки, текст_строки, номер_блока)."""
    with open(path, "rb") as f:
        data = f.read()
    lines, off, block = [], 0, 0
    for raw_line in data.split(b"\n"):
        text = raw_line.rstrip(b"\r").decode("cp866", "replace")
        m = re.match(r"\s*rem \[(\d+)\]", text, re.I)
        if m:
            block = int(m.group(1))
        lines.append((off, text, block))
        off += len(raw_line) + 1
    return lines


def line_at(lines, offset):
    cur = lines[0]
    for item in lines:
        if item[0] <= offset:
            cur = item
        else:
            break
    return cur


def assign_steps(calls, scenario_lines, scenario_name="scenario.cmd"):
    """Для каждого вызова определяет строку сценария, во время выполнения которой он сделан."""
    script_handles = set()
    last_pos = {}
    current = None                       # (offset, text, block)
    for c in calls:
        a = parse_args(c["args"])
        if c["name"] in ("NtCreateFile", "NtOpenFile") and \
                a.get("name", "").lower().endswith(scenario_name) and c["handle"]:
            script_handles.add(c["handle"])
        h = int(a["h"], 16) if "h" in a else None
        if c["name"] == "NtSetInformationFile" and h in script_handles and a.get("class") == "14":
            last_pos[h] = int(a.get("info", "0"), 16)
        if c["name"] == "NtReadFile" and h in script_handles:
            current = line_at(scenario_lines, last_pos.get(h, 0))
        if c["name"] == "NtClose" and h in script_handles:
            script_handles.discard(h)
        c["step"] = current
    return calls


# ----------------------------------------------------------------------------- вывод
def md_escape(s):
    return s.replace("|", "\\|")


def short_path(p):
    p = p.replace("\\??\\", "")
    tmp = os.environ.get("TEMP", "")
    if tmp and p.lower().startswith(tmp.lower()):
        p = "%TEMP%" + p[len(tmp):]
    return p


def main():
    if len(sys.argv) != 4:
        print("использование: analyze.py cdb_raw.log ntdll_syscalls.tsv каталог_вывода", file=sys.stderr)
        return 2
    log_path, tsv_path, out_dir = sys.argv[1:]
    here = os.path.dirname(os.path.abspath(__file__))
    scen_path = os.path.join(here, "..", "scenario", "scenario.cmd")
    try:
        numbers = {}
        with open(tsv_path, encoding="utf-8-sig") as f:
            for line in f:
                if "\t" in line:
                    n, num = line.strip().split("\t")
                    numbers[n] = int(num, 16)
        calls = parse_log(log_path)
        scenario = load_scenario(scen_path)
    except OSError as e:
        print(f"ошибка чтения входных файлов: {e}", file=sys.stderr)
        return 1
    if not calls:
        print("ошибка: в логе нет записей SC|… — трассировка не удалась", file=sys.stderr)
        return 1

    assign_steps(calls, scenario)
    for c in calls:
        c["group"] = group_of(c["name"])
        c["num"] = numbers.get(c["name"])

    os.makedirs(out_dir, exist_ok=True)

    # --- trace.tsv
    with open(os.path.join(out_dir, "trace.tsv"), "w", encoding="utf-8") as f:
        f.write("seq\ttid\tsyscall\tnumber\tgroup\tstep\targs\tstatus\thandle\n")
        for i, c in enumerate(calls, 1):
            step = c["step"][1].strip() if c["step"] else "(инициализация)"
            f.write(f"{i}\t{c['tid']}\t{c['name']}\t"
                    f"{'' if c['num'] is None else hex(c['num'])}\t{c['group']}\t{step}\t"
                    f"{short_path(c['args'])}\t"
                    f"{'' if c['status'] is None else status_text(c['status'])}\t"
                    f"{'' if c['handle'] is None else hex(c['handle'])}\n")

    # --- агрегаты
    by_name = collections.Counter(c["name"] for c in calls)
    err_by_name = collections.Counter(c["name"] for c in calls if is_error(c["status"]))
    by_group = collections.Counter(c["group"] for c in calls)
    names_in_group = collections.defaultdict(collections.Counter)
    for c in calls:
        names_in_group[c["group"]][c["name"]] += 1
    tids = sorted({c["tid"] for c in calls})
    errors = collections.Counter((c["name"], status_text(c["status"]))
                                 for c in calls if is_error(c["status"]))

    group_info = {k: (n, d) for k, n, d, _ in GROUPS + [OTHER]}

    # --- примеры аргументов
    def examples(pred, key, limit=12):
        seen, out = set(), []
        for c in calls:
            if pred(c):
                v = short_path(parse_args(c["args"]).get(key, ""))
                if v and v not in seen:
                    seen.add(v)
                    out.append((v, status_text(c["status"]) if c["status"] is not None else ""))
                    if len(out) >= limit:
                        break
        return out

    # --- шаги сценария
    blocks = collections.OrderedDict()
    blocks[0] = {"title": "Инициализация cmd.exe (до первой строки сценария)", "calls": []}
    for off, text, blk in scenario:
        m = re.match(r"\s*rem \[(\d+)\]\s*(.*)", text, re.I)
        if m:
            blocks[int(m.group(1))] = {"title": m.group(2).strip(), "calls": [], "cmds": []}
    finish = {"title": "exit /b 0 — завершение", "calls": []}
    for c in calls:
        st = c["step"]
        if st is None:
            blocks[0]["calls"].append(c)
        elif st[1].strip().lower().startswith("exit"):
            finish["calls"].append(c)
        elif st[2] in blocks:
            blocks[st[2]]["calls"].append(c)
    for off, text, blk in scenario:
        t = text.strip()
        if blk in blocks and t and not t.lower().startswith(("rem", "@echo", "exit")):
            blocks[blk].setdefault("cmds", []).append(t)
    blocks["fin"] = finish

    # --- profile.md
    total = len(calls)
    md = []
    md.append("# Профиль системных вызовов cmd.exe\n")
    md.append(f"Всего перехвачено системных вызовов: **{total}**, различных: **{len(by_name)}** "
              f"(из {len(numbers)} заглушек в ntdll.dll), потоков: **{len(tids)}**, "
              f"завершились ошибкой: **{sum(err_by_name.values())}**.\n")
    md.append("## Группы системных вызовов\n")
    md.append("| Группа | Вызовов | Доля | Различных | Функциональность cmd.exe |")
    md.append("|---|---:|---:|---:|---|")
    for key, cnt in by_group.most_common():
        n, d = group_info[key]
        md.append(f"| {n} | {cnt} | {cnt / total:.1%} | {len(names_in_group[key])} | {d} |")
    md.append("")
    for key, _cnt in by_group.most_common():
        n, _d = group_info[key]
        md.append(f"### {n}\n")
        md.append("| Системный вызов | Номер | Вызовов | Ошибок |")
        md.append("|---|---:|---:|---:|")
        for name, cnt in names_in_group[key].most_common():
            num = numbers.get(name)
            md.append(f"| {name} | {'' if num is None else f'0x{num:04X}'} | {cnt} | "
                      f"{err_by_name.get(name, 0)} |")
        md.append("")
    md.append("## Коды ошибок\n")
    md.append("| Вызов | NTSTATUS | Количество |")
    md.append("|---|---|---:|")
    for (name, st), cnt in errors.most_common():
        md.append(f"| {name} | {st} | {cnt} |")
    md.append("")
    md.append("## Примеры аргументов\n")
    for title, pred, key in [
        ("Открываемые файлы (NtCreateFile/NtOpenFile)",
         lambda c: c["name"] in ("NtCreateFile", "NtOpenFile"), "name"),
        ("Ключи реестра (NtOpenKey/NtOpenKeyEx)",
         lambda c: c["name"] in ("NtOpenKey", "NtOpenKeyEx"), "name"),
        ("Значения реестра (NtQueryValueKey)", lambda c: c["name"] == "NtQueryValueKey", "value"),
        ("Запуск процессов (NtCreateUserProcess)",
         lambda c: c["name"] == "NtCreateUserProcess", "cmdline"),
    ]:
        md.append(f"**{title}**\n")
        for v, st in examples(pred, key, limit=40):
            md.append(f"- `{md_escape(v)}` → {st}")
        md.append("")
    with open(os.path.join(out_dir, "profile.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(md))

    # --- steps.md
    sm = ["# Системные вызовы по блокам сценария scenario.cmd\n"]
    steps_json = []
    for key, b in blocks.items():
        cs = b["calls"]
        cnt = collections.Counter(c["name"] for c in cs)
        cmds = b.get("cmds", [])
        sm.append(f"## [{key}] {b['title']}\n")
        if cmds:
            sm.append("Команды: " + "; ".join(f"`{x}`" for x in cmds) + "\n")
        sm.append(f"Системных вызовов: {len(cs)}\n")
        sm.append("| Вызов | Кол-во |")
        sm.append("|---|---:|")
        for name, n in cnt.most_common(15):
            sm.append(f"| {name} | {n} |")
        key_lines = []
        for c in cs:
            a = parse_args(c["args"])
            if c["name"] in ("NtCreateFile", "NtOpenFile", "NtCreateUserProcess",
                             "NtSetInformationFile", "NtQueryDirectoryFileEx",
                             "NtWriteFile", "NtReadFile", "NtWaitForSingleObject",
                             "NtQueryValueKey", "NtTerminateProcess", "NtQueryAttributesFile"):
                if c["name"] == "NtSetInformationFile" and a.get("class") == "14":
                    continue
                desc = c["args"]
                if c["name"] in ("NtSetInformationFile",):
                    cls = int(a.get("class", "0"))
                    desc = f"h={a.get('h')}; {FILE_INFO_CLASS.get(cls, cls)}"
                key_lines.append(f"{c['name']}({short_path(desc)}) = "
                                 f"{status_text(c['status']) if c['status'] is not None else '—'}"
                                 + (f", h=0x{c['handle']:x}" if c["handle"] else ""))
        sm.append("")
        if key_lines:
            sm.append("Ключевые вызовы:\n")
            sm.append("```")
            sm.extend(key_lines[:40])
            sm.append("```")
        sm.append("")
        steps_json.append({"key": str(key), "title": b["title"], "cmds": cmds, "count": len(cs),
                           "top": cnt.most_common(8), "key_calls": key_lines})
    with open(os.path.join(out_dir, "steps.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(sm))

    # --- profile.json
    js = {
        "total": total, "distinct": len(by_name), "stubs": len(numbers), "threads": tids,
        "errors_total": sum(err_by_name.values()),
        "groups": [{"key": k, "name": group_info[k][0], "desc": group_info[k][1], "count": cnt,
                    "calls": [(n, numbers.get(n), c, err_by_name.get(n, 0))
                              for n, c in names_in_group[k].most_common()]}
                   for k, cnt in by_group.most_common()],
        "errors": [(n, s, c) for (n, s), c in errors.most_common()],
        "steps": steps_json,
        "examples": {
            "files": examples(lambda c: c["name"] in ("NtCreateFile", "NtOpenFile"), "name", 60),
            "keys": examples(lambda c: c["name"] in ("NtOpenKey", "NtOpenKeyEx"), "name", 60),
            "values": examples(lambda c: c["name"] == "NtQueryValueKey", "value", 60),
            "procs": examples(lambda c: c["name"] == "NtCreateUserProcess", "cmdline", 10),
        },
    }
    with open(os.path.join(out_dir, "profile.json"), "w", encoding="utf-8") as f:
        json.dump(js, f, ensure_ascii=False, indent=1)

    print(f"вызовов: {total}, различных: {len(by_name)}, ошибок: {sum(err_by_name.values())}")
    for k, cnt in by_group.most_common():
        print(f"  {group_info[k][0]:<55} {cnt:5d}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
