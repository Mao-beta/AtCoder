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
    N, K = NMI()
    A = NLI()
    C = [0] * (10**6+1)
    for a in A:
        C[a] += 1
    for g in range(10**6, 0, -1):
        tmp = 0
        for x in range(g, 10**6+1, g):
            tmp += C[x]
        if tmp >= K:
            print(g)
            return


if __name__ == "__main__":
    main()
