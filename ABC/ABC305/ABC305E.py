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
    N, M, K = NMI()
    AB = EI(M)
    PH = EI(K)
    G = adjlist(N, AB)
    PH = [[x-1, y] for x, y in PH]

    INF = N+1

    def f(h, p):
        return (N-h)*INF + p

    def inv(x):
        nh, p = divmod(x, INF)
        return N-nh, p

    hq = []
    seen = set()
    for p, h in PH:
        heappush(hq, f(h, p))

    while hq:
        x = heappop(hq)
        h, p = inv(x)
        if p in seen:
            continue
        seen.add(p)
        if h > 0:
            for g in G[p]:
                if g in seen:
                    continue
                heappush(hq, f(h-1, g))

    print(len(seen))
    seen = sorted(list(seen))
    seen = [x+1 for x in seen]
    print(*seen)


if __name__ == "__main__":
    main()
