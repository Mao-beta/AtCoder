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


def main():
    S = SI()
    T = SI()
    N = len(S)
    M = len(T)
    K = NI()
    INF = 10**6
    dp = [[[-INF]*(K+1) for _ in range(M+1)] for _ in range(N+1)]
    dp[0][0][0] = 0
    for i in range(N+1):
        for j in range(M+1):
            for k in range(K+1):
                d = dp[i][j][k]
                if d < 0:
                    continue
                if i < N:
                    dp[i+1][j][k] = max(dp[i+1][j][k], d)
                if j < M:
                    dp[i][j+1][k] = max(dp[i][j+1][k], d)
                if i < N and j < M:
                    if S[i] == T[j]:
                        dp[i+1][j+1][k] = max(dp[i+1][j+1][k], d+1)
                    if k < K:
                        dp[i+1][j+1][k+1] = max(dp[i+1][j+1][k+1], d+1)
    print(max(dp[-1][-1]))


if __name__ == "__main__":
    main()
