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
    N, M = NMI()
    ABC = EI(M)
    G = [[] for _ in range(N)]
    for a, b, c in ABC:
        a, b = a-1, b-1
        G[a].append([b, c])
        G[b].append([a, c])

    INF = 10**15
    D = [10**22] * N
    D[0] = 0
    # ice, d, v
    hq = [[0, 0, 0]]
    while hq:
        ice, d, v = heappop(hq)
        if D[v] < ice * INF + d:
            continue

        for g, c in G[v]:
            if c == -1:
                nice = ice + 1
                nd = d + 1
            else:
                nice = ice
                nd = max(d, c) + 1

            if D[g] < nice * INF + nd:
                continue

            D[g] = nice * INF + nd
            heappush(hq, [nice, nd, g])

    print(D)
    ice, d = divmod(D[-1], INF)
    print(d)


if __name__ == "__main__":
    main()
