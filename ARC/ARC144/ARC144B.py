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


def main():
    N, a, b = NMI()
    A = NLI()

    def check(X):
        na = 0
        nb = 0
        for ai in A:
            if ai >= X:
                nb += (ai - X) // b
            else:
                na += (X - ai + a - 1) // a
        return nb >= na

    ok = 0
    ng = 10**10
    while abs(ok - ng) > 1:
        X = (ok + ng) // 2
        if check(X):
            ok = X
        else:
            ng = X
    print(ok)


if __name__ == "__main__":
    main()
