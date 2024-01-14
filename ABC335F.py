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
    sq = 500
    # dp[i]: i個見たときの場合の数（aが大きいときは直接配るdpで加算）
    dp = [0] * (N+1)
    dp[0] = 1
    # dp2[a][r]: aで割ってr余るときiに対する累積加算分 a<=sq, r<sq
    dp2 = [[0]*sq for _ in range(sq+1)]

    # 0-index
    for i, a in enumerate(A):
        # dp2をdpに反映
        # 左側の各a(<=sq)で飛んできてるぶんを足す
        for aa in range(1, sq+1):
            dp[i] += dp2[aa][i%aa]
            dp[i] %= MOD99

        if a > sq:
            for ni in range(i+a, N, a):
                dp[ni] += dp[i]
                dp[ni] %= MOD99
        else:
            dp2[a][i%a] += dp[i]
            dp2[a][i%a] %= MOD99

    print(sum(dp) % MOD99)


if __name__ == "__main__":
    main()
