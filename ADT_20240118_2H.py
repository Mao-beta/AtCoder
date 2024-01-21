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
    N, M = NMI()
    A, B, C, D, E, F = NMI()
    XY = set(tuple(NMI()) for _ in range(M))
    dp = [[[0]*(N+1) for _ in range(N+1)] for _ in range(N+1)]
    dp[0][0][0] = 1

    def xy(i, j, k):
        return A*i + C*j + E*k, B*i + D*j + F*k

    for ijk in range(N):
        for i in range(N):
            jk = ijk - i
            for j in range(N):
                k = jk - j
                if k < 0:
                    continue
                d = dp[i][j][k]
                # print(i, j, k, d)
                if xy(i+1, j, k) not in XY:
                    dp[i+1][j][k] += d
                    dp[i+1][j][k] %= MOD99
                if xy(i, j+1, k) not in XY:
                    dp[i][j+1][k] += d
                    dp[i][j+1][k] %= MOD99
                if xy(i, j, k+1) not in XY:
                    dp[i][j][k+1] += d
                    dp[i][j][k+1] %= MOD99

    ans = 0
    for i in range(N+1):
        jk = N - i
        for j in range(N+1):
            k = jk - j
            if k < 0:
                continue
            ans += dp[i][j][k]
            # print(i, j, k, dp[i][j][k])
    print(ans % MOD99)


if __name__ == "__main__":
    main()
