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


def make_grid(h, w, num): return [[int(num)] * w for _ in range(h)]


def main():
    N, L = NMI()
    X = NLI()
    T = NLI()
    Xf = [0] * (L+10)
    for x in X:
        Xf[x] = 1
    dp = [10**20] * (L + 10)
    dp[0] = 0

    def rec(point):
        if point < 0:
            return 10**20

        if dp[point] < 10**20:
            return dp[point]

        res = dp[point]
        if point >= 1:
            res = min(res, rec(point-1) + T[0] + T[2]*Xf[point])
        if point >= 2:
            res = min(res, rec(point-2) + T[0] + T[1] + T[2]*Xf[point])
        if point >= 4:
            res = min(res, rec(point-4) + T[0] + T[1]*3 + T[2]*Xf[point])
        dp[point] = res
        return res

    rec(L)
    print(min(dp[L], dp[L-1] + T[0]//2 + T[1]//2, dp[L-2] + T[0]//2 + T[1]*3//2,\
              dp[L-3] + T[0]//2 + T[1]*5//2))


if __name__ == "__main__":
    main()