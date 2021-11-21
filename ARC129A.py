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
    N, L, R = NMI()
    K = 61

    # 上からi bit目まで確定　j=1でxorがN未満 2でNより大確定 k=1でR未満確定 の個数
    dp = [[[0]*2 for _ in range(2)] for _ in range(K+1)]
    dp[0][0][0] = 1
    N_str = bin(N)[2:].zfill(K)
    R_str = bin(R)[2:].zfill(K)

    for i in range(K):
        for j in range(2):
            d = int(N_str[i])

            for k in range(2):
                dr = int(R_str[i])
                lim = 2 if k == 1 else dr+1
                # 次の数字
                for x in range(lim):
                    if k == 1:
                        nk = 1
                    else:
                        if x == dr:
                            nk = 0
                        else:
                            nk = 1

                    if j == 1:
                        nj = 1
                    else:
                        if x^d < d:
                            nj = 1
                        elif x^d == d:
                            nj = 0
                        else:
                            continue

                    dp[i+1][nj][nk] += dp[i][j][k]

    ans = sum(dp[K][1])

    # 上からi bit目まで確定　j=1でxorがN未満確定 k=1でL未満確定 の個数
    dp = [[[0]*2 for _ in range(2)] for _ in range(K+1)]
    dp[0][0][0] = 1
    N_str = bin(N)[2:].zfill(K)
    L_str = bin(L-1)[2:].zfill(K)

    for i in range(K):
        for j in range(2):
            d = int(N_str[i])

            for k in range(2):
                dr = int(L_str[i])
                lim = 2 if k == 1 else dr+1
                # 次の数字
                for x in range(lim):
                    if k == 1:
                        nk = 1
                    else:
                        if x == dr:
                            nk = 0
                        else:
                            nk = 1

                    if j == 1:
                        nj = 1
                    else:
                        if x^d < d:
                            nj = 1
                        elif x^d == d:
                            nj = 0
                        else:
                            continue

                    dp[i+1][nj][nk] += dp[i][j][k]

    ans -= sum(dp[K][1])
    print(ans)


if __name__ == "__main__":
    main()
