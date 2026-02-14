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
    # 左右反転
    S = [SI()[::-1] for _ in range(N)]
    # print(*S, sep='\n')
    INF = 10**8
    # i段目まで決めて白黒境界がj
    dp = [INF]*(N+1)
    dp[0] = 0
    for i in range(N):
        dp2 = [INF] * (N+1)
        # dp[i+1][j] <- min(dp[i][:j+1])+add
        b = S[i].count("#")
        w = 0
        cum = dp[0]
        for j in range(N+1):
            dp2[j] = cum + w+b
            if j < N:
                cum = min(cum, dp[j+1])
                if S[i][j] == ".":
                    w += 1
                else:
                    b -= 1
        dp = dp2
        # print(dp)
    print(min(dp))


if __name__ == "__main__":
    main()
