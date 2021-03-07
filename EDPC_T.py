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
    N = NI()
    S = SI()

    # dp i番目の数字まで決定し、それより大きいものがj個
    dp = [[0] * N for _ in range(N+1)]
    for j in range(N):
        dp[1][j] = 1

    for i in range(2, N+1):
        cum = [0] + list(accumulate(dp[i-1]))
        s = S[i-2]
        for j in range(N-i+1):
            if s == "<":
                dp[i][j] = (cum[N-i+2] - cum[j+1]) % MOD
            else:
                dp[i][j] = (cum[j+1] - cum[0]) % MOD

    print(dp[N][0])


if __name__ == "__main__":
    main()
