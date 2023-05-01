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


def print_err(*args):
    print(*args, file=sys.stderr)


def main():
    N = NI()
    A = list(map(int, SI()))
    B = list(map(int, SI()))

    for i in range(N):
        if A[i] > B[i]:
            A[i], B[i] = B[i], A[i]

    MA = 0
    MB = 0
    T = 1
    for i in range(N-1, -1, -1):
        a, b = A[i], B[i]
        MA += a * T
        MB += b * T
        MA %= MOD99
        MB %= MOD99
        T = T * 10 % MOD99

    print(MA * MB % MOD99)


if __name__ == "__main__":
    main()
