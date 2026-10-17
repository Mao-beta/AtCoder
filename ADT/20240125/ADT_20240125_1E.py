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
    N = NI()
    dp = [[0]*10 for _ in range(N+1)]
    for i in range(1, 10):
        dp[1][i] = 1
    for i in range(1, N):
        for j in range(1, 10):
            ni = i+1
            for nj in range(j-1, j+2):
                if 1 <= nj <= 9:
                    dp[ni][nj] += dp[i][j]
                    dp[ni][nj] %= MOD99
    print(sum(dp[N])%MOD99)


if __name__ == "__main__":
    main()
