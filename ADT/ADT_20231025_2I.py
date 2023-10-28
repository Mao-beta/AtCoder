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
    N = NI()
    Pre = NLI()
    In = NLI()

    if Pre[0] != 1:
        print(-1)
        return

    L = [0] * (N+1)
    R = [0] * (N+1)

    Pre_inv = [0] * (N + 1)
    for i, x in enumerate(Pre):
        Pre_inv[x] = i

    In_inv = [0] * (N+1)
    for i, x in enumerate(In):
        In_inv[x] = i

    def rec(now, llim, rlim):
        idx = In_inv[now]
        pre_idx = Pre_inv[now]
        fn = idx - llim
        ln = rlim - (idx+1)
        if idx < llim or rlim <= idx:
            print(-1)
            exit()

        if fn > 0 and pre_idx + 1 < N:
            L[now] = Pre[pre_idx + 1]
            rec(L[now], llim, idx)

        if ln > 0 and pre_idx + 1 + fn < N:
            R[now] = Pre[pre_idx + 1 + fn]
            rec(R[now], idx+1, rlim)

    rec(1, 0, N)
    for l, r in zip(L[1:], R[1:]):
        print(l, r)


if __name__ == "__main__":
    main()
