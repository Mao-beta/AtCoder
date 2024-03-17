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
    B = 1000
    dp = [0] * N
    dp2 = [[0]*B for _ in range(B)]
    dp[0] = 1
    for i, a in enumerate(A):
        for j in range(1, B):
            dp[i] += dp2[j][i%j]
            dp[i] %= MOD99
        if a >= B:
            for ni in range(i+a, N, a):
                dp[ni] += dp[i]
                dp[ni] %= MOD99
        else:
            dp2[a][i%a] += dp[i]
            dp2[a][i%a] %= MOD99

    print(sum(dp) % MOD99)


if __name__ == "__main__":
    main()
