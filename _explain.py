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
    A = NLI()
    INF = 10**18
    dp = [[INF]*(2*N+1) for _ in range(2*N+1)]

    for l in range(2*N, -1, -1):
        for r in range(l, 2*N+1):
            if l == r:
                dp[l][r] = 0
                continue
            for m in range(l+1, r):
                dp[l][r] = min(dp[l][r], dp[l][m] + dp[m][r])
            if r-l >= 2:
                dp[l][r] = min(dp[l][r], dp[l+1][r-1] + abs(A[l]-A[r-1]))

    print(dp[0][2*N])


if __name__ == "__main__":
    main()
