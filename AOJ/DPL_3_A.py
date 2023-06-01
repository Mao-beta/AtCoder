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
    H, W = NMI()

    C = []
    C.append([1] * (W + 1))
    for h in range(H):
        C.append([1] + NLI())

    def judge(X):
        if X == 0:
            return True

        A = [[0]*(W+2)for _ in range(H+2)]
        for h in range(H+1):
            for w in range(W+1):
                if C[h][w] == 1:
                    hm = min(H+1, h+X)
                    wm = min(W+1, w+X)
                    A[h][w] += 1
                    A[h][wm] -= 1
                    A[hm][w] -= 1
                    A[hm][wm] += 1

        A = cum_2D(A)

        # print(X)
        # print(*A, sep="\n")
        for h in range(1, H+2):
            for w in range(1, W+2):
                if A[h][w] == 0:
                    return True

        return False

    ok = 0
    ng = 1401
    while abs(ok - ng) > 1:
        X = (ok + ng) // 2
        if judge(X):
            ok = X
        else:
            ng = X

    print(ok**2)
    # print(*C, sep="\n")


if __name__ == "__main__":
    main()
