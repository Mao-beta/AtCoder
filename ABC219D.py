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
    X, Y = NMI()
    AB = [NLI() for _ in range(N)]
    INF = 1<<60
    # dp[i][j][k] i個目までみてたこ焼きがj個、たいやきがkこあるときの最小値
    dp = [[[INF]*301 for _ in range(301)] for _ in range(N+1)]
    dp[0][0][0] = 0

    for i in range(N):
        a, b = AB[i]
        for j in range(301):
            for k in range(301):
                dp[i+1][j][k] = min(dp[i+1][j][k], dp[i][j][k])

                nj = min(300, j+a)
                nk = min(300, k+b)
                dp[i+1][nj][nk] = min(dp[i+1][nj][nk], dp[i][j][k] + 1)

    ans = INF
    for x in range(X, 301):
        for y in range(Y, 301):
            ans = min(ans, dp[N][x][y])

    print(ans if ans != INF else -1)


if __name__ == "__main__":
    main()
