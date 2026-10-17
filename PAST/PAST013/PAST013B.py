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
    A, B, C, D = NMI()
    if B < 0:
        A *= -1
        B *= -1
    if D < 0:
        C *= -1
        D *= -1
    if A * D < B * C:
        print("<")
    elif A * D > B * C:
        print(">")
    else:
        print("=")


if __name__ == "__main__":
    main()
