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
    L = NLI()

    P = L.copy()
    ans = 10**6
    tmp = 0
    for i in range(N-1):
        if P[i] == i+1:
            P[i], P[i+1] = P[i+1], P[i]
            tmp += 1

    if P[-1] == N:
        tmp += 1
    ans = min(ans, tmp)

    P = L.copy()
    tmp = 0
    for i in range(N-1, 0, -1):
        if P[i] == i + 1:
            P[i], P[i-1] = P[i-1], P[i]
            tmp += 1

    if P[0] == 1:
        tmp += 1
    ans = min(ans, tmp)

    print(ans)


if __name__ == "__main__":
    main()
