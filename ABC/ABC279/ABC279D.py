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
    A, B = NMI()
    L = 1
    R = 10**18 + 1

    def f(g):
        return B * (g-1) + A / (g**0.5)

    for i in range(100):
        m1 = (L * 2 + R) // 3
        m2 = (L + R * 2) // 3
        if f(m1) < f(m2):
            R = m2
        else:
            L = m1

    print(min(f(L), f(m1), f(m2), f(R)))


if __name__ == "__main__":
    main()
