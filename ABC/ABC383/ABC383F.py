import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.set_int_max_str_digits(10**6)
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
    N, X, K = NMI()
    PUC = EI(N)
    C2PU = [[] for _ in range(N+1)]
    for p, u, c in PUC:
        C2PU[c].append([p, u])

    dp0 = [0] * (X+1)
    for c, PUs in enumerate(C2PU):
        if len(PUs) == 0:
            continue
        dp1 = [0] * (X+1)
        for p, u in PUs:
            for x in range(X, -1, -1):
                if x < p:
                    dp1[x] = max(dp1[x], dp0[x])
                else:
                    dp1[x] = max(dp1[x], dp0[x], dp0[x-p] + u + K, dp1[x-p] + u)
        # print(dp0, dp1)
        dp0, dp1 = dp1, dp0
    print(max(dp0))


if __name__ == "__main__":
    main()
