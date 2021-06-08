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
    N = NI()
    T = NLI()
    sumT = sum(T)
    # dp[i][j] はi個めまで見て合計時間j分が作れるかどうか
    dp = [[0]*(sumT*2) for _ in range(N+1)]
    dp[0][0] = 1

    for i in range(N):
        for j in range(sumT):
            dp[i+1][j] |= dp[i][j]
            dp[i+1][j+T[i]] |= dp[i][j]

    ans = sumT
    for i, f in enumerate(dp[N]):
        if f:
            ans = min(ans, max(i, sumT - i))
    print(ans)


if __name__ == "__main__":
    main()
