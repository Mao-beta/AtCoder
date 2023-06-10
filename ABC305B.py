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
EI = lambda m: [NLI() for _ in range(m)]


def main():
    p, q = SMI()
    L = [0, 3, 4, 8, 9, 14, 23]
    D = {s: i for i, s in enumerate(list("ABCDEFG"))}
    p, q = D[p], D[q]
    if p > q:
        p, q = q, p
    print(L[q] - L[p])


if __name__ == "__main__":
    main()
