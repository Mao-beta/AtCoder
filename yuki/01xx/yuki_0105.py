import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

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
EI = lambda m: [NLI() for _ in range(m)]


def main():
    eps = 1e-11
    xl = math.cos(math.pi * 50 / 180) - eps
    xr = 1 + eps
    yl = 0 - eps
    yr = math.sin(math.pi * 50 / 180) + eps

    T = NI()
    for _ in range(T):
        _ = SI()
        XY = [list(map(float, input().split())) for _ in range(6)]
        for x, y in XY:
            if xl < x < xr and yl < y < yr:
                a = math.atan2(y, x)
                print(a * 180 / math.pi)


if __name__ == "__main__":
    main()
