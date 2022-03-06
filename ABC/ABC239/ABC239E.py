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


def adjlist_nond_1to0(n, edges):
    res = [[] for _ in range(n)]
    for a, b in edges:
        a, b = a - 1, b - 1
        res[a].append(b)
        res[b].append(a)
    return res


def main():
    N, Q = NMI()
    X = NLI()
    AB = [NLI() for _ in range(N-1)]
    VK = [NLI() for _ in range(Q)]
    VK = [[x-1, y] for x, y in VK]

    graph = adjlist_nond_1to0(N, AB)

    H = [[] for _ in range(N)]

    seen = [0] * N

    def rec(now):
        seen[now] = 1
        h = [X[now]]

        for goto in graph[now]:
            if seen[goto]: continue
            R = rec(goto)
            h += R

        h.sort(reverse=True)
        h = h[:20].copy()
        H[now] = h

        return h

    rec(0)
    # print(H)
    ans = [0] * Q

    for v, k in VK:
        print(H[v][k-1])


if __name__ == "__main__":
    main()
