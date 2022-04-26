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


def main():
    Y = NI()
    M = NI()
    D = NI()

    def f(y, m, d):
        if 1 <= m <= 2:
            m += 12
            y -= 1

        return 365*y + y//4 - y//100 + y//400 + 306*(m+1)//10 + d - 429

    print(f(2014, 5, 17) - f(Y, M, D))


if __name__ == "__main__":
    main()
