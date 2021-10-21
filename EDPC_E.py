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
    N, W = NMI()
    WV = [NLI() for _ in range(N)]

    # dp[i][j] i番目まで見て価値がjのときの重さの最小値
    # dp[i]を上から見てはじめてW以下になるときのjが答え
    INF = 10**20
    MV = 10**5
    dp = [[INF]*(MV+1) for _ in range(N+1)]
    dp[0][0] = 0

    for i in range(N):
        w, v = WV[i]
        for j in range(MV+1):
            dp[i+1][j] = min(dp[i+1][j], dp[i][j])

            if j+v <= MV:
                dp[i+1][j+v] = min(dp[i+1][j+v], dp[i][j] + w)

    for j in range(MV, -1, -1):
        now = dp[N][j]
        if now <= W:
            print(j)
            exit()


if __name__ == "__main__":
    main()
