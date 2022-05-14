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
    A, B, C, D, E, F, X = NMI()
    taka = X // (A+C) * A * B + min(X % (A+C), A) * B
    aoki = X // (D+F) * D * E + min(X % (D+F), D) * E
    if taka == aoki:
        print("Draw")
    elif taka > aoki:
        print("Takahashi")
    else:
        print("Aoki")


if __name__ == "__main__":
    main()
