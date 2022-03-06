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
    N = NI()
    C = NLI()
    A = [(c, i) for i, c in enumerate(C, start=1)]
    A.sort()

    ans = 0
    B = []
    for c, i in A:
        for b in B:
            i = min(i, i^b)
        if i > 0:
            B.append(i)
            ans += c
    print(ans)


if __name__ == "__main__":
    main()
