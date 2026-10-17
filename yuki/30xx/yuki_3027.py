import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.set_int_max_str_digits(10 ** 6)
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
    N = NI()
    F = NLI()
    X = [[0]*(N+1) for _ in range(N+1)]
    X[0][N] = 1
    for i in range(N):
        for j in range(1, N+1):
            X[i+1][j] += -1 * X[i][j]
            X[i+1][j-1] += X[i][j]
    H = [0] * (N+1)
    for i in range(N+1):
        for j in range(N+1):
            H[i] += X[j][i] * F[N-j]
    # print(*X, sep="\n")
    print(*H)


if __name__ == "__main__":
    main()
