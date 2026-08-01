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
    S = SI()
    N = len(S)
    dp = [[0]*4 for _ in range(N+1)]
    dp[0][0] = 1
    for i, s in enumerate(S):
        s = ord(s) - ord("a") + 1
        for j in range(4):
            dp[i+1][j] += dp[i][j]
            dp[i+1][j] %= MOD99
            if s == j:
                continue
            dp[i+1][s] += dp[i][j]
            dp[i+1][s] %= MOD99
        # print(dp[i])
    print(sum(dp[N][1:]) % MOD99)


if __name__ == "__main__":
    main()
