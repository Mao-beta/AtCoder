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
    N = NI()
    AB = [NLI() for _ in range(N-1)]
    graph = adjlist_nond_1to0(N, AB)

    pars = [-1] * N

    def rec(now):
        b, w = 1, 1
        for goto in graph[now]:
            if goto == pars[now]:
                continue

            pars[goto] = now
            gb, gw = rec(goto)
            b = b * gw % MOD
            w = w * (gb + gw) % MOD

        return b, w

    b, w = rec(0)
    print((b + w) % MOD)


if __name__ == "__main__":
    main()
