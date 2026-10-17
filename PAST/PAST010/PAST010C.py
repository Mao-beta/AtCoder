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
    A = list(SI())
    for i in range(25, -1, -1):
        z = (i+1) * 3
        if len(A) <= z:
            continue
        # A[-z:] = ["0"] * z
        print("".join(A[:-z]) + chr(i + ord("a")))
        break



if __name__ == "__main__":
    main()
