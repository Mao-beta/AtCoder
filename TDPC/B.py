import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations

if "PyPy" in sys.version:
    import pypyjit

    pypyjit.set_param('max_unroll_recursion=-1')

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
    N, M = NMI()
    A = NLI()
    B = NLI()
    INF = 10**10

    @lru_cache(maxsize=None)
    def rec(i, j):
        if i == N and j == M:
            return 0

        if (i+j) % 2 == 0:
            a = 0
            if i < N:
                a = max(a, rec(i+1, j) + A[i])
            if j < M:
                a = max(a, rec(i, j+1) + B[j])

        else:
            a = INF
            if i < N:
                a = min(a, rec(i + 1, j))
            if j < M:
                a = min(a, rec(i, j + 1))

        return a

    print(rec(0, 0))


if __name__ == "__main__":
    main()
