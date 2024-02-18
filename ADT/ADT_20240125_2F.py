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
    N, K = NMI()
    A = NLI()
    B = []
    for m in range(K):
        B.append(sorted(A[m::K]))
    prev = -1
    for i in range(N):
        x, r = divmod(i, K)
        if B[r][x] < prev:
            print("No")
            return
        prev = B[r][x]
    print("Yes")


if __name__ == "__main__":
    main()
