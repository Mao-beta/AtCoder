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
    N, Q = NMI()
    P = [[int(s == "B") for s in SI()] for _ in range(N)]
    querys = EI(Q)

    # print(*P, sep="\n")
    Cum = cum_2D(P)
    # print(*Cum, sep="\n")

    def calc(h, w):
        # [0, h), [0, w)の黒の個数
        res = 0
        hn, hr = divmod(h, N)
        wn, wr = divmod(w, N)
        res += Cum[-1][-1] * hn * wn
        res += area_sum(Cum, 0, hr, 0, N) * wn
        res += area_sum(Cum, 0, N, 0, wr) * hn
        res += area_sum(Cum, 0, hr, 0, wr)
        return res

    for A, B, C, D in querys:
        C += 1
        D += 1
        ans = calc(C, D) - calc(C, B) - calc(A, D) + calc(A, B)
        print(ans)


if __name__ == "__main__":
    main()
