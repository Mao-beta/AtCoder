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


def solve():
    N, M, X, Y = NMI()
    X, Y = X - 1, Y - 1
    UV = EI(M)
    G = adjlist(N, UV)
    ans = []
    seen = [0] * N
    finished = [0]

    def dfs(now, par):
        if finished[0]:
            return
        seen[now] = 1
        ans.append(now+1)
        if now == Y:
            print(*ans)
            finished[0] = 1
            return

        for g in sorted(G[now]):
            if g == par:
                continue
            if seen[g]:
                continue
            if finished[0]:
                return
            dfs(g, now)
            if finished[0]:
                return

        ans.pop()
        if finished[0]:
            return

    dfs(X, N)


def main():
    T = NI()
    for _ in range(T):
        solve()


if __name__ == "__main__":
    main()
