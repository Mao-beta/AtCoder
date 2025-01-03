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
    A, B = NMI()
    gap = B - A
    for g in range(gap, 0, -1):
        y = B // g * g
        x = y - g
        if A <= y <= B and A <= x <= B:
            print(g)
            exit()


if __name__ == "__main__":
    main()
