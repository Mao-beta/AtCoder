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
    N, M = NMI()
    XY = [NLI() for _ in range(M)]
    C = [1] * (N+1)
    R = [0] * (N+1)
    R[1] = 1
    for x, y in XY:
        C[x] -= 1
        C[y] += 1
        if R[x]:
            if C[x] == 0:
                R[x] = 0
                R[y] = 1
            else:
                R[y] = 1

    print(sum(R))


if __name__ == "__main__":
    main()
