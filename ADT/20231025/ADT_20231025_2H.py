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
    T = NI()
    for _ in range(T):
        N = NI()
        LR = EI(N)

        def solve(N, LR):
            R = defaultdict(list)
            for l, r in LR:
                R[l].append(r)
            hq = []
            nex = 0
            L = sorted(list(R.keys()))
            L.append(10**15)
            for i in range(len(L)-1):
                l = L[i]
                if nex < l:
                    nex = l
                for r in R[l]:
                    heappush(hq, r)
                while hq and nex < L[i+1]:
                    if nex > hq[0]:
                        return False
                    nex += 1
                    heappop(hq)
            return True

        if solve(N, LR):
            print("Yes")
        else:
            print("No")



if __name__ == "__main__":
    main()
