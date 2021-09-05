import sys
import math
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 998244353
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    N, M = NMI()
    # dp[i][k]: 前からi人を空でないk個のグループに分ける通りの数
    dp = [[0]*(N+1) for _ in range(N+1)]
    dp[0][0] = 1

    for i in range(1, N+1):
        for k in range(1, N+1):
            dp[i][k] += dp[i-1][k-1]
            dp[i][k] += dp[i-1][k] * max(0, (k - (i-1)//M)) % MOD
            dp[i][k] %= MOD

    print(*dp[N][1:], sep="\n")


if __name__ == "__main__":
    main()
