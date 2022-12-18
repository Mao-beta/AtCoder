import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

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
    H, W, N, h, w = NMI()
    A = [tuple(NMI()) for _ in range(H)]

    ans = [[N]*(W-w+1) for _ in range(H-h+1)]

    for t in range(1, N + 1):
        At = [tuple(int(x == t) for x in row) for row in A]
        C = cum_2D(At)

        for hl in range(H-h+1):
            for wl in range(W-w+1):
                hr = hl + h
                wr = wl + w

                total = C[-1][-1]
                b = area_sum(C, hl, hr, wl, wr)
                if total == b:
                    ans[hl][wl] -= 1

    for row in ans:
        print(" ".join(map(str, row)))


if __name__ == "__main__":
    main()
