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
    N, K = NMI()
    A = NLI()
    Q = NI()
    LR = EI(Q)

    S = [[0]*K for _ in range(N+1)]
    for i in range(N):
        for k in range(K):
            S[i+1][k] = S[i][k] + A[i] * (i%K == k)

    for l, r in LR:
        l -= 1
        G = [S[r][k] - S[l][k] for k in range(K)]
        if len(set(G)) == 1:
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    main()
