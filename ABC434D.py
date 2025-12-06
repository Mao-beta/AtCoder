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
    N = NI()
    UDLR = EI(N)
    B = 2002
    A = [[0]*B for _ in range(B)]
    for u, d, l, r in UDLR:
        A[u-1][l-1] += 1
        A[d][l-1] -= 1
        A[u-1][r] -= 1
        A[d][r] += 1
    C = cum_2D(A)
    # print(*C, sep="\n")
    nonzero = 0
    for i, row in enumerate(C):
        if i == 0:
            C[0] = row
            continue
        z = row.count(0)
        nonzero += B+1 - z
        row = [1 if c == 1 else 0 for c in row]
        C[i] = row
    zero = 2000**2 - nonzero
    # print(zero)
    # print()
    # print(*C[:10], sep="\n")
    CC = cum_2D(C)
    # print()
    # print(*CC[:10], sep="\n")
    for u, d, l, r in UDLR:
        # print(CC[d+1][r+1], CC[u][r+1], CC[d+1][l], CC[u][l])
        one = CC[d+1][r+1] - CC[u][r+1] - CC[d+1][l] + CC[u][l]
        # print(u, d, l, r, one)
        print(zero + one)

if __name__ == "__main__":
    main()
