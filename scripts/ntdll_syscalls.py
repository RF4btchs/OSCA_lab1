"""
Извлечение списка системных вызовов из ntdll.dll.

Каждый системный вызов Windows в user mode представлен в ntdll.dll
заглушкой (stub) вида:

    4C 8B D1          mov  r10, rcx
    B8 xx xx xx xx    mov  eax, <номер системного вызова>
    ...               syscall / int 2Eh

Скрипт разбирает таблицу экспорта PE-файла, берёт функции Nt*,
проверяет, что они начинаются с такой заглушки, и сохраняет пары
"имя -> номер". Функции Nt*, не являющиеся заглушками (например,
NtGetTickCount, читающая KUSER_SHARED_DATA), отбрасываются — это не
системные вызовы, и трассировать их как syscall было бы ошибкой.

Использование:
    python ntdll_syscalls.py [путь_к_ntdll.dll] > syscalls.tsv
"""
import struct
import sys


def read_pe_exports(path):
    with open(path, "rb") as f:
        data = f.read()

    if data[:2] != b"MZ":
        raise ValueError("не PE-файл (нет сигнатуры MZ)")
    pe = struct.unpack_from("<I", data, 0x3C)[0]
    if data[pe:pe + 4] != b"PE\0\0":
        raise ValueError("не PE-файл (нет сигнатуры PE)")

    n_sections = struct.unpack_from("<H", data, pe + 6)[0]
    opt_size = struct.unpack_from("<H", data, pe + 20)[0]
    opt = pe + 24
    magic = struct.unpack_from("<H", data, opt)[0]
    if magic != 0x20B:
        raise ValueError("ожидался PE32+ (x64)")
    export_rva, _ = struct.unpack_from("<II", data, opt + 112)

    sections = []
    sec = opt + opt_size
    for i in range(n_sections):
        vsize, va, rawsize, rawptr = struct.unpack_from("<IIII", data, sec + i * 40 + 8)
        sections.append((va, max(vsize, rawsize), rawptr))

    def rva2off(rva):
        for va, size, raw in sections:
            if va <= rva < va + size:
                return rva - va + raw
        raise ValueError(f"RVA {rva:#x} вне секций")

    ed = rva2off(export_rva)
    n_funcs, n_names, a_funcs, a_names, a_ords = struct.unpack_from("<IIIII", data, ed + 20)
    funcs = struct.unpack_from(f"<{n_funcs}I", data, rva2off(a_funcs))
    names = struct.unpack_from(f"<{n_names}I", data, rva2off(a_names))
    ords = struct.unpack_from(f"<{n_names}H", data, rva2off(a_ords))

    for name_rva, ordinal in zip(names, ords):
        o = rva2off(name_rva)
        name = data[o:data.index(b"\0", o)].decode("ascii")
        func_rva = funcs[ordinal]
        yield name, func_rva, data[rva2off(func_rva):rva2off(func_rva) + 8]


def syscall_stubs(path):
    result = {}
    for name, _rva, code in read_pe_exports(path):
        if not name.startswith("Nt") or name.startswith("Ntdll"):
            continue
        if code[:4] == b"\x4C\x8B\xD1\xB8":          # mov r10,rcx ; mov eax,imm32
            result[name] = struct.unpack_from("<I", code, 4)[0]
    return result


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else r"C:\Windows\System32\ntdll.dll"
    try:
        stubs = syscall_stubs(path)
    except (OSError, ValueError) as e:
        print(f"ошибка: {path}: {e}", file=sys.stderr)
        return 1
    if not stubs:
        print("ошибка: заглушки системных вызовов не найдены", file=sys.stderr)
        return 1
    for name, num in sorted(stubs.items(), key=lambda kv: kv[1]):
        print(f"{name}\t{num:#06x}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
