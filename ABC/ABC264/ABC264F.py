import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
MOD99 = 998244353

input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()
SMI = lambda: input().split()
SLI = lambda: list(SMI())


def main():
    H, W = NMI()
    HC = NLI()
    WC = NLI()
    A = [list(map(int, SI())) for _ in range(H)]

    DH = [0, 1]
    DW = [1, 0]

    INF = 10**15
    # dp[s][h*W+w]: h, wについて、反転状態がs(00-11)のときの最小コスト
    dp = [[INF]*(H*W) for _ in range(4)]
    dp[0][0] = 0
    dp[3][0] = HC[0] + WC[0]

    # 全部0にしたい
    target = A[0][0]
    for h in range(H):
        for w in range(W):
            i = h * W + w
            for s in range(4):
                if dp[s][i] == INF: continue
                for dh, dw in zip(DH, DW):
                    nh, nw = h+dh, w+dw
                    if nh >= H or nw >= W: continue
                    ni = nh * W + nw
                    a = A[nh][nw]
                    # 右
                    if h == nh:
                        if s & 1:
                            a ^= 1
                        # 欲しい色
                        if target == a:
                            ns = s & 1
                            dp[ns][ni] = min(dp[ns][ni], dp[s][i])
                        # 欲しい色でない
                        else:
                            ns = (s & 1) | 2
                            dp[ns][ni] = min(dp[ns][ni], dp[s][i] + WC[nw])

                    # 下
                    else:
                        if s & 2:
                            a ^= 1
                        # 欲しい色
                        if target == a:
                            ns = s & 2
                            dp[ns][ni] = min(dp[ns][ni], dp[s][i])
                        # 欲しい色でない
                        else:
                            ns = (s & 2) | 1
                            dp[ns][ni] = min(dp[ns][ni], dp[s][i] + HC[nh])


    ans = INF

    for s in range(4):
        ans = min(ans, dp[s][-1])


    dp = [[INF]*(H*W) for _ in range(4)]
    dp[1][0] = HC[0]
    dp[2][0] = WC[0]

    # 全部1にしたい
    target = A[0][0] ^ 1
    for h in range(H):
        for w in range(W):
            i = h * W + w
            for s in range(4):
                if dp[s][i] == INF: continue
                for dh, dw in zip(DH, DW):
                    nh, nw = h + dh, w + dw
                    if nh >= H or nw >= W: continue
                    ni = nh * W + nw
                    a = A[nh][nw]
                    # 右
                    if h == nh:
                        if s & 1:
                            a ^= 1
                        # 欲しい色
                        if target == a:
                            ns = s & 1
                            dp[ns][ni] = min(dp[ns][ni], dp[s][i])
                        # 欲しい色でない
                        else:
                            ns = (s & 1) | 2
                            dp[ns][ni] = min(dp[ns][ni], dp[s][i] + WC[nw])

                    # 下
                    else:
                        if s & 2:
                            a ^= 1
                        # 欲しい色
                        if target == a:
                            ns = s & 2
                            dp[ns][ni] = min(dp[ns][ni], dp[s][i])
                        # 欲しい色でない
                        else:
                            ns = (s & 2) | 1
                            dp[ns][ni] = min(dp[ns][ni], dp[s][i] + HC[nh])

    for s in range(4):
        ans = min(ans, dp[s][-1])

    print(ans)


if __name__ == "__main__":
    main()
