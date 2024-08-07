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
    N, K = NMI()
    p = 1
    N2inv = pow(N**2, MOD99-2, MOD99)
    for _ in range(K):
        p = (N**2-2*N+2) * p * N2inv + 2 * (1-p) * N2inv
        p %= MOD99
    q = 1 - p
    ans = p + q * (N+2) * (N-1) // 2 * pow(N-1, MOD99-2, MOD99)
    print(ans % MOD99)


# す?よ?と???あい?????


if __name__ == "__main__":
    main()
