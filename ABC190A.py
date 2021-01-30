import sys
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
    A, B, C = NMI()
    if C:
        if A >= B:
            print("Takahashi")
        else:
            print("Aoki")
    else:
        if A > B:
            print("Takahashi")
        else:
            print("Aoki")


if __name__ == "__main__":
    main()
