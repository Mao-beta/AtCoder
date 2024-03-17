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
    ABCDR = [SLI() for _ in range(N)]
    for s in range(10):
        s = str(s)
        ok = True
        for *A, r in ABCDR:
            if s in set(A) and r == "NO":
                ok = False
            elif s not in set(A) and r == "YES":
                ok = False
        if ok:
            print(s)
            return


if __name__ == "__main__":
    main()
