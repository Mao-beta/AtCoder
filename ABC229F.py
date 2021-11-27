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


def main():
    N = NI()
    A = NLI()
    B = NLI()
    INF = 10**20
    S = sum(A) + sum(B)
    ans = INF

    # dp[i][j][k] 頂点0は赤　頂点iまで色を決めて、iが赤のときj=0, 青のときj=1
    # 頂点1がrのときk=0, 青のときk=1
    dp = [[[0]*2 for _ in range(2)] for _ in range(N+1)]
    dp[1][0][0] = 0
    dp[1][0][1] = -INF
    dp[1][1][1] = A[0]
    dp[1][1][0] = -INF

    for i in range(1, N):
        for j in range(2):
            for k in range(2):
                dp[i+1][0][k] = max(dp[i+1][0][k],
                                 dp[i][0][k],
                                 dp[i][1][k] + B[i-1])
                dp[i+1][1][k] = max(dp[i+1][1][k],
                                 dp[i][0][k] + A[i] + B[i-1],
                                 dp[i][1][k] + A[i])

    #print(S)
    for j in range(2):
        for k in range(2):
            res = dp[N][j][k]
            if j != k:
                res += B[-1]
            #print(j, k, res)
            ans = min(ans, S - res)

    #print(*dp, sep="\n")
    print(ans)


if __name__ == "__main__":
    main()
