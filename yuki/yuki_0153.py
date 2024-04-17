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
    if N == 1:
        print("B")
        return
    G = [0] * (N+1)
    G[2] = 1
    for i in range(3, N+1):
        two = G[i//2] ^ G[i-(i//2)]
        if i % 3 == 0 or i % 3 == 2:
            three = G[i//3]
        else:
            three = G[i//3+1]
        for g in range(3):
            if g not in [two, three]:
                G[i] = g
                break
    if G[N]:
        print("A")
    else:
        print("B")


if __name__ == "__main__":
    main()
