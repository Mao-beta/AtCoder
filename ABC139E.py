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


def topological_sort(graph):
    """
    BFSによるトポロジカルソート O(V+E)
    :param graph: 隣接リスト
    :return: 長さnならトポソ可能、そうでなければサイクルあり
    """
    n = len(graph)
    dims = [0] * n
    for i, adj in enumerate(graph):
        for goto in adj:
            dims[goto] += 1

    steps = [0] * n
    que = deque()
    for i, d in enumerate(dims):
        if d == 0:
            que.append((i, 1))

    res = []
    while que:
        now, s = que.popleft()
        res.append(now)
        s = max(steps[now], s)
        steps[now] = s

        for goto in graph[now]:
            dims[goto] -= 1
            if dims[goto] == 0:
                que.append((goto, s+1))

    return res, max(steps)


def compress(S):
    """ 座標圧縮 """

    S = set(S)
    zipped, unzipped = {}, {}
    for i, a in enumerate(sorted(S)):
        zipped[a] = i
        unzipped[i] = a
    return zipped, unzipped


def main():
    N = NI()
    A = [NLI() for _ in range(N)]

    S = set()
    for i in range(1, N+1):
        for j in range(i+1, N+1):
            S.add((i, j))

    Z, UZ = compress(S)
    M = len(Z)
    graph = [[] for _ in range(M)]

    seen = set()
    for i, row in enumerate(A, start=1):
        pv = None
        for j in row:
            ti, tj = min(i, j), max(i, j)
            v = Z[(ti, tj)]
            if pv is not None and (pv, v) not in seen:
                graph[pv].append(v)
                seen.add((pv, v))
            pv = v

    res, ans = topological_sort(graph)
    if len(res) == M:
        print(ans)
    else:
        print(-1)


if __name__ == "__main__":
    main()
