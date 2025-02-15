import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.setrecursionlimit(1000000)
MOD = 10**9+7
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
    S = SI()
    cnt = Counter(S)
    N = len(S)
    C = [[0]*1001 for _ in range(1001)]
    C[0][0] = 1
    C[1][0] = 1
    C[1][1] = 1
    for n in range(2, 1001):
        for r in range(n+1):
            if r == 0 or r == n:
                C[n][r] = 1
            else:
                C[n][r] = (C[n-1][r-1] + C[n-1][r]) % MOD
    ans = 1
    for x, k in cnt.items():
        ans = ans * C[N][k] % MOD
        N -= k
    print((ans-1) % MOD)


if __name__ == "__main__":
    main()
