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
    UVW = EI(M)
    UVW = [[x-1, y-1, w] for x, y, w in UVW]
    INF = 10**10
    D = [[INF]*N for _ in range(N)]
    for i in range(N):
        D[i][i] = 0
    for u, v, w in UVW:
        D[u][v] = w
    for k in range(N):
        for i in range(N):
            for j in range(N):
                D[i][j] = min(D[i][j], D[i][k]+D[k][j])

    # TSP
    # dp[now][S]
    dp = [[INF]*(1<<N) for _ in range(N)]
    for i in range(N):
        dp[i][1<<i] = 0

    for case in range(1<<N):
        for now in range(N):
            if dp[now][case] >= INF//2:
                continue
            for g in range(N):
                if (case >> g) & 1:
                    continue
                dp[g][case|(1<<g)] = min(dp[g][case|(1<<g)], dp[now][case] + D[now][g])

    ans = INF
    for i in range(N):
        ans = min(ans, dp[i][-1])

    if ans >= INF//2:
        print("No")
    else:
        print(ans)


if __name__ == "__main__":
    main()
