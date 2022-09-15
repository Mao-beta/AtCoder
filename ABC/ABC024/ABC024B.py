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
    N, T = NMI()
    A = [NI() for _ in range(N)]
    imos = [0] * (10**6*2)
    for a in A:
        imos[a] += 1
        imos[a+T] -= 1
    S = list(accumulate(imos))
    print(sum(1 for s in S if s > 0))


if __name__ == "__main__":
    main()
