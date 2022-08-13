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
    R = [NI() for _ in range(N)]
    m, M = R[0], R[0]
    for i in range(1, N):
        r = R[i]

        if r < m:
            m -= r
        elif r < M:
            m = 0
        else:
            m = abs(r-M)

        M += r

    print(M)
    print(m)


if __name__ == "__main__":
    main()
