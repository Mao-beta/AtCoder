import sys
import math
from collections import defaultdict
from collections import deque

sys.setrecursionlimit(100000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    L, R = NMI()

    L = bin(L)[2:]
    R = bin(R)[2:]

    K = len(R)
    L = L.zfill(K)

    # dp[i][j][k][l]
    # i桁まで確定 j:x超過フラグ k:y未満フラグ l:最上位桁(1, 1)が出たか
    dp = [[[[0]*2 for _ in range(2)]
           for _ in range(2)]for _ in range(K+1)]
    dp[0][0][0][0] = 1

    for i in range(K):
        for j in range(2):
            for k in range(2):
                for l in range(2):
                    if dp[i][j][k][l] == 0: continue

                    xlim = 0 if j == 1 else int(L[i])
                    ylim = 1 if k == 1 else int(R[i])

                    for x in range(xlim, 2):
                        for y in range(ylim+1):
                            nj = j | (x > xlim)
                            nk = k | (y < ylim)
                            nl = l

                            # 最上位桁が確定していないときは(1, 1)でnl==1へ
                            # (0, 0)でnl==0へ寄与 それ以外はダメ
                            if l == 0:
                                if x == 1 and y == 1:
                                    nl = 1
                                elif x == 0 and y == 0:
                                    nl = 0
                                else:
                                    continue

                            # (1, 0)は条件を満たさないのでダメ
                            if x == 1 and y == 0: continue

                            dp[i+1][nj][nk][nl] += dp[i][j][k][l]
                            dp[i+1][nj][nk][nl] %= MOD

    # K桁まで確定して最上位桁のあるものの総数が答え
    ans = 0
    for j in range(2):
        for k in range(2):
            ans += dp[K][j][k][1]

    print(ans % MOD)


if __name__ == "__main__":
    main()
