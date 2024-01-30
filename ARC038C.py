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
    CA = EI(N-1)
    G = [0] * N
    res = 0
    for i, (c, a) in enumerate(CA, start=1):
        a %= 2
        S = set(G[i-c:i])
        g = 0
        for j in range(N+1):
            if j not in S:
                g = j
                break
        G[i] = g
        if a:
            res ^= g
    if res:
        print("First")
    else:
        print("Second")


if __name__ == "__main__":
    main()
