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
    X, Y, D = NMI()
    if X > Y:
        X, Y = Y, X
    if D <= X:
        print(D+1)
    elif D <= Y:
        print(X+1)
    elif D <= X+Y:
        print(X-(D-Y)+1)
    else:
        print(0)


if __name__ == "__main__":
    main()
