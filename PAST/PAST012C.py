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
    P = [[0] + NLI() for _ in range(3)]

    def mul(f, g):
        n, m = len(f), len(g)
        res = [0] * (n+m-1)
        for i, ff in enumerate(f):
            for j, gg in enumerate(g):
                res[i+j] += ff * gg
        return res

    X = mul(P[0], mul(P[1], P[2]))
    for x in X[1:]:
        print(x / 100**3)


if __name__ == "__main__":
    main()
