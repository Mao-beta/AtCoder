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
    N, Q = NMI()
    H = [10**12] + NLI() + [10**12]
    even, odd = 0, 0
    G01 = Counter()
    G10 = Counter()
    for i in range(N+1):
        a, b = H[i], H[i+1]
        if i % 2 == 0:
            G01[b-a] += 1
        else:
            G10[b-a] += 1
    for _ in range(Q):
        t, *X = NMI()
        if t == 1:
            odd += X[0]
        elif t == 2:
            even += X[0]
        else:
            # G01のkey hについて、真の値はh+odd-even
            # G10のkey hについて、真の値はh-odd+even
            u, v = X
            if u % 2 == 0:
                left = H[u-1] + odd
                prev = H[u] + even
                right = H[u+1] + odd
                G10[prev - left - even + odd] -= 1
                G01[right - prev + even - odd] -= 1
                H[u] += v
                G10[prev - left - even + odd + v] += 1
                G01[right - prev + even - odd - v] += 1
            else:
                left = H[u-1] + even
                prev = H[u] + odd
                right = H[u+1] + even
                G01[prev - left + even - odd] -= 1
                G10[right - prev - even + odd] -= 1
                H[u] += v
                G01[prev - left + even - odd + v] += 1
                G10[right - prev - even + odd - v] += 1

        print(G01[even-odd] + G10[odd-even])


if __name__ == "__main__":
    main()
