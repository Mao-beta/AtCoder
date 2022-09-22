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
    D = NI()
    A = list(accumulate([0]+[NI() for _ in range(D)]))
    Q = NI()
    for _ in range(Q):
        s, t = NMI()
        x, y = A[s], A[t]
        if x > y:
            print(s)
        elif x < y:
            print(t)
        else:
            print("Same")


if __name__ == "__main__":
    main()
