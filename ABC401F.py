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
    idx2 = depth2.index(max(depth2))
    depth3 = dfs(idx2)
    depth = [max(x, y) for x, y in zip(depth2, depth3)]
    return max(depth2), depth


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

def main():
    N1 = NI()
    UV1 = EI(N1-1)
    N2 = NI()
    UV2 = EI(N2-1)
    G1 = adjlist(N1, UV1)
    G2 = adjlist(N2, UV2)
    dia1, depth1 = diameter(N1, G1)
    dia2, depth2 = diameter(N2, G2)
    C1 = [0] * (N1+1)
    C2 = [0] * (N2+1)
    for i, d in enumerate(depth1):
        C1[d] += 1
    num = 0
    val = 0
    for i, d in enumerate(depth2):
        C2[d] += 1
    d2 = N2+1
    mdia = max(dia1, dia2)
    ans = 0
    for d1 in range(N1+1):
        while d2 > 0 and d2 > mdia - (d1+1) +1:
            d2 -= 1
            num += C2[d2]
            val += C2[d2] * d2
        ans += mdia * (N2-num) * C1[d1] + (val + (d1+1)*num) * C1[d1]
    print(ans)


if __name__ == "__main__":
    main()
