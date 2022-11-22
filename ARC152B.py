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
    N, L = NMI()
    A = NLI()
    X = [L-a for a in A][::-1]
    gap = 10**15
    for a in A:
        idx = bisect.bisect_left(X, a)
        if idx > 0:
            gap = min(gap, a - X[idx-1])
        if idx < N:
            gap = min(gap, X[idx] - a)

    print(2*L + gap*2)


if __name__ == "__main__":
    main()
