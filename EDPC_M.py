import sys
import math
from collections import defaultdict
from collections import deque
from itertools import accumulate

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    N, K = NMI()
    A = NLI()

    # dp[i][j] i番目まで見てj個まで配ったときの場合の数
    dp = [[0]*(K+1) for _ in range(N+1)]
    dp[0][0] = 1

    for i in range(N):
        cum = [0] + list(accumulate(dp[i]))
        for k in range(K+1):
            r = k+1
            l = max(0, k-A[i])
            dp[i+1][k] = (cum[r] - cum[l]) % MOD

    print(dp[N][K])


if __name__ == "__main__":
    main()
