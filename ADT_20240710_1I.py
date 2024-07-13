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
    UVW = EI(M)
    UVW = [[x-1, y-1, w] for x, y, w in UVW]
    K = NI()
    A = NLI()
    A = set([x-1 for x in A])
    D = NI()
    X = NLI()

    G = adjlist(N, UVW, in_origin=0)

    INF = 10**10
    hq = []
    ans = [INF] * N
    for a in A:
        ans[a] = 0
        for v, w in G[a]:
            if v in A:
                continue
            heappush(hq, [w, v])

    for turn, x in enumerate(X, start=1):
        nhq = []
        while hq:
            if hq[0][0] > x:
                break
            d, now = heappop(hq)




if __name__ == "__main__":
    main()
