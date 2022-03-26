import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations

if "PyPy" in sys.version:
    import pypyjit

    pypyjit.set_param('max_unroll_recursion=-1')

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
    N, M = NMI()
    A = NLI()[::-1]
    C = NLI()[::-1]

    B = [-200] * (M+1)
    for i in range(M+1):
        c = C[i]
        if i == 0:
            B[i] = c // A[0]
            continue

        for bi in range(i):
            if 0 <= i - bi <= N:
                c -= B[bi] * A[i-bi]

        B[i] = c // A[0]

    print(*B[::-1])


if __name__ == "__main__":
    main()
