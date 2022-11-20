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


def main():
    N, Q = NMI()
    TAB = [NLI() for _ in range(Q)]
    D = defaultdict(set)
    for t, a, b in TAB:
        if t == 1:
            D[a].add(b)
        elif t == 2:
            D[a].discard(b)
        else:
            if b in D[a] and a in D[b]:
                print("Yes")
            else:
                print("No")


if __name__ == "__main__":
    main()
