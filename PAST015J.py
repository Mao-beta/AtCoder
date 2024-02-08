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
    N, M = NMI()
    X = []
    ABX = EI(N)
    total = 0
    for a, b, x in ABX:
        if x == 0:
            total += a * (b-1)
            X.append([a, b-1])
        else:
            if b == 1:
                total += a
                X.append([a, 1])
            else:
                total += a * b
                X.append([2*a, 1])
                X.append([a, b-2])
    X.sort()
    cut = 0
    while M > 0 and X:
        a, b = X.pop()
        t = min(M, b)
        M -= t
        cut += a * t
    print(total - cut)


if __name__ == "__main__":
    main()
