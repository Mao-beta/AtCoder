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
    N, X = NMI()
    XYC = [NLI() for _ in range(N-1)]
    G = adjlist(N, XYC)

    xors = [0] * N

    def dfs(now, par, x):
        xors[now] = x
        for goto, c in G[now]:
            if goto == par:
                continue
            dfs(goto, now, x^c)

    dfs(0, N, 0)
    C = Counter(xors)

    ans = 0
    for i, x in enumerate(xors):
        target = X ^ x
        ans += C[target]
        if xors[i] == target:
            ans -= 1

    print(ans//2)


if __name__ == "__main__":
    main()
