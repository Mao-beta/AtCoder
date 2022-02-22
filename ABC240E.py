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
    UV = [NLI() for _ in range(N-1)]
    graph = adjlist_nond_1to0(N, UV)

    seen = [0] * N
    parents = [0] * N
    parents[0] = -1
    topo = []
    x = [1]
    L = [1] * N
    R = [1] * N

    def rec(now):
        seen[now] = 1
        topo.append(now)

        # print(now, graph[now])

        if now != 0 and len(graph[now]) <= 1:
            L[now] = x[0]
            R[now] = x[0]
            x[0] += 1
            return L[now], R[now]

        ll = None
        rr = None
        for goto in graph[now]:
            if seen[goto]: continue
            parents[goto] = now
            if ll is None:
                ll, rr = rec(goto)
            else:
                l, r = rec(goto)
                ll = min(ll, l)
                rr = max(rr, r)

        L[now] = ll
        R[now] = rr
        return L[now], R[now]

    rec(0)
    for l, r in zip(L, R):
        print(l, r)


if __name__ == "__main__":
    main()
