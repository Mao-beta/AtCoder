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
    N, A, B = NMI()
    if A > B:
        print(0)
        exit()

    if N == 1:
        if A != B:
            print(0)
            exit()
        else:
            print(1)
            exit()

    if A == B:
        print(1)
        exit()

    M = A + B * (N-1)
    m = A * (N-1) + B
    print(M - m + 1)


if __name__ == "__main__":
    main()
