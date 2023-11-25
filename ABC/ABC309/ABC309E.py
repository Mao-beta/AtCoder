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
EI = lambda m: [NLI() for _ in range(m)]


def main():
    N, M = NMI()
    P = [-1, -1] + NLI()
    XY = EI(M)
    Y = [0] * (N+1)
    G = [[] for _ in range(N+1)]
    for i, p in enumerate(P):
        if p < 0:
            continue
        G[p].append(i)
    for x, y in XY:
        Y[x] = max(Y[x], y+1)

    ok = [0] * (N+1)

    def rec(now, y):
        y = max(y, Y[now])
        if y > 0:
            ok[now] = 1
        y -= 1
        for g in G[now]:
            if g == P[now]:
                continue
            rec(g, y)

    rec(1, 0)
    print(sum(ok))


if __name__ == "__main__":
    main()
