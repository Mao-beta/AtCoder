import sys
import math
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    N, L = NMI()
    dp = [0] * (N+1)
    dp[0] = 1
    for i in range(1, N+1):
        dp[i] += dp[i-1]
        if i >= L:
            dp[i] += dp[i-L]
        dp[i] %= MOD

    print(dp[N])


if __name__ == "__main__":
    main()
