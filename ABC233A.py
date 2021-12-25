import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict
from functools import lru_cache

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


def solve(X, Y):
    if X >= Y:
        print(0)
    else:
        res = Y - X
        print(res//10 + 1 if res % 10 else res//10)


def main():
    # input
    X, Y = NMI()
    # solve
    solve(X, Y)


if __name__ == "__main__":
    main()
