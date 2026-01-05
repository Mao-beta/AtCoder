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
    A = NLI()
    C = list(accumulate([0]+A)) + [10**20]

    def rec(l, r):
        if l+1 == r:
            return
        d = C[r] - C[l]
        dr = d // 2
        dl = d - dr
        t = C[l] + dl
        idx = bisect.bisect_left(C, t)
        if C[idx] != t:
            print("No")
            exit()
        else:
            rec(l, idx)
            rec(idx, r)

    rec(0, N)
    print("Yes")


if __name__ == "__main__":
    main()
