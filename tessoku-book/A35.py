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
    N = NI()
    A = NLI()

    for i in range(N-1, 0, -1):
        tmp = []
        for j in range(i):
            if i % 2 == 1:
                tmp.append(max(A[j], A[j+1]))
            else:
                tmp.append(min(A[j], A[j + 1]))
        A = tmp

    print(A[-1])


if __name__ == "__main__":
    main()
