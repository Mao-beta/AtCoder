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
    N = NI()
    ans = 0

    if N <= 999:
        print(0)
        exit()
    if N <= 999999:
        print(0 + (N-999)*1)
        exit()
    if N <= 999999999:
        print(999 * 0 + 999000 * 1 + (N-999999) * 2)
        exit()
    if N <= 999999999999:
        print(999 * 0 + 999000 * 1 + 999000000 * 2 + (N-999999999) * 3)
        exit()
    if N <= 999999999999999:
        print(999 * 0 + 999000 * 1 + 999000000 * 2 + 999000000000 * 3 + (N-999999999999) * 4)
        exit()
    if N <= 999999999999999999:
        print(999 * 0 + 999000 * 1 + 999000000 * 2 + 999000000000 * 3 + 999000000000000 * 4 + (N-999999999999999) * 5)
        exit()


if __name__ == "__main__":
    main()
