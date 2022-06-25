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
    N, K, Q = NMI()
    A = NLI()
    L = NLI()
    M = [0] * (N+1)
    for a in A:
        M[a] = 1

    for l in L:
        a = A[l-1]
        if a == N or M[a+1]:
            continue
        M[a] = 0
        M[a+1] = 1
        A[l-1] += 1

    print(*A)


if __name__ == "__main__":
    main()
