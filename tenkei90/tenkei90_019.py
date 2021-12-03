import sys
import math
from collections import deque
from functools import lru_cache

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    N = NI()
    A = NLI()
    # dp[l][r] は[l, r)での最小コスト
    # dp[0][2N]が答え
    INF = 10**10
    dp = [[INF]*(2*N+1) for _ in range(2*N+1)]

    for gap in range(0, 2*N+1, 2):
        for l in range(2*N+1 - gap):
            r = l + gap
            if l == r:
                dp[l][r] = 0
                continue
            dp[l][r] = min(dp[l][r], dp[l+1][r-1] + abs(A[l]-A[r-1]))
            for k in range(l+2, r, 2):
                dp[l][r] = min(dp[l][r], dp[l][k] + dp[k][r])

    print(dp[0][2*N])


if __name__ == "__main__":
    main()
