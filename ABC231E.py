import sys
import math
from collections import deque

sys.setrecursionlimit(100000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()

INF = 10**20

def main():
    N, X = NMI()
    A = NLI() + [INF]
    # 下からi桁めまで払った jは次の桁でoverかどうか
    dp = [[INF]*2 for _ in range(N+1)]
    dp[0][0] = 0

    for i in range(N):
        a = A[i]

        #くりあがりなし -> なし
        b = X // a * a % A[i+1] // a
        dp[i+1][0] = min(dp[i+1][0], dp[i][0] + b)

        #くりあがりなし -> あり
        b = X // a * a % A[i+1] // a
        g = A[i+1] // a
        dp[i+1][1] = min(dp[i+1][1], dp[i][0] + g - b)

        #くりあがりあり -> なし
        b = X // a * a % A[i+1] // a + 1
        dp[i+1][0] = min(dp[i+1][0], dp[i][1] + b)

        #くりあがりあり -> あり
        b = X // a * a % A[i+1] // a + 1
        g = A[i+1] // a
        dp[i+1][1] = min(dp[i+1][1], dp[i][1] + g - b)

    ans = min(dp[N][0], dp[N][1] + 1)
    print(ans)


if __name__ == "__main__":
    main()
