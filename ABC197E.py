import sys
import math
from collections import defaultdict

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def make_grid(h, w, num): return [[int(num)] * w for _ in range(h)]


def main():
    N = NI()
    B = [NLI() for _ in range(N)]
    B = sorted(B, key=lambda x: (x[1], x[0]))

    D = [[] for _ in range(N+1)]
    for x, c in B:
        D[c].append(x)

    maxD = []
    minD = []
    for c, d in enumerate(D):
        if d:
            maxD.append(max(d))
            minD.append(min(d))

    n = len(maxD)
    # i個まで見て現在地が最大値側（j=1）か最小値側か(j=0)のときの時間の最小値
    dp = [[0]*2 for _ in range(n+1)]
    prevM = 0
    prevm = 0
    for i, (M, m) in enumerate(zip(maxD, minD)):
        gapMM = abs(M - prevM)
        gapMm = abs(M - prevm)
        gapmM = abs(m - prevM)
        gapmm = abs(m - prevm)
        dp[i+1][0] = min(dp[i][0]+gapMm+M-m, dp[i][1]+gapMM+M-m)
        dp[i+1][1] = min(dp[i][0]+gapmm+M-m, dp[i][1]+gapmM+M-m)
        prevm = m
        prevM = M

    print(min(dp[n][0]+abs(prevm), dp[n][1]+abs(prevM)))


if __name__ == "__main__":
    main()
