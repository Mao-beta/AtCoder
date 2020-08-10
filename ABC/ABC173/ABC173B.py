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
    D = {"AC": 0, "WA": 0, "TLE": 0, "RE": 0}
    for i in range(N):
        D[SI()] += 1
    for x, y in D.items():
        print("{0} x {1}".format(x, y))


if __name__ == "__main__":
    main()