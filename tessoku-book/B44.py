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
    A = [NLI() for _ in range(N)]
    Q = NI()
    for _ in range(Q):
        q, x, y = NMI()
        x -= 1
        y -= 1
        if q == 1:
            A[x], A[y] = A[y], A[x]
        else:
            print(A[x][y])


if __name__ == "__main__":
    main()