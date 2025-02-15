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
    M = NI()
    R = N // 1000 % M
    C = [[] for _ in range(M+1)]
    mod = 10**9
    C[0].append(1)
    C[1] = [1, 1]
    for n in range(2, M+1):
        C[n].append(1)
        for r in range(1, n):
            C[n].append((C[n-1][r] + C[n-1][r-1]) % mod)
        C[n].append(1)
    print(C[M][R])


if __name__ == "__main__":
    main()
