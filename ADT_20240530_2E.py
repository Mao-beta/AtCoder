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


def main():
    N = NI()
    dp = [[0]*11 for _ in range(N+1)]
    for j in range(1, 10):
        dp[1][j] = 1
    for i in range(2, N+1):
        for j in range(1, 10):
            dp[i][j] = dp[i-1][j] + dp[i-1][j-1] + dp[i-1][j+1]
            dp[i][j] %= MOD99
    print(sum(dp[-1]) % MOD99)


if __name__ == "__main__":
    main()