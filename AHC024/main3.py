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
    N, M = NMI()
    C = EI(N)
    G = [set() for _ in range(M + 1)]

    DH = [0, 0, 1, -1]
    DW = [1, -1, 0, 0]

    DH8 = [0, 0, 1, -1, 1, 1, -1, -1]
    DW8 = [1, -1, 0, 0, 1, -1, 1, -1]




if __name__ == "__main__":
    main()
