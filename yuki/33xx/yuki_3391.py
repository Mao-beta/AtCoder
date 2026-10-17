import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.set_int_max_str_digits(10 ** 6)
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
    N, M, K = NMI()
    A = sorted(NLI())
    L = [0] * N
    R = [0] * N
    l, r = 0, 0

    for i, a in enumerate(A):
        while l < N and A[l] < a-K:
            l += 1
        L[i] = l
        while r < N and A[r] <= a+K:
            r += 1
        R[i] = r

    dp = [1] * (N+1)
    dp[0] = 0
    dp2 = [0] * (N+1)
    for _ in range(M-1):
        for j in range(N):
            dp[j+1] += dp[j]
            dp[j+1] %= MOD99
        for j in range(N):
            dp2[j+1] = (dp[R[j]] - dp[L[j]]) % MOD99
        dp, dp2 = dp2, dp
    print(sum(dp) % MOD99)


if __name__ == "__main__":
    main()
