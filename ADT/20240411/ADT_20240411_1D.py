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
    S = SI()
    T = SI()
    N = len(S)
    S = [ord(s) - ord("a") for s in S]
    T = [ord(s) - ord("a") for s in T]

    for i in range(26):
        SS = [(s+i)%26 for s in S]
        if SS == T:
            print("Yes")
            return

    print("No")


if __name__ == "__main__":
    main()
