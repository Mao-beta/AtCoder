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
    A = NLI()
    B = NLI()
    win = 0
    total = 0
    for P in permutations(A, N):
        for Q in permutations(B, N):
            awin = 0
            for a, b in zip(P, Q):
                if a > b:
                    awin += 1
            bwin = N - awin
            if awin > bwin:
                win += 1
            total += 1
    print(win / total)


if __name__ == "__main__":
    main()
