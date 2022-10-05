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


def compress(S):
    """ 座標圧縮 """

    S = set(S)
    zipped, unzipped = {}, {}
    for i, a in enumerate(sorted(S)):
        zipped[a] = i
        unzipped[i] = a
    return zipped, unzipped


def main():
    W, H = NMI()
    N = NI()
    XY = [NLI() for _ in range(N)]

    X = [0, W+1]
    Y = [0, H+1]
    for x, y in XY:
        X.append(x)
        Y.append(y)

    ZX, UZX = compress(X)
    ZY, UZY = compress(Y)

    XN = len(ZX)
    YN = len(ZY)

    # print(ZX)

    # dp[(xl, xr, yl, yr)]
    # 領域[xl, xr), [yl, yr) における最大
    dp = defaultdict(lambda: -1)


    def rec(xl, xr, yl, yr):

        if xr - xl <= 1 or yr - yl <= 1:
            dp[(xl, xr, yl, yr)] = 0
            return 0

        # print(xl, xr, yl, yr)

        w = UZX[xr] - UZX[xl] - 1
        h = UZY[yr] - UZY[yl] - 1
        # print(w, h)

        res = 0
        for x, y in XY:
            zx = ZX[x]
            zy = ZY[y]

            if not (xl < zx < xr) or not (yl < zy < yr):
                continue

            # print(zx, zy)

            ld = dp[(xl, zx, yl, zy)]
            if ld == -1:
                ld = rec(xl, zx, yl, zy)

            lu = dp[(xl, zx, zy, yr)]
            if lu == -1:
                lu = rec(xl, zx, zy, yr)

            rd = dp[(zx, xr, yl, zy)]
            if rd == -1:
                rd = rec(zx, xr, yl, zy)

            ru = dp[(zx, xr, zy, yr)]
            if ru == -1:
                ru = rec(zx, xr, zy, yr)

            tmp = ld + lu + rd + ru
            tmp += w + h - 1

            res = max(res, tmp)

        dp[(xl, xr, yl, yr)] = res
        return res


    rec(0, XN-1, 0, YN-1)
    print(dp[(0, XN-1, 0, YN-1)])


if __name__ == "__main__":
    main()
