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
    A = NLI()
    E = 0
    C = 0
    inv = pow(N, -1, MOD99)
    for i in range(N-1, -1, -1):
        C += A[i]
        e = (E + C) * inv % MOD99
        E += e
        E %= MOD99
        C %= MOD99
    print(e % MOD99)


if __name__ == "__main__":
    main()
