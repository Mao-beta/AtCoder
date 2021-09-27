import sys
import math
from collections import deque

sys.setrecursionlimit(100000)
MOD = 998244353
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    N = NI()
    A = NLI()
    dp = [[0]*10 for _ in range(N)]
    dp[0][A[0]] = 1
    for i in range(N-1):
        for al in range(10):
            ar = A[i+1]
            dp[i+1][(al+ar) % 10] += dp[i][al]
            dp[i+1][(al*ar) % 10] += dp[i][al]
            dp[i+1][(al+ar) % 10] %= MOD
            dp[i+1][(al*ar) % 10] %= MOD

    for k in range(10):
        print(dp[N-1][k])


if __name__ == "__main__":
    main()
