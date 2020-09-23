import sys
import math
from collections import defaultdict
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 998244353
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    N, K = NMI()
    LR = [NLI() for _ in range(K)]
    dp = [0] * (N*2+10)
    dp[1] = 1
    now = 0

    for i in range(1, N+1):
        now = (now + dp[i]) % MOD
        for l, r in LR:
            dp[i+l] = (dp[i+l] + now) % MOD
            dp[i+r+1] = (dp[i+r+1] - now) % MOD

    print(dp[N])


if __name__ == "__main__":
    main()