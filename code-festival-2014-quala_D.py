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
    A, K = NMI()
    A = str(A)
    L = len(A)

    INF = 10**20

    # A以下
    # dp[i][j][z][b] i桁まで確定 jは未満フラグ
    # zはleading-zero bは使った数の集合(1<<10)
    dp = [[[[INF]*(1<<10) for _ in range(2)]
           for _ in range(2)] for _ in range(L+1)]
    dp[0][0][0][0] = int(A)

    for i in range(L):
        for j in range(2):
            for z in range(2):
                for b in range(1<<10):
                    lim = 9 if j == 1 else int(A[i])
                    for x in range(lim+1):
                        nj = j | (x < lim)
                        nz = z & (x == 0)
                        nb = b
                        if nz == 0:
                            nb = b | (1 << x)

                        dp[i+1][nj][nz][nb] = min(dp[i+1][nj][nz][nb],
                                                  dp[i][j][z][b] - x * pow(10, L-i-1))

    ans = INF
    for j in range(2):
        for z in range(2):
            for b in range(1<<10):
                if bin(b).count("1") > K:
                    continue
                if dp[L][j][z][b] < 0: continue
                ans = min(ans, dp[L][j][z][b])


    # A以上
    # dp[i][j][z][b] i桁まで確定 jは超過フラグ
    # zはleading-zero bは使った数の集合(1<<10)
    dp = [[[[INF]*(1<<10) for _ in range(2)]
           for _ in range(2)] for _ in range(L+1)]
    dp[0][0][0][0] = -int(A)

    for i in range(L):
        for j in range(2):
            for z in range(2):
                for b in range(1<<10):
                    lim = 0 if j == 1 else int(A[i])
                    for x in range(lim, 10):
                        nj = j | (x > lim)
                        nz = z & (x == 0)
                        nb = b
                        if nz == 0:
                            nb = b | (1 << x)

                        dp[i+1][nj][nz][nb] = min(dp[i+1][nj][nz][nb],
                                                  dp[i][j][z][b] + x * pow(10, L-i-1))

    for j in range(2):
        for z in range(2):
            for b in range(1<<10):
                if bin(b).count("1") > K:
                    continue
                if dp[L][j][z][b] < 0: continue
                ans = min(ans, dp[L][j][z][b])
    print(ans)


if __name__ == "__main__":
    main()
