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
    A = NLI()
    INF = 10**10

    taka = -INF
    for ta in range(N):
        aoki = -INF
        B = []

        for ao in range(N):
            if ta == ao: continue
            if ta < ao:
                T = A[ta: ao+1]
            else:
                T = A[ao: ta+1]

            aop = sum(T[1::2])
            if aop > aoki:
                aoki = aop
                B = T.copy()

        # print(ta, ao, B, sum(B[0::2]))
        taka = max(taka, sum(B[0::2]))

    print(taka)



if __name__ == "__main__":
    main()
