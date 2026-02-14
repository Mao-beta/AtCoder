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
    N, C = NMI()
    A = NLI()
    C -= 1
    A[C] += 1
    ac = A[C]
    A.sort()
    t = 0
    for i, a in enumerate(A):
        if ac == a:
            t = i
    C = t
    Asum = sum(A) - 1
    bunbo = pow(Asum, MOD99-2, MOD99)
    E = [0] * N
    PEsum = 0
    Psum = (Asum + 1) * bunbo % MOD99
    # print(A)
    for i in range(N-1, -1, -1):
        # Psum -= A[i] / Asum
        # E[i] = (PEsum + 1) / (1-Psum)
        # PEsum += A[i] / Asum * E[i]
        Psum -= (A[i]) * bunbo % MOD99
        Psum %= MOD99
        E[i] = (PEsum + 1) * pow(1-Psum, MOD99-2, MOD99) % MOD99
        PEsum += A[i] * bunbo * E[i] % MOD99
        PEsum %= MOD99
        # print(E[i], Psum, PEsum)
    # print(E, C)
    print(E[C])


if __name__ == "__main__":
    main()
