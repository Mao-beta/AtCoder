import sys
import os
import glob
import shutil
import math
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
    os.chdir("C:\\Users\\User\\PycharmProjects\\AtCoder")
    print(os.path.dirname(os.path.abspath(__file__)))
    print(os.getcwd())
    ABC_files = glob.glob("ABC*.py")
    ARC_files = glob.glob("ARC*.py")
    AGC_files = glob.glob("AGC*.py")
    PAST_files = glob.glob("PAST*.py")
    for f in ABC_files:
        contest = f[0:6]
        if not os.path.exists(contest):
            os.mkdir(contest)
        shutil.move(f, contest)

    for f in ARC_files:
        contest = f[0:6]
        if not os.path.exists(contest):
            os.mkdir(contest)
        shutil.move(f, contest)

    for f in AGC_files:
        contest = f[0:6]
        if not os.path.exists(contest):
            os.mkdir(contest)
        shutil.move(f, contest)

    for f in PAST_files:
        contest = f[0:6]
        if not os.path.exists(contest):
            os.mkdir(contest)
        shutil.move(f, contest)



if __name__ == "__main__":
    main()