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
    Q = NI()
    hq = []
    for _ in range(Q):
        q, *x = SMI()
        q = int(q)
        if q == 1:
            heappush(hq, int(x[0]))
        elif q == 2:
            print(hq[0])
        else:
            heappop(hq)


if __name__ == "__main__":
    main()