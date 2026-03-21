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
    K, M = NMI()
    CL = EI(K)
    MOD = 10007 * M

    def rec(i):
        # i桁のrepunitのmod
        if i == 1:
            return 1
        elif i % 2:
            return (rec(i-1) * 10 + 1) % MOD
        else:
            r = rec(i>>1)
            return (r * pow(10, i>>1, MOD) + r) % MOD

    ans = 0
    for c, l in CL:
        ans = (ans * pow(10, l, MOD) + rec(l) * c) % MOD
    print(ans // M)


if __name__ == "__main__":
    main()
