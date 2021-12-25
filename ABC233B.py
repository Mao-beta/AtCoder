import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict
from functools import lru_cache

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
    # input
    L, R = NMI()
    S = list(SI())
    S[L-1:R] = S[L-1:R][::-1]
    print("".join(S))


if __name__ == "__main__":
    main()
