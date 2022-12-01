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
    N, X, Y = NMI()
    A = NLI()
    # 0, 0, 1, 1, 2, 0, 
    g = 0
    L = [0, 0, 1, 1, 2]
    for a in A:
        g ^= L[a%5]
    if g:
        print("First")
    else:
        print("Second")


if __name__ == "__main__":
    main()
