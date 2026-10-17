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
    X = NI()
    S = set(range(1, 10))
    for i in range(1, 10):
        for j in range(10):
            s = 10 * i + j
            S.add(s)
            g = j - i
            while s < 10**20:
                k = s % 10 + g
                if 0 <= k < 10:
                    s = 10 * s + k
                    S.add(s)
                else:
                    break

    S = sorted(list(S))
    print(S[bisect.bisect_left(S, X)])


if __name__ == "__main__":
    main()
