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
    X = NLI()
    Y = [1/x for x in X]
    Y.sort()
    # print(Y)

    M = -10**20
    m = 10**20
    for i, y in enumerate(Y):
        # Z = [yy - y for yy in Y]
        # print(Z)
        if i < N-2:
            M = max(M, (Y[N-1] + y) * (Y[N-2] + y) - y**2)
        if i >= 2:
            M = max(M, (Y[0] + y) * (Y[1] + y) - y ** 2)

        if 1 <= i < N-1:
            m = min(m, (Y[0] + y) * (Y[N-1] + y) - y ** 2)
        elif i == 0:
            m = min(m, (Y[1] + y) * (Y[2] + y) - y ** 2)
        else:
            m = min(m, (Y[N-2] + y) * (Y[N-3] + y) - y ** 2)

    print(m, M)


if __name__ == "__main__":
    main()
