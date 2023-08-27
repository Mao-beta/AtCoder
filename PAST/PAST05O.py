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


def adjlist(n, edges, directed=False, in_origin=1):
    if len(edges) == 0:
        return [[] for _ in range(n)]

    weighted = True if len(edges[0]) > 2 else False
    if in_origin == 1:
        if weighted:
            edges = [[x-1, y-1, w] for x, y, w in edges]
        else:
            edges = [[x-1, y-1] for x, y in edges]

    res = [[] for _ in range(n)]

    if weighted:
        for u, v, c in edges:
            res[u].append([v, c])
            if not directed:
                res[v].append([u, c])

    else:
        for u, v in edges:
            res[u].append(v)
            if not directed:
                res[v].append(u)

    return res


def main():
    N, M = NMI()
    AB = EI(M)
    Q = NI()
    TX = EI(Q)
    G = adjlist(N, AB)
    sz = 3000
    stars = set(i for i in range(N) if len(G) >= sz)
    x2stars = [stars & set(Gi) for Gi in G]
    t1_timings = [[-1] for _ in range(N)]
    t2_timings = [-1 for _ in range(N)]
    notes = [0] * N

    for ti, (t, x) in enumerate(TX):
        x -= 1
        if t == 1:
            if x in stars:
                t1_timings[x].append(ti)
            else:
                for g in G[x]:
                    notes[g] += 1

        else:
            res = notes[x]
            prev_ti = t2_timings[x]
            for g in x2stars[x]:
                res += len(t1_timings[g]) - bisect.bisect_right(t1_timings[g], prev_ti)
            print(res)
            notes[x] = 0
            t2_timings[x] = ti


if __name__ == "__main__":
    main()
