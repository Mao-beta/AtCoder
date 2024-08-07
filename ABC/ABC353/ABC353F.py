import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.set_int_max_str_digits(10**6)
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


def main(K, Sx, Sy, Tx, Ty):

    if K == 1:
        return abs(Sx - Tx) + abs(Sy - Ty)

    ans = 10 ** 20

    if Sx // K == Tx // K and Sy // K == Ty // K:
        if (Sx // K + Sy // K) % 2 == 0:
            ans = min(ans, abs(Sx-Tx) + abs(Sy-Ty))
        else:
            return 0

    def B2B(px, py, qx, qy):
        # 大→大、Kで割った後の座標で
        if K > 2:
            return max(abs(px-qx), abs(py-qy)) * 2
        else:
            x = abs(px-qx)
            y = abs(py-qy)
            if x < y:
                x, y = y, x
            # print(px, py, qx, qy, x, y)
            return 2*y + 3*(x-y) // 2

    SXY = []
    TXY = []

    if (Sx // K + Sy // K) % 2 == 0:
        SXY.append([Sx // K - 1, Sy // K, Sx % K + 1])
        SXY.append([Sx // K + 1, Sy // K, K - Sx % K])
        SXY.append([Sx // K, Sy // K - 1, Sy % K + 1])
        SXY.append([Sx // K, Sy // K + 1, K - Sy % K])
    else:
        SXY.append([Sx // K, Sy // K, 0])

    if (Tx // K + Ty // K) % 2 == 0:
        TXY.append([Tx // K - 1, Ty // K, Tx % K + 1])
        TXY.append([Tx // K + 1, Ty // K, K - Tx % K])
        TXY.append([Tx // K, Ty // K - 1, Ty % K + 1])
        TXY.append([Tx // K, Ty // K + 1, K - Ty % K])
    else:
        TXY.append([Tx // K, Ty // K, 0])

    for px, py, p in SXY:
        for qx, qy, q in TXY:
            tmp = p + q + B2B(px, py, qx, qy)
            # print(px, py, qx, qy, p, q, tmp)
            ans = min(ans, tmp)
    return ans


if __name__ == "__main__":
    K = NI()
    Sx, Sy = NMI()
    Tx, Ty = NMI()
    print(main(K, Sx, Sy, Tx, Ty))
    #
    # K = 2
    # for Sx in range(K+1):
    #     for Sy in range(K + 1):
    #         for Tx in range(K + 1):
    #             for Ty in range(K + 1):
    #                 res = main(K, Sx, Sy, Tx, Ty)
    #                 print(K, Sx, Sy, Tx, Ty, res)
