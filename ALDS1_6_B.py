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


def partition(A, p, r):
    i = p
    x = A[r]
    for j in range(p, r):
        a = A[j]
        if a <= x:
            A[i], A[j] = A[j], A[i]
            i += 1
    A[i], A[r] = A[r], A[i]
    return i


def main():
    N = NI()
    A = NLI()
    idx = partition(A, 0, N-1)
    A[idx] = f"[{A[idx]}]"
    print(*A)


if __name__ == "__main__":
    main()
