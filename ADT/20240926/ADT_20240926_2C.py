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
    K, G, M = NMI()
    g, m = 0, 0
    for _ in range(K):
        if g == G:
            g = 0
        elif m == 0:
            m = M
        else:
            if m + g > G:
                m, g = m+g-G, G
            else:
                m, g = 0, m+g
    print(g, m)


if __name__ == "__main__":
    main()
