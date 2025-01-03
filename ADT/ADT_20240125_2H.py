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
    N, M, K = NMI()
    # i回投げて現在地がjのときの確率
    dp = [[0]*(N+1) for _ in range(K+1)]
    dp[0][0] = 1
    inv = pow(M, -1, MOD99)
    for i in range(K):
        for j in range(N):
            for x in range(1, M+1):
                nj = j+x
                if nj > N:
                    nj = 2*N - nj
                dp[i+1][nj] += dp[i][j] * inv % MOD99
                dp[i+1][nj] %= MOD99

    ans = 0
    for i in range(K+1):
        ans += dp[i][N]
        ans %= MOD99
    print(ans)


if __name__ == "__main__":
    main()
