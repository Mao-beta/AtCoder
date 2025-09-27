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
    A = list(range(1, N + 1))
    base = 0
    for qi in range(Q):
        q, *X = NMI()
        if q == 1:
            p, x = X
            p -= 1
            A[(base+p)%N] = x
        elif q == 2:
            p = X[0] - 1
            print(A[(base+p)%N])
        else:
            k = X[0]
            base = (base + k) % N


if __name__ == "__main__":
    main()
