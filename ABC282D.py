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


def is_bipartite(N, graph):
    colors = [-1] * N

    def dfs_paint_01_color(start):
        if colors[start] != -1:
            return True, [0, 0]

        stack = deque()
        stack.append(start)

        colors[start] = 0
        ns = [0, 0]

        while stack:
            now = stack.pop()
            c = colors[now]
            ns[c] += 1

            for goto in graph[now]:
                if colors[goto] == 1 - c:
                    continue
                elif colors[goto] == c:
                    return False, ns
                stack.append(goto)
                colors[goto] = 1 - c

        return True, ns

    ext, inc = 0, 0
    for s in range(N):
        f, ns = dfs_paint_01_color(s)
        if not f:
            print(0)
            exit()

        ext += (N - sum(ns)) * sum(ns)
        inc += ns[0] * ns[1]

    return ext // 2 + inc


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
    N, M = NMI()
    UV = EI(M)

    G = adjlist(N, UV)
    print(is_bipartite(N, G) - M)


if __name__ == "__main__":
    main()
