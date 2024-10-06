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
    S = SI()
    K = NI()
    N = len(S)
    Knum = S.count("K")
    Enum = S.count("E")
    Ynum = len(S) - Knum - Enum
    dp = [[[[0]*(K**2+1) for _ in range(Enum+1)] for _ in range(Knum+1)] for _ in range(N+1)]
    dp[0][0][0][0] = 1
    for i in range(N):
        for k in range(Knum+1):
            for e in range(Enum+1):
                for j in range(K**2+1):
                    pass


if __name__ == "__main__":
    main()
