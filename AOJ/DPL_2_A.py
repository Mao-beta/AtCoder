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


def TSP(N, D, start):
    """
    巡回セールスマン問題 O(N^2*2^N)
    :param N: 頂点数
    :param D: NxNの距離行列
    :param start: 始点のindex
    :return: 最短距離
    """
    INF = 10**15
    dp = [[INF] * (1<<N) for _ in range(N)]
    dp[start][0] = 0

    for case in range(1<<N):
        for u in range(N):
            if dp[u][case] >= INF:
                continue
            for v in range(N):
                if (case >> v) & 1:
                    continue
                dp[v][case|(1<<v)] = min(dp[v][case|(1<<v)], dp[u][case] + D[u][v])

    return dp[start][-1]


def main():
    N, M = NMI()
    edges = EI(M)
    edges = [[x-1, y-1, w] for x, y, w in edges]
    INF = 10**15
    D = [[INF]*N for _ in range(N)]
    for x, y, w in edges:
        D[x][y] = w

    ans = INF
    for s in range(N):
        ans = min(ans, TSP(N, D, s))

    print(-1 if ans == INF else ans)


if __name__ == "__main__":
    main()
