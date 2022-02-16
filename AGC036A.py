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
    S = NI()
    X1 = 0
    Y1 = 0
    X2 = 10**9
    Y2 = 1
    X3 = (-S) % 10**9
    Y3 = (S+X3) // 10**9
    print(X1, Y1, X2, Y2, X3, Y3)


if __name__ == "__main__":
    main()
