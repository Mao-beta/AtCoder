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
EI = lambda m: [NLI() for _ in range(m)]


def bitonic_TSP(N: int, XY: list) -> float:
    """
    二次元平面内のN頂点について、
    左端→右端の一方向のパス + 右端→左端の一方向のパス
    (要は行って帰っての1周だけ)で全点通過するときの最短経路長 O(N^2)
    xが互いに異なる場合のみverified
    """
    import math

    INF = float("inf")
    XY.sort()
    # dp[i]: 遅いほうの点がiのときの最短距離
    dp = [INF] * N
    # 1個めだけ処理
    x0, y0 = XY[0]
    x1, y1 = XY[1]
    dp[0] = math.sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2)

    for i, (xi, yi) in enumerate(XY):
        # x2, y2からはじめる
        if i <= 1:
            continue

        dp2 = [INF] * N
        for j in range(i):
            if dp[j] == INF:
                continue

            # i-1番目の点
            xi_, yi_ = XY[i - 1]
            # j番目の点
            xj, yj = XY[j]

            # i-1につなげる
            dp2[j] = min(dp2[j], dp[j] + math.sqrt((xi - xi_) ** 2 + (yi - yi_) ** 2))
            # jにつなげる
            dp2[i - 1] = min(dp2[i - 1], dp[j] + math.sqrt((xi - xj) ** 2 + (yi - yj) ** 2))

        dp, dp2 = dp2, dp

    ans = INF
    for i, d in enumerate(dp):
        xn, yn = XY[-1]
        xi, yi = XY[i]
        ans = min(ans, d + math.sqrt((xi - xn) ** 2 + (yi - yn) ** 2))

    return ans


def main():
    N = NI()
    XY = EI(N)

    print(bitonic_TSP(N, XY))


if __name__ == "__main__":
    main()
