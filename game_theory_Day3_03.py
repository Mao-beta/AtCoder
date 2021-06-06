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


def cum_2D(_A):
    """
    2次元リストAの累積和
    """
    from copy import deepcopy

    A = deepcopy(_A)
    H = len(A)
    W = len(A[0])
    for h in range(H):
        for w in range(W-1):
            A[h][w+1] += A[h][w]
    for w in range(W):
        for h in range(H-1):
            A[h+1][w] += A[h][w]

    return A


def area_sum(cum, hl, hr, wl, wr):
    """
    2次元累積和の行列cum（左と上は0）から、元の行列の[hl:hr, wl:wr]の範囲で和をとる
    """
    return cum[hr][wr] - cum[hl][wr] - cum[hr][wl] + cum[hl][wl]


def main():
    T = NI()
    not_primes = {1, 4, 6, 8, 9}
    for _ in range(T):
        N = NI()

        # 合成数を1とする盤面構築
        grid = [[0]*(N+1)]
        for h in range(N):
            row = NLI()
            row = [0] + [1 if x in not_primes else 0 for x in row]
            grid.append(row)

        Cum = cum_2D(grid)

        if N == 1:
            print("Second")
            continue

        # dp[hl][hr][wl][wr] は hl:hr, wl:wr の領域のGrundy数
        # それぞれ0以上N以下
        dp = [[[[0]*(N+1) for _ in range(N+1)] for _ in range(N+1)] for _ in range(N+1)]

        # hr-hl==1 かつ wr-wl==1 のときdp==0
        # それ以外のとき、あり得る分割を全部試す
        # ある分割で、分割後の二つのGrundy数のXORをとる
        # それらのMexが元の状態のGrundy数
        for hgap_wgap in range(2, N*2+1):
            for wgap in range(1, N+1):
                hgap = hgap_wgap - wgap
                if not (1 <= hgap <= N): continue
                for hl in range(0, N+1 - hgap):
                    for wl in range(0, N+1 - wgap):
                        hr = hl + hgap
                        wr = wl + wgap
                        area = area_sum(Cum, hl, hr, wl, wr)
                        if hgap == wgap == 1:
                            area = 0
                        if area == 0:
                            dp[hl][hr][wl][wr] = 0
                            continue

                        S = set()

                        for hi in range(hl+1, hr):
                            g_l = dp[hl][hi][wl][wr]
                            g_r = dp[hi][hr][wl][wr]
                            S.add(g_l ^ g_r)

                        for wi in range(wl+1, wr):
                            g_l = dp[hl][hr][wl][wi]
                            g_r = dp[hl][hr][wi][wr]
                            S.add(g_l ^ g_r)

                        for g in range(100):
                            if g not in S:
                                dp[hl][hr][wl][wr] = g
                                break

        print("First" if dp[0][N][0][N] else "Second")


if __name__ == "__main__":
    main()
