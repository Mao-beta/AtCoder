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
    N = NI()
    A = [NI() for _ in range(N)]
    A.sort()

    if N % 2:
        m = N // 2
        a, b, c = A[m-1], A[m], A[m+1]
        ans = sum(A[:m - 1]) * (-2) + sum(A[m + 2:]) * 2
        if c-b > b-a:
            ans += 2*c - b - a
        else:
            ans += c + b - 2*a

    else:
        m = N // 2
        ans = sum(A[:m]) * (-2) + sum(A[m:]) * 2
        ans += A[m-1] - A[m]

    print(ans)


if __name__ == "__main__":
    main()
