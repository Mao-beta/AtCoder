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

    if N < A:
        print(0)
        exit()

    if A <= B:
        print(N - (A-1))
        exit()
    elif B == 1:
        print(N - N // A)
        exit()

    d, m = divmod(N, A)
    # print(d, m, B)
    if m < B:
        print((d-1) * B + m+1)
    else:
        print((d-1) * B + B)


if __name__ == "__main__":
    main()
