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
    N, K = NMI()
    XY = [NLI() for _ in range(N)]
    D = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(i+1, N):
            xi, yi = XY[i]
            xj, yj = XY[j]
            d = (xi-xj)**2 + (yi-yj)**2
            D[i][j] = d
            D[j][i] = d

    M = [0] * (1<<N)
    for case in range(1<<N):
        for i in range(N):
            if (case>>i) & 1:
                continue
            for j in range(N):
                if (case>>j) & 1 == 0:
                    continue
                M[case | (1<<i)] = max(M[case | (1<<i)], D[i][j])

    # dp[k][S] k個のグループで現在集合Sのときの距離最大値の最小値
    # 2つの配列を使いまわして次元を落とす dp[-1]が答え
    dp = M.copy()
    dp2 = [1<<60] * (1 << N)

    for k in range(2, K + 1):
        for case in range(1<<N):
            sub = case
            while sub:
                sub = case & (sub - 1)
                dp2[case] = min(dp2[case], max(dp[sub], M[case - sub]))
        dp, dp2 = dp2, dp

    print(dp[-1])


if __name__ == "__main__":
    main()
