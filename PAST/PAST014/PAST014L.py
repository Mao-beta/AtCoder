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
    G = adjlist(N, AB, directed=True)
    in_deg = [0] * N
    for a, b in AB:
        a, b = a-1, b-1
        in_deg[b] += 1

    hq = []
    seen = [0] * N
    ans = []
    for i in range(N):
        if in_deg[i] == 0:
            heappush(hq, i)
            seen[i] = 1

    while hq:
        now = heappop(hq)
        ans.append(now+1)

        for g in G[now]:
            if seen[g]:
                continue
            in_deg[g] -= 1
            if in_deg[g] == 0:
                heappush(hq, g)
                seen[g] = 1

    print(*ans)


if __name__ == "__main__":
    main()
