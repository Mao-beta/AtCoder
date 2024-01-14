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
    N, Q = NMI()
    P = [[i, 0] for i in range(1, N+1)][::-1]
    S = "RLUD"
    DX = [1, -1, 0, 0]
    DY = [0, 0, 1, -1]
    for i in range(Q):
        t, x = SMI()
        if t == "1":
            c = S.index(x)
            dx, dy = DX[c], DY[c]
            x, y = P[-1]
            P.append([x+dx, y+dy])
        else:
            x, y = P[-int(x)]
            print(x, y)


if __name__ == "__main__":
    main()
