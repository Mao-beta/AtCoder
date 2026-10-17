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
    N = NI()
    UVW = EI(N-1)
    G = adjlist(N, UVW)

    D = deque()
    D.append([~0, N, 0])
    D.append([0, N, 0])
    S = [1] * N
    ans = 0
    while D:
        now, par, e = D.pop()
        if now >= 0:
            for v, w in G[now]:
                if v == par:
                    continue
                D.append([~v, now, w])
                D.append([v, now, w])
        else:
            now = ~now
            if S[now] * (N-S[now]) % 2:
                ans ^= e
            if par < N:
                S[par] += S[now]
    print(ans)



if __name__ == "__main__":
    main()
