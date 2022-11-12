import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

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


def main(H, W, A):

    TA = [x for x in zip(*A)]

    G = [[] for _ in range(W)]

    for row in A:
        row_i = [(x, i) for i, x in enumerate(row)]
        row_i.sort()
        n = len(row_i)
        # print("HW", H, W)
        # print("n", n)
        for i in range(n-1):
            xa, ia = row_i[i]
            xb, ib = row_i[i+1]
            # print(xa, ia, xb, ib)
            if xa == 0 or xa == xb : continue
            else:
                G[ia].append(ib)

    topo_h = topological_sort(G)

    GG = [[] for _ in range(H)]

    for row in TA:
        row_i = [(x, i) for i, x in enumerate(row)]
        row_i.sort()
        n = len(row_i)
        # print("HW", H, W)
        # print("n", n)
        for i in range(n - 1):
            xa, ia = row_i[i]
            xb, ib = row_i[i + 1]
            # print(xa, ia, xb, ib)
            if xa == 0 or xa == xb:
                continue
            else:
                GG[ia].append(ib)

    topo_w = topological_sort(GG)

    if len(topo_h) == H and len(topo_w) == W:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    H, W = NMI()
    A = [tuple(NMI()) for _ in range(H)]
    main(H, W, A)

    # import random
    #
    # for _ in range(50):
    #     H = random.randint(2, 200)
    #     W = random.randint(2, 200)
    #     A = [[random.randint(0, H*W) for _ in range(W)] for _ in range(H)]
    #
    #     # print(H, W)
    #     # print(*A, sep="\n")
    #     main(H, W, A)
