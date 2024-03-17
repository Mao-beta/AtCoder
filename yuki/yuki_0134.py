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
NMI = lambda: map(float, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()
SMI = lambda: input().split()
SLI = lambda: list(SMI())
EI = lambda m: [NLI() for _ in range(m)]


def TSP(N, D, start, W):
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
        w = 0
        for i in range(N):
            if (case >> i) & 1 == 0:
                w += W[i]

        for u in range(N):
            if dp[u][case] >= INF/2:
                continue
            for v in range(N):
                if (case >> v) & 1:
                    continue
                dp[v][case|(1<<v)] = min(dp[v][case|(1<<v)], dp[u][case] + D[u][v] * (w+100) / 120 + W[u])

    return dp[start][-1]


def main():
    XY = [NLI()]
    N = NI()
    W = [0]
    for _ in range(N):
        x, y, w = NMI()
        XY.append([x, y])
        W.append(w)
    D = [[0]*(N+1) for _ in range(N+1)]
    for i in range(N+1):
        xi, yi = XY[i]
        for j in range(N+1):
            xj, yj = XY[j]
            D[i][j] = abs(xi-xj) + abs(yi-yj)

    ans = TSP(N+1, D, 0, W)
    print(ans)


if __name__ == "__main__":
    main()
