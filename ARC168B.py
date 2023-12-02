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
    A = NLI()
    x = 0
    S = set()
    for a in A:
        x ^= a
        if a in S:
            S.discard(a)
        else:
            S.add(a)

    if x != 0:
        print(-1)
    else:
        if not S:
            print(0)
        else:
            M = sorted(list(S))[-1]
            print(M-1)


if __name__ == "__main__":
    main()
