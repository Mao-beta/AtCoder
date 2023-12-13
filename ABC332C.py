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
    N, M = NMI()
    S = SI()

    for logo_base in range(N+1):
        muji = M
        logo = logo_base
        ok = True
        for s in S:
            if s == "1":
                if muji > 0:
                    muji -= 1
                elif logo > 0:
                    logo -= 1
                else:
                    ok = False
                    break

            elif s == "2":
                if logo > 0:
                    logo -= 1
                else:
                    ok = False
                    break

            else:
                muji = M
                logo = logo_base

        if ok:
            print(logo_base)
            return



if __name__ == "__main__":
    main()
