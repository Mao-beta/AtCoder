import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

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
    M = NLI()
    g = 0
    for m in M:
        for p in range(2, 10**4):
            k = 0
            while m % p == 0:
                k += 1
                m //= p
            g ^= k % 3
            if m == 1:
                break
    if g:
        print("Alice")
    else:
        print("Bob")


if __name__ == "__main__":
    main()
