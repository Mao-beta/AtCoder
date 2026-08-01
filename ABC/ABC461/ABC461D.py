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
    H, W, K = NMI()
    S = [list(map(int, list(SI()))) for _ in range(H)]
    C = cum_2D(S)
    # print(*C, sep="\n")
    ans = 0
    X = [0] * (W+1)
    for h1 in range(H):
        for h2 in range(h1+1, H+1):
            for w in range(W + 1):
                X[w] = area_sum(C, h1, h2, 0, w)
            # print(h1, h2, X)
            l, r = 0, 0
            for w in range(W):
                k = X[w] + K
                while r < W+1 and k >= X[r]:
                    r += 1
                while l < W+1 and k > X[l]:
                    l += 1
                if l <= w:
                    l = w+1
                # print(h1, h2, w, k, l, r)
                if r-l >= 0:
                    ans += r-l
    print(ans)


if __name__ == "__main__":
    main()
