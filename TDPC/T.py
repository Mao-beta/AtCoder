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


def mul(f, g, mod=998244353):
    """愚直畳み込み"""
    fn = len(f)
    gn = len(g)
    res = [0] * (fn + gn - 1)
    for fi in range(fn):
        for gi in range(gn):
            res[fi+gi] += f[fi] * g[gi] % mod
            res[fi+gi] %= mod
    return res


def bostan_mori(P: list, Q: list, n: int, mod=998244353):
    """
    d+1項間線形漸化式Qをもつ数列の第n項 modをもとめる
    A = P / Q
    O(M(d)logN) M(d)はd次多項式同士の積の計算量(O(d^2 logN))
    http://q.c.titech.ac.jp/docs/progs/polynomial_division.html

    :param P: 母関数の分子を表すd項以下のlist
    :param Q: 母関数の分母をあらわすd+1項のlist
        (フィボナッチなら An - An-1 - An-2 = 0 なので Q=[1, -1, -1])
    :param n: 求めたい第n項(0-index)
    :return: A[n]
    """

    while n > 0:
        Qm = [-q if i % 2 else q for i, q in enumerate(Q)]
        V = mul(Q, Qm, mod)
        Q = V[::2]
        PQm = mul(P, Qm, mod)
        if n % 2 == 0:
            P = PQm[::2]
            n >>= 1
        else:
            P = PQm[1::2]
            n >>= 1

    return P[0]


def main():
    K, N = NMI()
    A = [1] * K
    Q = [-1] * (K+1)
    Q[0] = 1
    P = mul(A, Q, MOD)[:K]

    X = bostan_mori(P, Q, N-1, MOD)
    print(X)


if __name__ == "__main__":
    main()
