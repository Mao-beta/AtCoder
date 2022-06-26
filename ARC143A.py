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
    A = NLI()
    A.sort(reverse=True)
    a, b, c = A # a > b > c
    q = 0
    r = a - b + q
    p = b - c + r
    B = [p+r, p+q, q+r]
    if A[0] >= B[0]:
        print(sum(B) // 2 + A[0] - B[0])
    else:
        print(-1)


if __name__ == "__main__":
    main()
