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

    D = defaultdict(int)

    def f(x):
        if x == 0:
            return 1

        p, q = x//3, x//2
        f3 = D[p]
        if f3 == 0:
            f3 = f(p)

        f2 = D[q]
        if f2 == 0:
            f2 = f(q)

        res = f2 + f3
        D[x] = res
        return res

    print(f(N))



if __name__ == "__main__":
    main()
