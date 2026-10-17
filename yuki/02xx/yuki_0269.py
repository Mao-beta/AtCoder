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


def partition_number(N, K, mod):
    # Nを0以上のK個の整数の和として分割する O(NK)
    dp = [[0] * (K+1) for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(N+1):
        for j in range(1, K+1):
            # 分割に0を含む場合は元々分割が1個少なかったことにする
            dp[i][j] = dp[i][j-1]
            # 0を含まない場合は全部1以上なので全体から1ずつ引いたケースに帰着
            if i >= j:
                dp[i][j] += dp[i-j][j]
            dp[i][j] %= mod
    return dp[N][K]


def main():
    N, S, K = NMI()
    S -= (N-1)*K * N // 2
    if S < 0:
        print(0)
        return
    print(partition_number(S, N, MOD))


if __name__ == "__main__":
    main()
