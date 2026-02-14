import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.set_int_max_str_digits(10**6)
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
    S = set(SI())
    T = set(SI())
    Q = NI()
    for _ in range(Q):
        t = True
        a = True
        W = SI()
        for w in W:
            if w not in S:
                t = False
            if w not in T:
                a = False
        if t and not a:
            print("Takahashi")
        elif a and not t:
            print("Aoki")
        else:
            print("Unknown")


if __name__ == "__main__":
    main()
