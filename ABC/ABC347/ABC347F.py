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


def accum_max(X, n):
    for i in range(n-1):
        for j in range(n):
            X[i+1][j] = max(X[i+1][j], X[i][j])
    for i in range(n):
        for j in range(n-1):
            X[i][j+1] = max(X[i][j], X[i][j+1])
    return X


def main():
    N, M = NMI()
    A = EI(N)
    INF = 10**18

    def solve(A):
        C = cum_2D(A)
        # print(*C, sep="\n")
        # Aにおいて右下が(i,j)のMxM正方形の合計値
        one = [[-INF]*N for _ in range(N)]
        for i in range(M-1, N):
            for j in range(M-1, N):
                one[i][j] = area_sum(C, i+1-M, i+1, j+1-M, j+1)

        # Aにおいて右下が(i,j)のMxM正方形の合計値の累積Max
        one = accum_max(one, N)
        # print(*one, sep="\n")

        # Aにおいて2個目の右下が(i,j)のMxM正方形の合計値
        two = [[-INF]*N for _ in range(N)]
        for i in range(M-1, N):
            for j in range(M-1, N):
                if i < 2 * M - 1 and j < 2 * M - 1:
                    continue
                s = area_sum(C, i+1-M, i+1, j+1-M, j+1)
                if i >= M:
                    two[i][j] = max(two[i][j], one[i-M][j] + s)
                if j >= M:
                    two[i][j] = max(two[i][j], one[i][j-M] + s)

        # print(*two, sep="\n")
        two = accum_max(two, N)
        # print(*two, sep="\n")
        # print()

        three = [[-INF] * N for _ in range(N)]
        for i in range(N-M+1):
            for j in range(N-M+1):
                s = area_sum(C, i, i+M, j, j+M)
                if i > 0:
                    # print(i, j, "two[i-1][-1]", two[i-1][-1])
                    three[i][j] = max(three[i][j], two[i-1][-1] + s)
                if j > 0:
                    # print(i, j, "two[-1][j-1]", two[-1][j-1])
                    three[i][j] = max(three[i][j], two[-1][j-1] + s)

        # print(*three, sep="\n")

        res = -INF
        for row in three:
            res = max(res, max(row))
        return res


    ans = solve(A)
    A = [a[::-1] for a in A]
    ans = max(ans, solve(A))
    A = A[::-1]
    ans = max(ans, solve(A))
    A = [a[::-1] for a in A]
    ans = max(ans, solve(A))
    print(ans)


if __name__ == "__main__":
    main()
