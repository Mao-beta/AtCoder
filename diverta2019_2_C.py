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
    N = NI()
    A = NLI()
    A = [(a, i) for i, a in enumerate(A, start=1)]
    A.sort()
    ans = []
    M = A[-1][0]
    m = A[0][0]

    for j in range(1, N-1):
        a, i = A[j]
        if a < 0:
            ans.append((M, a))
            M -= a
        else:
            ans.append((m, a))
            m -= a

    ans.append((M, m))
    M -= m
    print(M)
    for x, y in ans:
        print(x, y)


if __name__ == "__main__":
    main()
