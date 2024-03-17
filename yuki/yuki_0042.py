import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 9
MOD99 = 998244353

input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()
SMI = lambda: input().split()
SLI = lambda: list(SMI())
EI = lambda m: [NLI() for _ in range(m)]


def div_sparse_one(f: list, k, M):
    """(1-x^k)で割る x^Mまで"""
    res = f.copy()
    for i in range(M+1):
        if i+k <= M:
            res[i+k] += res[i]
            res[i+k] %= MOD
    return res


def lagrangian_interpolation(P, n, mod):
    """
    d次多項式f(x)のラグランジュ補完mod O(D^2)
    https://ikatakos.com/pot/programming_algorithm/linear_algebra/lagrange_interpolation
    :param P: d+1個の(x, f(x))のlist
    :return: f(n) mod
    """
    res = 0
    for i, (xi, fx) in enumerate(P):
        f = fx
        for j, (xj, _) in enumerate(P):
            if i == j:
                continue
            f = f * (n-xj) * pow(xi-xj, -1, mod) % mod
        res = (res + f) % mod
    return res


def main():
    C = [1, 5, 10, 50, 100, 500]
    f = [0] * 3001
    f[0] = 1
    for c in C:
        f = div_sparse_one(f, c, 3000)

    T = NI()
    for _ in range(T):
        M = NI()
        r = M % 500
        P = []
        for i in range(6):
            P.append([r + i*500, f[r + i*500]])
        res = lagrangian_interpolation(P, M, MOD)
        print(res)


if __name__ == "__main__":
    main()
