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
    D, N = NMI()
    LRH = [NLI() for _ in range(N)]
    M = [24] * D
    for l, r, h in LRH:
        for d in range(l-1, r):
            M[d] = min(M[d], h)
    print(sum(M))


if __name__ == "__main__":
    main()
