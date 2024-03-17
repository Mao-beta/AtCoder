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


def TSP(N, D, start):
    """
    巡回セールスマン問題 O(N^2*2^N)
    :param N: 頂点数
    :param D: NxNの距離行列
    :param start: 始点のindex
    :return: 最短距離
    """
    INF = 100
    dp = [[INF] * (1<<N) for _ in range(N)]
    dp[start][1<<start] = 0

    for case in range(1<<N):
        for u in range(N):
            if dp[u][case] >= INF:
                continue
            for v in range(N):
                if (case >> v) & 1:
                    continue
                dp[v][case|(1<<v)] = min(dp[v][case|(1<<v)], dp[u][case] + D[u][v])

    res = INF
    for i in range(N):
        res = min(res, dp[i][-1])
    return res


def main():
    N, M, K = NMI()
    UV = EI(M)
    UV = [[x-1, y-1] for x, y in UV]
    INF = 100

    # ワーシャルフロイド
    D = [[INF]*N for _ in range(N)]
    for i in range(N):
        D[i][i] = 0
    for u, v in UV:
        D[u][v] = 1
        D[v][u] = 1
    for k in range(N):
        for u in range(N):
            for v in range(N):
                D[u][v] = min(D[u][v], D[u][k] + D[k][v])

    A = [(1<<(k-1))-1 for k in range(1, N+1)]
    ans = 0

    # 回ることにした頂点(0以外)
    fixed = [0]
    for x in range(N-1, 0, -1):
        # xはK歩で行けるなら絶対fixedに入れる
        if D[0][x] > K:
            continue
        fixed.append(x)
        if len(fixed) > K+1:
            break
        n = len(fixed)
        FD = [[INF]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                FD[i][j] = D[fixed[i]][fixed[j]]
        k = TSP(n, FD, 0)
        if k > K:
            fixed.pop()
        else:
            ans += A[x]

    print(ans)


if __name__ == "__main__":
    main()
