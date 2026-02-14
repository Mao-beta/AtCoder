import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.set_int_max_str_digits(10**6)
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
    LR = EI(M)
    LR = [[x-1, y] for x, y in LR]
    L2R = [[] for _ in range(N)]
    hq = []
    for l, r in LR:
        L2R[l].append(r)
    for l in range(N):
        for r in L2R[l]:
            heappush(hq, r)
        if hq and hq[0] <= l:
            print("No")
            return
        if hq:
            heappop(hq)
    if hq:
        print("No")
    else:
        print("Yes")


if __name__ == "__main__":
    main()
