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
    N = NI()
    L = 2*N+1
    A = EI(L)
    INF = 10**10 * L**2

    def f(h, w):
        return h * L + w

    def g(idx):
        return divmod(idx, L)

    DH = [1, -1, 0, 0, 1, 1, -1, -1]
    DW = [0, 0, 1, -1, 1, -1, 1, -1]

    def Dijkstra(starts):
        C = [INF] * L**2
        hq = []

        for start in starts:
            h, w = g(start)
            C[start] = A[h][w]
            heappush(hq, (C[start], start))

        while hq:
            cost, now = heappop(hq)
            if C[now] < cost:
                continue

            h, w = g(now)

            for dh, dw in zip(DH, DW):
                nh, nw = h+dh, w+dw
                if nh < 0 or L <= nh or nw < 0 or L <= nw:
                    continue
                ni = f(nh, nw)
                a = A[nh][nw]
                if a < 0:
                    continue
                if C[ni] > cost + a:
                    C[ni] = cost + a
                    heappush(hq, (C[ni], ni))
        return C


    starts = []
    ends = []
    for h in range(L):
        for w in range(L):
            if 0 < h < L-1 and 0 < w < L-1:
                continue
            if w < N:
                starts.append(f(h, w))
            else:
                ends.append(f(h, w))

    ans = INF
    C = Dijkstra(starts)
    for e in ends:
        ans = min(ans, C[e])

    print(ans)


if __name__ == "__main__":
    main()
