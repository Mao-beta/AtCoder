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


def main():
    N, M = NMI()
    A = NLI()
    B = NLI()
    buff = 1505
    X = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            X[i][j] = A[i] * B[j] % M
    NN = buff*3
    F = [[0]*NN for _ in range(NN)]
    for i in range(N):
        for j in range(N):
            x = X[i][j]
            # 左上　左・上・下・右
            F[buff + i + 1 - buff][buff + j + 1 - buff] += (buff - 1) * x
            F[buff + i + 0 - buff][buff + j + 2 - buff] -= (buff - 1) * x
            F[buff + i + 2 - buff][buff + j + 2 - buff] -= buff * x
            F[buff + i + 1 - buff][buff + j + 3 - buff] += buff * x

            # 左下　左・上・下・右
            F[buff + i + 1 + buff-1][buff + j + 1 - buff] -= (buff - 1) * x
            F[buff + i + 0 + buff-1][buff + j + 2 - buff] += buff * x
            F[buff + i + 2 + buff-1][buff + j + 2 - buff] += (buff - 1) * x
            F[buff + i + 1 + buff-1][buff + j + 3 - buff] -= buff * x

            # 右上　左・上・下・右
            F[buff + i + 1 - buff][buff + j + 1 + buff-1] -= buff * x
            F[buff + i + 0 - buff][buff + j + 2 + buff-1] += buff * x
            F[buff + i + 2 - buff][buff + j + 2 + buff-1] += buff * x
            F[buff + i + 1 - buff][buff + j + 3 + buff-1] -= buff * x

            # 右下　左・上・下・右
            F[buff + i + 1 + buff - 1][buff + j + 1 + buff-1] += buff * x
            F[buff + i + 0 + buff - 1][buff + j + 2 + buff-1] -= buff * x
            F[buff + i + 2 + buff - 1][buff + j + 2 + buff-1] -= buff * x
            F[buff + i + 1 + buff - 1][buff + j + 3 + buff-1] += buff * x

    for i in range(NN-1, -1, -1):
        for j in range(NN-1, -1, -1):
            ni, nj = i-1, j+1
            if 0 <= ni < NN and 0 <= nj < NN:
                F[ni][nj] += F[i][j]
    for i in range(NN):
        for j in range(NN):
            ni, nj = i+1, j+1
            if 0 <= ni < NN and 0 <= nj < NN:
                F[ni][nj] += F[i][j]
    for i in range(NN):
        for j in range(NN):
            ni, nj = i, j+1
            if 0 <= ni < NN and 0 <= nj < NN:
                F[ni][nj] += F[i][j]
    for i in range(NN):
        for j in range(NN):
            ni, nj = i+1, j
            if 0 <= ni < NN and 0 <= nj < NN:
                F[ni][nj] += F[i][j]
    ans = 0
    for i in range(N):
        for j in range(N):
            tmp = F[i+buff][j+buff] + i*N + j
            ans ^= tmp
    print(ans)


if __name__ == "__main__":
    main()
