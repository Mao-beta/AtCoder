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
    A, B = NMI()
    if A * B <= 0:
        print("Zero")
    elif A > 0:
        print("Positive")
    else:
        if abs(A - B) % 2:
            print("Positive")
        else:
            print("Negative")


if __name__ == "__main__":
    main()
