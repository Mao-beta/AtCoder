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
    P = NLI()
    L = []
    for i in range(N-1, 0, -1):
        L.append(P[i])
        L.sort()
        if P[i-1] > P[i]:
            idx = bisect.bisect_left(L, P[i-1])
            t = L[idx-1]
            L.pop(idx-1)
            L.append(P[i-1])
            P[i-1] = t
            P[i:] = sorted(L, reverse=True)
            print(*P)
            exit()


if __name__ == "__main__":
    main()
