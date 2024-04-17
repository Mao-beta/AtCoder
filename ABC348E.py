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
    N = NI()
    AB = EI(N-1)
    # AB = [[x-1, y-1] for x, y in AB]
    C = NLI()
    G = adjlist(N, AB)

    P = [N] * N
    S = [0] * N
    D = [0] * N
    total = sum(C)

    def dfs(now):
        S[now] = C[now]
        for g in G[now]:
            if g == P[now]:
                continue
            P[g] = now
            D[g] = D[now] + 1
            dfs(g)
            S[now] += S[g]

    dfs(0)
    ans = [0]
    for i in range(N):
        ans[0] += C[i] * D[i]


    def dfs2(now, v):
        ans[0] = min(ans[0], v)

        for g in G[now]:
            if g == P[now]:
                continue
            dfs2(g, v + total - S[g] * 2)

    dfs2(0, ans[0])

    print(ans[0])



if __name__ == "__main__":
    main()
