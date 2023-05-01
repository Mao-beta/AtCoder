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
    T = NI()
    for _ in range(T):
        N, M = NMI()
        C = NLI()
        UV = EI(M)
        G = adjlist(N, UV)

        que = deque()
        que.append((0, N-1))
        seen = [[-1]*N for _ in range(N)]
        seen[0][N-1] = 0

        while que:
            t, a = que.popleft()

            for goto_t in G[t]:
                for goto_a in G[a]:
                    if seen[goto_t][goto_a] >= 0:
                        continue

                    if C[goto_t] == C[goto_a]:
                        continue
                    seen[goto_t][goto_a] = seen[t][a] + 1
                    que.append((goto_t, goto_a))

        print(seen[N-1][0])


if __name__ == "__main__":
    main()
