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
    N, M, K = NMI()
    B = [NLI() for _ in range(M)]
    B = [[u-1, v-1] for u, v in B]
    dp = [0] * N
    dp[0] = 1

    for k in range(K):
        s = sum(dp) % MOD
        ndp = [s] * N
        for i, d in enumerate(dp):
            ndp[i] -= d
        for u, v in B:
            ndp[u] -= dp[v]
            ndp[v] -= dp[u]
        dp = [nd % MOD for nd in ndp]

    print(dp[0])


if __name__ == "__main__":
    main()
