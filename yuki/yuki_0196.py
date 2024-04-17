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


def adjlist(n, edges, directed=False, in_origin=1):
    if len(edges) == 0:
        return [[] for _ in range(n)]

    weighted = True if len(edges[0]) > 2 else False
    if in_origin == 1:
        if weighted:
            edges = [[x-1, y-1, w] for x, y, w in edges]
        else:
            edges = [[x-1, y-1] for x, y in edges]

    res = [[] for _ in range(n)]

    if weighted:
        for u, v, c in edges:
            res[u].append([v, c])
            if not directed:
                res[v].append([u, c])

    else:
        for u, v in edges:
            res[u].append(v)
            if not directed:
                res[v].append(u)

    return res


def main():
    N, K = NMI()
    AB = EI(N-1)
    # i以下の部分木でj個塗る
    dp = [[0]*(N+1) for _ in range(N)]
    P = [N] * N
    G = adjlist(N, AB, in_origin=0)
    # i以下の部分木のサイズ
    SZ = [0] * N

    # 二乗の木DP

    def dfs(now):
        SZ[now] = 1
        dp[now][0] = 1
        for v in G[now]:
            if v == P[now]:
                continue
            P[v] = now
            dfs(v)
            for i in range(SZ[now], -1, -1):
                for j in range(SZ[v], 0, -1):
                    dp[now][i+j] += dp[now][i] * dp[v][j] % MOD
                    dp[now][i+j] %= MOD
            SZ[now] += SZ[v]
        dp[now][SZ[now]] = 1

    dfs(0)
    print(dp[0][K])


if __name__ == "__main__":
    main()
