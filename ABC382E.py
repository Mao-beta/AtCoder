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
    N, X = NMI()
    P = NLI()
    # 1パック内でのレア入手枚数についての確率
    # i枚見てレアがj枚のときの確率
    dp = [[0.0]*(N+1) for _ in range(N+1)]
    dp[0][0] = 1.0
    for i, p in enumerate(P):
        for j in range(i+1):
            dp[i+1][j] += dp[i][j] * (100-p) / 100
            dp[i+1][j+1] += dp[i][j] * p / 100
    # 残りi枚のレアを引けばいいときの開封個数の期待値
    DP = [0.0] * (X+1)
    for i in range(1, X+1):
        bunbo = 1
        for j in range(1, N+1):
            k = max(i-j, 0)
            bunbo += dp[N][j] * DP[k]
        DP[i] = bunbo / (1 - dp[N][0])

    print(DP[X])


if __name__ == "__main__":
    main()
