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
    A = NLI() + [0]*100
    AS = sum(A)
    ans = 10**9
    for K in range(1, 200, 2):
        P = [0] * K
        for k in range(K):
            P[k] = min(k+1, K-k)
        PS = sum(P)
        if AS < PS:
            break
        over = 0
        for p, a in zip(P, A):
            over += max(a-p, 0)
        ans = min(ans, over + sum(A[K:]))
    print(ans)


if __name__ == "__main__":
    main()
