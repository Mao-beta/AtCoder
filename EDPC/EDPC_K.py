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
    N, K = NMI()
    A = NLI()
    G = [0] * (K+1)
    for g in range(1, K+1):
        S = set()
        for a in A:
            if g - a >= 0:
                S.add(G[g-a])

        for x in range(K+1):
            if x not in S:
                G[g] = x
                break

    if G[K] > 0:
        print("First")
    else:
        print("Second")


if __name__ == "__main__":
    main()
