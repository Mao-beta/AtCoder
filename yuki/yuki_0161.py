import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

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


def main():
    G, C, P = NMI()
    S = SI()
    INF = 10**5
    dp = [[[-INF]*(P+1) for _ in range(C+1)] for _ in range(G+1)]
    dp[G][C][P] = 0
    for g in range(G, -1, -1):
        for c in range(C, -1, -1):
            for p in range(P, -1, -1):
                i = G+C+P-g-c-p
                if i == G+C+P:
                    continue
                s = S[i]
                d = dp[g][c][p]
                if s == "G":
                    if g:
                        dp[g-1][c][p] = max(dp[g-1][c][p], d+1)
                    if c:
                        dp[g][c-1][p] = max(dp[g][c-1][p], d)
                    if p:
                        dp[g][c][p-1] = max(dp[g][c][p-1], d+3)
                if s == "C":
                    if g:
                        dp[g-1][c][p] = max(dp[g-1][c][p], d+3)
                    if c:
                        dp[g][c-1][p] = max(dp[g][c-1][p], d+1)
                    if p:
                        dp[g][c][p-1] = max(dp[g][c][p-1], d)
                if s == "P":
                    if g:
                        dp[g-1][c][p] = max(dp[g-1][c][p], d)
                    if c:
                        dp[g][c-1][p] = max(dp[g][c-1][p], d+3)
                    if p:
                        dp[g][c][p-1] = max(dp[g][c][p-1], d+1)
    print(dp[0][0][0])


if __name__ == "__main__":
    main()
