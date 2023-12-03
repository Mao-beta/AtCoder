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
    N, S, M, L = NMI()
    ans = 10**18
    for s in range(20):
        for m in range(20):
            for l in range(20):
                cost = s * S + m * M + l * L
                num = 6 * s + 8 * m + 12 * l
                if num >= N:
                    ans = min(ans, cost)
    print(ans)


if __name__ == "__main__":
    main()
