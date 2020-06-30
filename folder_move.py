import sys
import math
import os
import glob
import shutil
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def make_grid(h, w, num): return [[int(num)] * w for _ in range(h)]


def main():
    print(os.listdir())
    ABC_dirs = glob.glob("ABC*[!py]")
    ARC_dirs = glob.glob("ARC*[!py]")
    AGC_dirs = glob.glob("AGC*[!py]")
    PAST_files = glob.glob("**/PAST*.py", recursive=True)
    print(PAST_files)
    for f in PAST_files:
        contest = "PAST"
        if not os.path.exists(contest):
            os.mkdir(contest)
        shutil.move(f, contest)



if __name__ == "__main__":
    main()