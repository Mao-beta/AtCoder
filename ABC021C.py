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
    N = NI()
    a, b = NMI()
    a, b = a-1, b-1
    M = NI()
    XY = [NLI() for _ in range(M)]
    graph = adjlist(N, XY)

    steps = [-2] * N
    que = deque()
    que.append(a)
    steps[a] = 0

    dp = [0] * N
    dp[a] = 1

    while que:
        now = que.popleft()
        step = steps[now]
        for goto in graph[now]:
            if steps[goto] == step - 1:
                dp[now] += dp[goto]
                dp[now] %= MOD
                continue
            if steps[goto] != -2:
                continue
            que.append(goto)
            steps[goto] = step + 1

    print(dp[b])



if __name__ == "__main__":
    main()
