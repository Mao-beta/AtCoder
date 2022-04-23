import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations

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
    T = NI()

    for _ in range(T):
        N = NI()
        A = NLI()
        A = [x-1 for x in A]
        if sum(A) % 2:
            print("errorgorn")
        else:
            print("maomao90")


if __name__ == "__main__":
    main()
