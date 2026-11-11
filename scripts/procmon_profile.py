"""
Профиль активности cmd.exe по журналу Process Monitor (CSV).

    python procmon_profile.py procmon.csv <PID cmd.exe> <каталог_вывода>

Оставляет события процесса cmd.exe с указанным PID и всех его потомков
(событие "Process Create", в поле Detail — "PID: n"), группирует операции
Procmon по классам (File System, Registry, Process/Thread, Network) и пишет:
    procmon_cmd.csv     — отфильтрованные события
    procmon_profile.md  — сводка операций, результатов и путей
"""
import collections
import csv
import os
import re
import sys

CATEGORY = [
    ("Процессы и потоки", re.compile(r"^(Process |Thread |Load Image)")),
    ("Реестр", re.compile(r"^Reg")),
    ("Сеть", re.compile(r"^(TCP|UDP) ")),
    ("Файловая система", re.compile(r".")),
]


def category(op):
    for name, rx in CATEGORY:
        if rx.search(op):
            return name
    return "Прочее"


def read_csv(path):
    with open(path, "rb") as f:
        raw = f.read()
    for enc in ("utf-8-sig", "utf-16", "cp1251"):
        try:
            text = raw.decode(enc)
            break
        except UnicodeDecodeError:
            continue
    else:
        raise ValueError("не удалось определить кодировку CSV")
    return list(csv.DictReader(text.splitlines()))


def main():
    if len(sys.argv) != 4:
        print("использование: procmon_profile.py procmon.csv PID каталог_вывода", file=sys.stderr)
        return 2
    path, root_pid, out_dir = sys.argv[1], sys.argv[2], sys.argv[3]
    try:
        rows = read_csv(path)
    except (OSError, ValueError) as e:
        print(f"ошибка чтения {path}: {e}", file=sys.stderr)
        return 1
    if not rows or "Operation" not in rows[0]:
        print("ошибка: CSV не похож на журнал Procmon", file=sys.stderr)
        return 1

    pids = {root_pid}
    events = []
    for r in rows:
        if r["PID"] in pids:
            events.append(r)
            if r["Operation"] == "Process Create":
                m = re.search(r"PID: (\d+)", r.get("Detail", ""))
                if m:
                    pids.add(m.group(1))
    if not events:
        print(f"ошибка: нет событий для PID {root_pid}", file=sys.stderr)
        return 1

    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "procmon_cmd.csv"), "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(events)

    by_proc = collections.Counter(f"{e['Process Name']} (PID {e['PID']})" for e in events)
    by_cat = collections.Counter(category(e["Operation"]) for e in events)
    by_op = collections.Counter((category(e["Operation"]), e["Operation"]) for e in events)
    by_res = collections.Counter(e["Result"] for e in events)

    md = ["# Профиль cmd.exe по данным Process Monitor\n",
          f"Событий: **{len(events)}**\n", "## Процессы\n", "| Процесс | Событий |", "|---|---:|"]
    md += [f"| {p} | {n} |" for p, n in by_proc.most_common()]
    md += ["", "## Классы операций\n", "| Класс | Событий |", "|---|---:|"]
    md += [f"| {c} | {n} |" for c, n in by_cat.most_common()]
    md += ["", "## Операции\n", "| Класс | Операция | Событий |", "|---|---|---:|"]
    md += [f"| {c} | {o} | {n} |" for (c, o), n in by_op.most_common()]
    md += ["", "## Результаты\n", "| Result | Событий |", "|---|---:|"]
    md += [f"| {r} | {n} |" for r, n in by_res.most_common()]
    md += ["", "## Ключевые события сценария\n", "```"]
    key_ops = ("Process Create", "Process Start", "Process Exit", "WriteFile", "SetRenameInformationFile",
               "SetDispositionInformationFile", "SetDispositionInformationEx")
    for e in events:
        if e["Operation"] in key_ops or (e["Operation"] == "CreateFile" and "sandbox" in e["Path"]):
            md.append(f"{e['Time of Day']}  {e['Process Name']}:{e['PID']}  {e['Operation']:<28} "
                      f"{e['Path']}  {e['Result']}")
    md.append("```")
    with open(os.path.join(out_dir, "procmon_profile.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(md))
    print(f"событий cmd.exe и потомков: {len(events)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
