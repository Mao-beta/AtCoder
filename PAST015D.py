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
    A, B, C, D, R = NMI()
    rec = [0] * 2001
    for t in range(2001):
        if t % D == 0:
            if t < B:
                p = A
                q = A+R
            else:
                p = C
                q = C+R
            for x in range(max(p, t), min(q, 2000)):
                rec[x] = 1

    ok = 1
    for t in range(C, C+R):
        if rec[t] == 0:
            ok = 0
    if ok:
        print("Yes")
    else:
        print("No")



if __name__ == "__main__":
    main()
