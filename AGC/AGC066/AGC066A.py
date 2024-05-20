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


def main():
    N, d = NMI()
    A = EI(N)

    res = 0
    P = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            a = A[i][j] % (2 * d)
            if (i+j) % 2 == 0:
                g0 = -a
                g2d = 2*d-a
                if abs(g0) < abs(g2d):
                    res += abs(g0)
                    P[i][j] = A[i][j] + g0
                else:
                    res += abs(g2d)
                    P[i][j] = A[i][j] + g2d
            else:
                P[i][j] = A[i][j] + d-a
                res += abs(d-a)

    if res <= d * N * N / 2:
        # print(res)
        for row in P:
            print(*row)
        return

    res = 0
    P = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            a = A[i][j] % (2 * d)
            if (i + j) % 2 == 1:
                g0 = -a
                g2d = 2 * d - a
                if abs(g0) < abs(g2d):
                    res += abs(g0)
                    P[i][j] = A[i][j] + g0
                else:
                    res += abs(g2d)
                    P[i][j] = A[i][j] + g2d
            else:
                P[i][j] = A[i][j] + d - a
                res += abs(d - a)

    if res <= d * N * N / 2:
        # print(res)
        for row in P:
            print(*row)
        return


if __name__ == "__main__":
    main()
