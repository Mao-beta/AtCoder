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
    N, M = NMI()
    UV = EI(M)
    A = EI(N-1)

    G = adjlist(N, UV)
    for i in range(N):
        G[i] = set(G[i])

    INF = 10**15
    # dp[case] 回ったのがcaseのときの最大値
    dp = [-INF] * (1<<N)
    dp[1] = 0
    for case in range(1<<N):
        if dp[case] < 0:
            continue
        day = bin(case).count("1") - 1
        for goto in range(N):
            if (case >> goto) & 1:
                continue
            for now in range(N):
                if (case >> now) & 1 == 0:
                    continue
                if goto not in G[now]:
                    continue
                goto_c = case | (1<<goto)
                dp[goto_c] = max(dp[goto_c], dp[case] + A[day][goto])
                break
    print(dp[-1])


if __name__ == "__main__":
    main()
