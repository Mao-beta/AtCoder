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
    B = SLI()
    N = NI()
    A = [SI() for _ in range(N)]
    table = str.maketrans(
        {s: str(i) for i, s in enumerate(B)}
    )
    T = [[int(a.translate(table)), a] for a in A]
    T.sort()
    for t, a in T:
        print(a)


if __name__ == "__main__":
    main()
