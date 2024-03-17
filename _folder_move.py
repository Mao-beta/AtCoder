import sys
import math
import os
import glob
import shutil
from collections import deque
from pathlib import Path

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def make_grid(h, w, num): return [[int(num)] * w for _ in range(h)]


def main():
    target_paths = list(Path("./").glob("*.py"))
    for path in target_paths:
        contest = path.stem[:3]
        num = path.stem[3:6]
        if contest not in ["ABC", "ARC", "AGC"]:
            continue

        dst_dir = Path(f"./{contest}/{contest+num}")
        dst_dir.mkdir(parents=True, exist_ok=True)
        dst_path = dst_dir/path.name
        while dst_path.exists():
            filename = dst_path.stem + "_"
            suffix = path.suffix
            dst_path = dst_dir/(filename+suffix)
        shutil.move(path, dst_path)


    for path in target_paths:
        contest = path.stem[:3]
        if contest not in ["ADT"]:
            continue

        dst_dir = Path(f"./{contest}/")
        dst_dir.mkdir(parents=True, exist_ok=True)
        dst_path = dst_dir/path.name
        while dst_path.exists():
            filename = dst_path.stem + "_"
            suffix = path.suffix
            dst_path = dst_dir/(filename+suffix)
        shutil.move(path, dst_path)


    for path in target_paths:
        contest = path.stem[:4]

        if contest not in ["PAST", "EDPC"]:
            continue

        dst_dir = Path(f"./{contest}")
        dst_dir.mkdir(parents=True, exist_ok=True)
        dst_path = dst_dir/path.name
        while dst_path.exists():
            filename = dst_path.stem + "_"
            suffix = path.suffix
            dst_path = dst_dir/(filename+suffix)
        shutil.move(path, dst_path)


    for path in target_paths:
        contest = path.stem[:4]

        if contest not in ["yuki"]:
            continue

        dst_dir = Path(f"./{contest}")
        dst_dir.mkdir(parents=True, exist_ok=True)
        dst_path = dst_dir/path.name
        while dst_path.exists():
            filename = dst_path.stem + "_"
            suffix = path.suffix
            dst_path = dst_dir/(filename+suffix)
        shutil.move(path, dst_path)


    for path in target_paths:
        contest = path.stem[:8]

        if contest != "tenkei90":
            continue

        dst_dir = Path(f"./{contest}")
        dst_dir.mkdir(parents=True, exist_ok=True)
        dst_path = dst_dir/path.name
        while dst_path.exists():
            filename = dst_path.stem + "_"
            suffix = path.suffix
            dst_path = dst_dir/(filename+suffix)
        shutil.move(path, dst_path)



if __name__ == "__main__":
    main()