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


def adjlist(n, edges, directed=False, in_origin=1):
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
    N, M, K = NMI()
    UV = [NLI() for _ in range(M)]
    A = NLI()
    B = NLI()
    G = adjlist(N, UV)

    que = deque()
    target = 0
    if A[0] == B[0]:
        target = 1
    que.append((0, target))

    seen = [0] * N

    while que:
        now, t = que.popleft()

        if seen[now]:
            continue

        seen[now] = 1

        if now != N-1 and t == K:
            continue
        if now == N-1 and t < K:
            print("No")
            exit()

        for goto in G[now]:
            if seen[goto]:
                continue

            if t >= K:
                que.append((goto, t))

            elif B[t] == A[goto]:
                que.append((goto, t+1))
            else:
                que.appendleft((goto, t))

    print("Yes")


if __name__ == "__main__":
    main()
