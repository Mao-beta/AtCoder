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
    N, M = NMI()
    P = NLI()
    L = NLI()
    D = NLI()
    X = []
    INF = 10**20
    for p in P:
        X.append([p, INF])
    for l, d in zip(L, D):
        X.append([l, d])
    X.sort()

    ans = 0
    hq = []
    for a, b in X:
        if b != INF:
            heappush(hq, -b)
        else:
            if hq:
                d = -heappop(hq)
                a -= d
            ans += a

    print(ans)


if __name__ == "__main__":
    main()
