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

    if A[0][0] == 1:
        for h in range(H):
            for w in range(W):
                A[h][w] ^= 1

    INF = 10**18
    # dp[s][h][w]: h, wについて、反転状態がs(00-11)のときの最小コスト
    dp = [[[INF]*W for _ in range(H)] for _ in range(4)]
    dp[0][0][0] = 0
    dp[3][0][0] = HC[0] + WC[0]

    # 全部0にしたい
    target = 0
    for h in range(H):
        for w in range(W):
            for s in range(4):
                if dp[s][h][w] == INF: continue
                for nh, nw in zip([h, h+1], [w+1, w]):
                    if nh >= H or nw >= W: continue
                    # 次が欲しい色のときは変えない
                    a = A[nh][nw]
                    if (s & 1):
                        a ^= 1
                    if (s & 2):
                        a ^= 1

                    if A[nh][nw] == a:
                        # 右
                        if h == nh:
                            ns = s & 1
                            dp[ns][nh][nw] = min(dp[ns][nh][nw], dp[s][h][w])
                        # 下
                        else:
                            ns = s & 2
                            dp[ns][nh][nw] = min(dp[ns][nh][nw], dp[s][h][w])

                    # 次が違う色のときは変える
                    else:
                        # 右
                        if h == nh:
                            ns = (s & 1) | 2
                            dp[ns][nh][nw] = min(dp[ns][nh][nw], dp[s][h][w] + WC[nw])
                        # 下
                        else:
                            ns = (s & 2) | 1
                            dp[ns][nh][nw] = min(dp[ns][nh][nw], dp[s][h][w] + HC[nh])

                print(h, w, s)
                print(*dp[s], sep="\n")

    print(*dp, sep="\n")

    ans = INF

    for s in range(4):
        ans = min(ans, dp[s][-1][-1])


    dp = [[[INF] * W for _ in range(H)] for _ in range(4)]
    dp[1][0][0] = HC[0]
    dp[2][0][0] = WC[0]

    # 全部1にしたい
    target = 1
    for h in range(H):
        for w in range(W):
            for s in range(4):
                if dp[s][h][w] == INF: continue
                for nh, nw in zip([h, h + 1], [w + 1, w]):
                    if nh >= H or nw >= W: continue
                    # 次が欲しい色のときは変えない
                    a = A[nh][nw]
                    if (s & 1):
                        a ^= 1
                    if (s & 2):
                        a ^= 1

                    if A[nh][nw] == a:
                        # 右
                        if h == nh:
                            ns = s & 1
                            dp[ns][nh][nw] = min(dp[ns][nh][nw], dp[s][h][w])
                        # 下
                        else:
                            ns = s & 2
                            dp[ns][nh][nw] = min(dp[ns][nh][nw], dp[s][h][w])

                    # 次が違う色のときは変える
                    else:
                        # 右
                        if h == nh:
                            ns = (s & 1) | 2
                            dp[ns][nh][nw] = min(dp[ns][nh][nw], dp[s][h][w] + WC[nw])
                        # 下
                        else:
                            ns = (s & 2) | 1
                            dp[ns][nh][nw] = min(dp[ns][nh][nw], dp[s][h][w] + HC[nh])

    for s in range(4):
        ans = min(ans, dp[s][-1][-1])
    print()
    print(*dp, sep="\n")
    print(ans)


if __name__ == "__main__":
    main()
