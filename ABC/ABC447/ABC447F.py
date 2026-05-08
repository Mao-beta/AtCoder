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
    Q = NI()

    for _ in range(Q):
        N = NI()
        AB = EI(N-1)
        G = adjlist(N, AB)
        ans = [1]

        def dfs(now, par):
            # print(now, par)
            res = 0
            D = []
            for g in G[now]:
                if g == par:
                    continue
                d = dfs(g, now)
                D.append(d)
            D.sort()
            # print(now, par, D)
            if len(G[now]) <= 2:
                res = 0
            elif len(G[now]) == 3:
                res = 1
                ans[0] = max(ans[0], D[-1] + 1)
            else:
                ans[0] = max(ans[0], D[-1] + D[-2] + 1)
                res = max(res, D[-1] + 1)
            # print(f"{now+1=}, {par+1=}, {res=}")
            return res

        dfs(0, N)
        print(ans[0])


if __name__ == "__main__":
    main()
