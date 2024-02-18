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

    # iから始めたときの総和
    D = defaultdict(int)
    D[1] = 0
    D[2] = 2

    def rec(x):
        res = x
        if x in D:
            return D[x]

        res += rec(x//2)
        res += rec((x+1)//2)
        D[x] = res
        return res

    print(rec(N))


if __name__ == "__main__":
    main()
