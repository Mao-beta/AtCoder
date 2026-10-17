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
        for goto in adj:
            dims[goto] += 1

    que = deque()
    for i, d in enumerate(dims):
        if d == 0:
            que.append(i)

    res = []
    while que:
        now = que.popleft()
        res.append(now)

        for goto in graph[now]:
            dims[goto] -= 1
            if dims[goto] == 0:
                que.append(goto)

    return res


def main():
    N, M = NMI()
    AB = EI(M)

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

    G = adjlist(N, AB, directed=True)
    topo = topological_sort(G)
    if len(topo) == N:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
