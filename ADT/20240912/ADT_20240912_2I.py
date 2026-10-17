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


def cum_2D(A):
    """
    2次元リストAの累積和（左と上は0になる）
    """
    H = len(A)
    W = len(A[0])
    C = [[0]*(W+1) for _ in range(H+1)]

    for h in range(H):
        cw = 0
        for w in range(W):
            cw += A[h][w]
            if h == 0 and w == 0:
                C[h+1][w+1] = A[h][w]
            elif h == 0:
                C[h+1][w+1] = A[h][w] + C[h+1][w]
            elif w == 0:
                C[h+1][w+1] = A[h][w] + C[h][w+1]
            else:
                C[h+1][w+1] = C[h][w+1] + cw

    return C


def area_sum(cum, hl, hr, wl, wr):
    """
    2次元累積和の行列cum（左と上は0）から、元の行列の[hl:hr, wl:wr]の範囲で和をとる
    """
    return cum[hr][wr] - cum[hl][wr] - cum[hr][wl] + cum[hl][wl]


def main():
    N, M = NMI()
    A = EI(N)

    def calc(A):
        res = 0
        cum = cum_2D(A)
        areas = [[0]*(N-M+1) for _ in range(N-M+1)]
        for h in range(N-M+1):
            for w in range(N-M+1):
                areas[h][w] = area_sum(cum, h, h+M, w, w+M)
        # print(*areas, sep="\n")
        lows = [max(areas[h]) for h in range(N-M+1)]

        for h in range(1, N-M):
            for h2 in range(h+1, N-M):
                res = max(res, max(lows[:h]) + max(lows[h:h2]) + max(lows[h2:]))
        # print(res)

        for h in range(N-M, 0, -1):
            lows[h-1] = max(lows[h-1], lows[h])
        LUs = [row[:] for row in areas]
        for h in range(N-M+1):
            for w in range(N-M):
                LUs[h][w+1] = max(LUs[h][w+1], LUs[h][w])
        for w in range(N-M+1):
            for h in range(N-M):
                LUs[h+1][w] = max(LUs[h+1][w], LUs[h][w])

        RUs = [row[:] for row in areas]
        for h in range(N-M+1):
            for w in range(N-M, 0, -1):
                RUs[h][w-1] = max(RUs[h][w-1], RUs[h][w])
        for w in range(N-M+1):
            for h in range(N-M):
                RUs[h+1][w] = max(RUs[h+1][w], RUs[h][w])
        print("LU")
        print(*LUs, sep="\n")
        print("RU")
        print(*RUs, sep="\n")
        print("lows")
        print(*lows, sep="\n")
        for hidx in range(1, N-M):
            for widx in range(1, N-M):
                if 0 <= widx-1+M < N-M+1 and hidx+M < N-M+1:
                    res = max(res, lows[hidx+M] + LUs[hidx-1][widx-1] + RUs[hidx-1][widx-1+M])
                    print(hidx, widx, res)
        return res

    ans = 0
    ans = max(ans, calc(A))
    A = A[::-1]
    ans = max(ans, calc(A))
    A = [a for a in zip(*A)]
    ans = max(ans, calc(A))
    A = A[::-1]
    ans = max(ans, calc(A))
    print(ans)



if __name__ == "__main__":
    main()
