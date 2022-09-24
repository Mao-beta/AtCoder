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
    X, Y, Z = NMI()
    if X * Y > 0:
        if abs(X) < abs(Y):
            print(abs(X))
        elif (Y-X) * (Y-Z) < 0:
            print(abs(Z) + abs(X-Z))
        else:
            print(-1)

    else:
        print(abs(X))


if __name__ == "__main__":
    main()
