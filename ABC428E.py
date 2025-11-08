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


def adjlist(n, edges, directed=False, in_origin=1) -> list[list[int]]:
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


def diameter(N, graph):
    """
    :param N: 木の頂点数
    :param graph: 木の隣接行列(0-index)
    :return: 直径
    """

    def dfs(start):
        depth = [-1] * N
        depth[start] = 0

        stack = deque()
        stack.append(start)

        while stack:
            now = stack.pop()
            for goto in graph[now]:
                if depth[goto] != -1:
                    continue
                depth[goto] = depth[now] + 1
                stack.append(goto)
        return depth

    depth1 = dfs(0)
    idx = depth1.index(max(depth1))
    depth2 = dfs(idx)
    dia = max(depth2)
    cent = depth2.index(dia // 2)
    depth3 = dfs(cent)

    return cent, depth3


def main():
    N = NI()
    AB = EI(N-1)
    G = adjlist(N, AB)
    cent, depth = diameter(N, G)
    # print(cent, depth)

    starts = [i for i in range(N) if depth[i] == 1]
    cands = defaultdict(list)
    Ms = defaultdict(list)

    for start in starts:
        stack = deque()
        stack.append(start)
        cand = []
        M = [start, 0]

        while stack:
            now = stack.pop()
            cand.append(now)

            if depth[now] > M[1]:
                M = [now, depth[now]]
            elif depth[now] == M[1]:
                M[0] = max(M[0], now)

            for goto in G[now]:
                if depth[goto] <= depth[now]:
                    continue
                stack.append(goto)

        Ms[start] = M
        cands[start] = cand

    # print(Ms)
    # print(cands)
    Ms = sorted(Ms.items(), key=lambda x: (-x[1][1], -x[1][0]))
    Maxcands = set(cands[Ms[0][0]])
    for i in range(N):
        if i not in Maxcands:
            print(Ms[0][1][0] + 1)
        else:
            print(Ms[1][1][0] + 1)


if __name__ == "__main__":
    main()
