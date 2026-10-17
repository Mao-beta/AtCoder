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


def adjlist(n, edges, directed=False, in_origin=1):
    if len(edges) == 0:
        return [[] for _ in range(n)]

    weighted = True if len(edges[0]) > 2 else False
    if in_origin == 1:
        if weighted:
            edges = [[x - 1, y - 1, w] for x, y, w in edges]
        else:
            edges = [[x - 1, y - 1] for x, y in edges]

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
    N = NI()
    UV = EI(N-1)
    G = [[] for _ in range(N)]
    for i, (u, v) in enumerate(UV):
        u, v = u-1, v-1
        G[u].append([v, i])
        G[v].append([u, i])

    ans = [0]
    R = [-1] * N
    L = [N] * N

    def dfs(now, par):
        # print(now, par, L, R)
        if now == 0:
            ans[0] += N * (N-1) // 2
        else:
            ans[0] += (L[now] + 1) * (N-1 - R[now])
            # print((L[now] + 1) * (N-1 - R[now]))

        for g, i in G[now]:
            if g == par:
                continue
            R[g] = max(R[now], i)
            L[g] = min(L[now], i)
            dfs(g, now)


    dfs(0, N)
    # print(L)
    # print(R)
    print(ans[0])


if __name__ == "__main__":
    main()
