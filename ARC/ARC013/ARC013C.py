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
    N = NI()
    g = 0
    for _ in range(N):
        xi, yi, zi = NMI()
        M = NI()
        xm, ym, zm = xi, yi, zi
        xM, yM, zM = 0, 0, 0
        for _ in range(M):
            x, y, z = NMI()
            xm = min(xm, x)
            ym = min(ym, y)
            zm = min(zm, z)
            xM = max(xM, x+1)
            yM = max(yM, y+1)
            zM = max(zM, z+1)
        # print(xm, xM, ym, yM, zm, zM)
        g ^= xm ^ ym ^ zm ^ (xi-xM) ^ (yi-yM) ^ (zi-zM)
    if g:
        print("WIN")
    else:
        print("LOSE")


if __name__ == "__main__":
    main()
