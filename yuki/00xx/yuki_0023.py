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
    H, A, D = NMI()
    INF = 10**10
    E = [INF] * (H+1+A+D)
    for h in range(H+A+D, -1, -1):
        if h >= H:
            E[h] = 0
            continue
        E[h] = min(E[h], E[h+A] + 1)
        E[h] = min(E[h], E[h+D] + 1.5)
    print(E[0])


if __name__ == "__main__":
    main()
