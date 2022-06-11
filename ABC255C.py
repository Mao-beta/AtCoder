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
    X, A, D, N = NMI()

    if D == 0:
        print(abs(X - A))
        exit()

    last = A + D * (N-1)
    if D < 0:
        D *= -1
        m = last
        M = A
    else:
        m = A
        M = last

    X -= m
    M -= m

    if X > M:
        print(X - M)
        exit()

    if X < 0:
        print(-X)
        exit()

    r = X % D
    print(min(r, D-r))


if __name__ == "__main__":
    main()
