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
    ABC_files = Path("./").glob("AGC*")
    for path in ABC_files:
        if path.name == "AGC":
            continue
        print(path)
        contest = path.name[:6]
        print(contest)
        goto_fol = Path("AGC")/contest
        shutil.move(str(path), str(goto_fol))




if __name__ == "__main__":
    main()