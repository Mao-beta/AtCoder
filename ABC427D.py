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
    N, M, K = NMI()
    S = SI()
    UV = EI(M)
    UV = [[x-1, y-1] for x, y in UV]
    G = adjlist(N, UV, in_origin=0, directed=True)

    dp = [[-1]*N for _ in range(2*K+1)]
    for v in range(N):
        if S[v] == "A":
            dp[2*K][v] = 0
        else:
            dp[2*K][v] = 1

    for i in range(2*K-1, -1, -1):
        # A側
        if i % 2 == 0:
            for v, gv in enumerate(G):
                win = False
                for g in gv:
                    if dp[i+1][g] == 0:
                        win = True
                if win:
                    dp[i][v] = 0
                else:
                    dp[i][v] = 1
        # B側
        else:
            for v, gv in enumerate(G):
                win = False
                for g in gv:
                    if dp[i+1][g] == 1:
                        win = True
                if win:
                    dp[i][v] = 1
                else:
                    dp[i][v] = 0

    # print(*dp, sep="\n")

    print("Bob" if dp[0][0] else "Alice")


def main():
    T = NI()
    for _ in range(T):
        solve()


if __name__ == "__main__":
    main()
