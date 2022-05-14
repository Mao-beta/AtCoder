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
    D = [NI() for _ in range(N)]
    D.sort(reverse=True)
    C = [0] * (max(D)+1)
    for d in D:
        C[d] += 1

    for i in range(3):
        Cum = list(accumulate(C))
        C = [0] * (max(D) + 1)

        for d in D:
            r = d // 2
            C[d] += Cum[r] % MOD

    print(sum(C) % MOD)


if __name__ == "__main__":
    main()
