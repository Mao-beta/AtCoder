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
EI = lambda m: [NLI() for _ in range(m)]


def main():
    N, M = NMI()
    A = NLI()
    B = A[2:]
    B.sort()

    ans = 10**20
    a0, a1 = A[0], A[1]

    for l in range(N-M-1):
        r = l + M-1
        bl, br = B[l], B[r]
        k = 0
        if bl < a0:
            k += a0 - bl
        if a1 < br:
            k += br - a1
        ans = min(ans, k)

    print(ans)


if __name__ == "__main__":
    main()
