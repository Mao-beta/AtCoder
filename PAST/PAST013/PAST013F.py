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
    N = NI()
    A, B, C, D = NMI()
    X = int(SI().replace(".", ""))
    S = A * 1000 + B * 2000 + C * 3000 + D * 4000
    k = (S - N * X + (X - 1000 - 1)) // (X - 1000)
    print(max(k, 0))


if __name__ == "__main__":
    main()
