import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.set_int_max_str_digits(10**6)
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


def adjlist(n, edges, directed=False, in_origin=1) -> list[list[int]]:
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
    UV = EI(N-1)
    A = NLI()
    G = adjlist(N, UV)
    INF = 10**8
    SZ = [0] * N
    dp0 = [[-INF for _ in range(N+1)] for _ in range(N)]
    dp1 = [[-INF for _ in range(N+1)] for _ in range(N)]

    def dfs(now, par):
        sz = 1
        if par < N:
            pidx = G[now].index(par)
            del G[now][pidx]
        n = len(G[now])

        for goto in G[now]:
            dfs(goto, now)
            sz += SZ[goto]
        SZ[now] = sz
        sdp0 = [[-INF for _ in range(sz+1)] for _ in range(n+1)]
        sdp1 = [[-INF for _ in range(sz+1)] for _ in range(n+1)]
        sdp0[0][0] = 0
        sdp1[0][0] = 0
        for i in range(n):
            v = G[now][i]
            for j in range(sz+1):
                if sdp0[i][j] >= 0:
                    for k in range(sz+1):
                        if j+k > sz:
                            break
                        sdp0[i+1][j+k] = max(sdp0[i+1][j+k], sdp0[i][j] + dp0[v][k])
                if sdp1[i][j] >= 0:
                    for k in range(sz+1):
                        if j+k > sz:
                            break
                        sdp1[i+1][j+k] = max(sdp1[i+1][j+k],
                                             sdp1[i][j] + dp1[v][k],
                                             sdp1[i][j] + dp0[v][k],
                                             sdp0[i][j] + dp0[v][k])

        for j in range(sz+1):
            dp0[now][j] = sdp1[-1][j]
            if j >= 1:
                dp1[now][j] = max(sdp0[-1][j-1] + A[now], sdp1[-1][j])

    dfs(0, N)
    ans = max(dp0[0][K], dp1[0][K])
    if ans < 0:
        print(-1)
    else:
        print(ans)


if __name__ == "__main__":
    main()
