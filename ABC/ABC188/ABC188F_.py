import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache, cache
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
    X, Y = NMI()

    @cache
    def rec(x):
        if x <= 1:
            return abs(X-x)
        elif x % 2:
            return min(abs(X-x), rec((x-1)//2) + 2, rec((x+1)//2) + 2)
        else:
            return min(abs(X-x), rec(x//2) + 1)

    print(rec(Y))


if __name__ == "__main__":
    main()
