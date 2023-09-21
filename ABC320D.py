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
    ABXY = EI(M)
    G = [[] for _ in range(N)]
    for a, b, x, y in ABXY:
        a, b = a-1, b-1
        G[a].append([b, x, y])
        G[b].append([a, -x, -y])

    INF = 10**18
    P = [[INF, INF] for _ in range(N)]
    P[0] = [0, 0]

    def dfs(now):
        x, y = P[now]
        for g, dx, dy in G[now]:
            if P[g][0] < INF:
                continue
            P[g] = [x+dx, y+dy]
            dfs(g)

    dfs(0)
    for x, y in P:
        if x < INF:
            print(x, y)
        else:
            print("undecidable")


if __name__ == "__main__":
    main()
