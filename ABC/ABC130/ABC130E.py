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
    N, M = NMI()
    S = NLI()
    T = NLI()

    # dp[i][j]はSのi番目、Tのj番目まで見たときの共通部分列の個数(1-index)
    dp = [[0]*(M+1) for _ in range(N+1)]

    for i in range(N+1):
        for j in range(M+1):
            if i == 0 or j == 0:
                dp[i][j] = 1
                continue
            # i-1, jからS[i]を取らない
            dp[i][j] += dp[i-1][j]
            # i, j-1からT[j]を取らない
            dp[i][j] += dp[i][j-1]
            # 上記の重複分を除く
            dp[i][j] -= dp[i-1][j-1]
            # S[i-1]==T[j-1]のとき、i-1, j-1からS[i-1], T[j-1]を取る
            if S[i-1] == T[j-1]:
                dp[i][j] += dp[i-1][j-1]
            dp[i][j] %= MOD

    print(dp[-1][-1])


if __name__ == "__main__":
    main()
