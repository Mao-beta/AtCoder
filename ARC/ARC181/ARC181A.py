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

from random import randint


def solve(N, P):
    Q = list(range(1, N + 1))
    R = [randint(10 ** 8, 10 ** 10) for _ in range(N+1)]
    PR = [p^R[p] for p in P]
    QR = [q^R[q] for q in Q]
    if P == Q:
        return 0
    if P[0] == N and P[-1] == 1:
        return 3

    p, q = 0, 0
    for i, (pr, qr) in enumerate(zip(PR, QR)):
        p ^= pr
        q ^= qr
        if pr == qr and p == q:
            # print(i, p, q)
            return 1

    return 2


def guchoku(N, P):
    Q = list(range(1, N + 1))
    if P == Q:
        return 0
    for i in range(N):
        if i == 0:
            X = [P[i]] + sorted(P[i+1:])
        elif i == N-1:
            X = sorted(P[:i]) + [P[i]]
        else:
            X = sorted(P[:i]) + [P[i]] + sorted(P[i+1:])
        if X == Q:
            return 1
    return 2

def main():

    # for N in range(3, 10):
    #     for P in permutations(range(1, N+1)):
    #         P = list(P)
    #         print(N, P)
    #         gu = guchoku(N, P)
    #         ans = solve(N, P)
    #         print(gu, ans)
    #         assert gu == ans
    #
    # return

    T = NI()

    for _ in range(T):
        N = NI()
        P = NLI()
        print(solve(N, P))


if __name__ == "__main__":
    main()
