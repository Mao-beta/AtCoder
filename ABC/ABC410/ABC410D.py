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
    N, M = NMI()
    ABW = EI(M)
    G = adjlist(N, ABW, directed=True)
    dp = [[0]*(1<<10) for _ in range(N)]
    dp[0][0] = 1
    D = deque()
    D.append([0, 0])
    while D:
        now, d = D.popleft()
        for nxt, w in G[now]:
            nw = d ^ w
            if dp[nxt][nw]:
                continue
            D.append([nxt, nw])
            dp[nxt][nw] = 1
    ans = [i for i in range(1<<10) if dp[N-1][i]]
    if len(ans) == 0:
        print(-1)
    else:
        print(min(ans))


if __name__ == "__main__":
    main()
