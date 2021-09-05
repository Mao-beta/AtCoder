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
    H, W, C = NMI()
    A = [NLI() for _ in range(H)]

    def solve(A):
        INF = 1<<60
        # dp[i][j]: (i, j)を含む左上の領域のどこかで駅を立て、線路を引いてきているときの最小コスト
        # X[i][j]: (i, j)に駅を立てて切り上げるときの最小コスト
        # これは真左か真上のdpの値+Aij+Cの小さいほう
        dp = [[INF]*W for _ in range(H)]
        X = [[INF]*W for _ in range(H)]
        dp[0][0] = A[0][0]
        for h in range(H):
            for w in range(W):
                dp[h][w] = min(dp[h][w], A[h][w])
                if h != 0:
                    dp[h][w] = min(dp[h][w], dp[h-1][w] + C)
                if w != 0:
                    dp[h][w] = min(dp[h][w], dp[h][w-1] + C)

                if h != 0:
                    X[h][w] = min(X[h][w], dp[h-1][w] + C + A[h][w])
                if w != 0:
                    X[h][w] = min(X[h][w], dp[h][w-1] + C + A[h][w])

        res = INF
        for row in X:
            res = min(res, min(row))
        return res

    ans = solve(A)
    A = [row[::-1] for row in A]

    ans = min(ans, solve(A))
    print(ans)


if __name__ == "__main__":
    main()
