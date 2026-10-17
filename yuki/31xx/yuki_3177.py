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
    def nand(a, b):
        return 1 ^ (a & b)
    for a in range(2):
        for b in range(2):
            for c in range(2):
                if nand(nand(a, b), c) != nand(a, nand(b, c)):
                    print(a, b, c)
                    return


if __name__ == "__main__":
    main()
