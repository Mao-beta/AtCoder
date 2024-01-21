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
    N, Q = NMI()
    S = SI() + "#"
    P = [0] * N
    for i in range(N):
        if S[i] == S[i+1]:
            P[i] = 1
    C = list(accumulate([0]+P))
    for _ in range(Q):
        l, r = NMI()
        l -= 1
        print(C[r-1]-C[l])


if __name__ == "__main__":
    main()
