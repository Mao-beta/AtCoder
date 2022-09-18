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
    A = [0] + NLI() + [0]
    L = list(accumulate(A, max))
    R = list(accumulate(A[::-1], max))[::-1]
    D = NI()
    for _ in range(D):
        l, r = NMI()
        print(max(L[l-1], R[r+1]))


if __name__ == "__main__":
    main()
