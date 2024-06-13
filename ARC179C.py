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


def main(N):
    cnt = N+1
    def plus(i, j):
        print("+", i, j, flush=True)
        return NI()

    def lt(i, j):
        print("?", i, j, flush=True)
        return NI()

    def search(X, a):
        l = 0
        r = len(X)
        while r - l > 0:
            m = (l + r) // 2
            j = X[m]
            res = lt(a, j)
            if res == 1:
                r = m
            else:
                l = m + 1
        return l

    L = []
    for i in range(1, N+1):
        idx = search(L, i)
        L.insert(idx, i)

    # minとmaxを足していく
    while len(L) > 1:
        P = plus(L[0], L[-1])
        cnt += 1
        L.pop(0)
        L.pop()
        idx = search(L, P)
        L.insert(idx, P)

    print("!", flush=True)


if __name__ == "__main__":
    main(NI())
