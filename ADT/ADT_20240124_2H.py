import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product, chain

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
    H, W, N, h, w = NMI()
    A = EI(H)
    C = Counter(chain.from_iterable(A))

    ans = [[0]*(W-w+1) for _ in range(H-h+1)]
    for a in range(N+1):
        B = [[int(x==a) for x in row] for row in A]
        cum = cum_2D(B)
        for i in range(H-h+1):
            for j in range(W-w+1):
                cnt = area_sum(cum, i, i+h, j, j+w)
                if cnt < C[a]:
                    ans[i][j] += 1

    for row in ans:
        print(*row)


if __name__ == "__main__":
    main()