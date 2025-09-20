import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.set_int_max_str_digits(10**6)
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
    N, Q = NMI()
    A = NLI()
    B = NLI()
    M = [min(a, b) for a, b in zip(A, B)]
    ans = sum(M)
    for _ in range(Q):
        c, x, v = SMI()
        x, v = int(x)-1, int(v)
        if c == "A":
            if A[x] < B[x] and v < B[x]:
                ans -= M[x] - v
            elif A[x] < B[x] and v >= B[x]:
                ans -= M[x] - B[x]
            elif A[x] >= B[x] and v < B[x]:
                ans -= M[x] - v
            elif A[x] >= B[x] and v >= B[x]:
                ans -= M[x] - B[x]
            A[x] = v
            M[x] = min(A[x], B[x])
        else:
            b = B[x]
            if B[x] < A[x] and v < A[x]:
                ans -= M[x] - v
            elif B[x] < A[x] and v >= A[x]:
                ans -= M[x] - A[x]
            elif B[x] >= A[x] and v < A[x]:
                ans -= M[x] - v
            elif B[x] >= A[x] and v >= A[x]:
                ans -= M[x] - A[x]
            B[x] = v
            M[x] = min(A[x], B[x])
        # print(A, B, M)
        print(ans)


if __name__ == "__main__":
    main()
