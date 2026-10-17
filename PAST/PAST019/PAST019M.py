import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.set_int_max_str_digits(10**6)
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

from collections import deque


def topological_sort(graph):
    """
    BFSによるトポロジカルソート O(V+E)
    :param graph: 隣接リスト
    :return: 長さnならトポソ可能、そうでなければサイクルあり
    """
    n = len(graph)
    dims = [0] * n
    for i, adj in enumerate(graph):
        for goto, w in adj:
            dims[goto] += 1

    que = deque()
    for i, d in enumerate(dims):
        if d == 0:
            que.append(i)

    res = []
    while que:
        now = que.popleft()
        res.append(now)

        for goto, w in graph[now]:
            dims[goto] -= 1
            if dims[goto] == 0:
                que.append(goto)

    return res


def main():
    N, M = NMI()
    P = NLI()
    UVW = [SLI() for _ in range(M)]
    G = [[] for _ in range(N)]
    RG = [[] for _ in range(N)]
    for u, v, w in UVW:
        u, v = int(u)-1, int(v)-1
        w = float(w)
        G[u].append([v, w])
        RG[v].append([u, w])
    topo = topological_sort(G)
    # print(topo)
    dp = [-1.0] * N
    dp[N-1] = 0.0
    use = set()
    use.add(N-1)
    for v in topo[::-1]:
        if v not in use:
            continue
        for u, w in RG[v]:
            dp[u] = max(dp[u], (dp[v] + P[v]) * w)
            use.add(u)
    if dp[0] < 0:
        print(-1)
        return
    # print(dp)
    print(dp[0] + P[0])


if __name__ == "__main__":
    main()
