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
    N, M = NMI()
    trains = EI(M)
    G = [[] for _ in range(N)]
    for l, d, k, c, a, b in trains:
        a, b = a-1, b-1
        G[b].append([a, l, d, k, c])
    INF = 10**19
    ans = [-INF] * N
    ans[N-1] = INF
    D = []
    heappush(D, [-INF, N-1])
    while D:
        t, b = heappop(D)
        t = -t
        if t < ans[b]:
            continue
        for a, l, d, k, c in G[b]:
            if l + (k-1) * d + c <= t:
                x = l + (k-1) * d
            elif l + c > t:
                continue
            else:
                i = (t-c-l) // d
                x = l + i * d
            if ans[a] >= x:
                continue
            ans[a] = x
            heappush(D, [-x, a])

    for a in ans[:-1]:
        if a < 0:
            print("Unreachable")
        else:
            print(a)



if __name__ == "__main__":
    main()
