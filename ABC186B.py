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
    H, W = NMI()
    grid = [NLI() for _ in range(H)]
    mins = []
    s = 0
    for row in grid:
        mins.append(min(row))
        s += sum(row)
    print(s - min(mins) * H*W)


if __name__ == "__main__":
    main()
