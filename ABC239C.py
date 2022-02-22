import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
MOD99 = 998244353

input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()
SMI = lambda: input().split()
SLI = lambda: list(SMI())


def main():
    x1, y1, x2, y2 = NMI()
    x = x2 - x1
    y = y2 - y1
    DX = [1, 2, 2, 1, -1, -2, -2, -1]
    DY = [2, 1, -1, -2, -2, -1, 1, 2]
    for X, Y in zip(DX, DY):
        for dx, dy in zip(DX, DY):
            nx, ny = X + dx, Y + dy
            if x == nx and y == ny:
                print("Yes")
                exit()

    print("No")


if __name__ == "__main__":
    main()
