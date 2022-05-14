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
    N, Q = NMI()
    B = list(range(1, N+1))
    P = [0] + list(range(N))

    for _ in range(Q):
        x = NI()
        px = P[x]
        py = px + 1
        if py == N:
            py = px - 1
        y = B[py]
        P[x], P[y] = P[y], P[x]
        B[px], B[py] = B[py], B[px]

    print(*B)


if __name__ == "__main__":
    main()
