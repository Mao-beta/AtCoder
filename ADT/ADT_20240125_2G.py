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
    N = NI()
    A = EI(2*N-1)

    ans = [0]
    mask = (1 << (2*N)) - 1

    def rec(S, b):
        if S == mask:
            ans[0] = max(ans[0], b)
            return

        ti = 0
        for i in range(2*N):
            if (S >> i) & 1 == 0:
                ti = i
                break

        for j in range(ti+1, 2*N):
            if (S >> j) & 1 == 0:
                rec(S | (1<<ti) | (1<<j), b ^ A[ti][j-ti-1])

    rec(0, 0)
    print(ans[0])


if __name__ == "__main__":
    main()
