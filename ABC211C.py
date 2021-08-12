import sys
import math
from collections import defaultdict
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    S = SI()
    N = len(S)
    C = "chokudai"
    M = len(C)
    # Sのi文字目まで見て"chokudai"のj文字まで線を引いている通りの数
    dp = [[0]*(M+1) for _ in range(N+1)]
    dp[0][0] = 1

    # もらうDP
    for i in range(1, N+1):
        s = S[i-1]
        for j in range(M+1):
            dp[i][j] += dp[i-1][j]
            dp[i][j] %= MOD
            if j == 0: continue
            c = C[j-1]
            if s == c:
                dp[i][j] += dp[i-1][j-1]
                dp[i][j] %= MOD

    print(dp[-1][-1])


if __name__ == "__main__":
    main()
