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


def main():
    N = NI()
    A = NLI()
    X = []
    for _ in range(N):
        _ = NI()
        X.append(set(NMI()))

    Q = NI()
    for _ in range(Q):
        _ = NI()
        Y = set(NMI())
        res = -1
        a = -1
        for di, x in enumerate(X):
            if x & Y:
                continue
            if A[di] > a:
                res = di + 1
                a = A[di]

        print(res)


if __name__ == "__main__":
    main()
