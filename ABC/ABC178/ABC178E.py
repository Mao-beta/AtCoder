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
    Ps = [NLI() for _ in range(N)]
    Px = [x+y for x, y in Ps]
    Py = [x-y for x, y in Ps]
    print(max(max(Px) - min(Px), max(Py) - min(Py)))


if __name__ == "__main__":
    main()