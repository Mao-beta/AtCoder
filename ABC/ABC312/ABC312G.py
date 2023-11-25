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
    N = NI()
    AB = EI(N-1)
    G = adjlist(N, AB)

    ans = [N * (N-1) * (N-2) // 6]

    def dfs(now, par):
        X = []
        for g in G[now]:
            if g == par:
                continue
            X.append(dfs(g, now))
        subsize = sum(X) + 1
        X.append(N - subsize)

        # Xの相異なる2項の積の和
        # = ((Σx)^2 - Σ(x^2)) // 2
        s = ((N-1)**2 - sum([x**2 for x in X])) // 2
        ans[0] -= s
        return subsize

    dfs(0, N)
    print(ans[0])


if __name__ == "__main__":
    main()
