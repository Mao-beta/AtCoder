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


def is_bipartite(N, graph):
    colors = [-1] * N

    def dfs_paint_01_color(start):
        if colors[start] != -1:
            return False, []

        stack = deque()
        stack.append(start)

        colors[start] = 0

        sub_res = True
        sub_colors = [0, 0]

        while stack:
            now = stack.pop()
            c = colors[now]
            sub_colors[c] += 1

            for goto in graph[now]:
                if colors[goto] == 1 - c:
                    continue
                elif colors[goto] == c:
                    sub_res = False
                    continue
                stack.append(goto)
                colors[goto] = 1 - c

        return sub_res, sub_colors

    res1 = []
    res2 = []
    for s in range(N):
        X = dfs_paint_01_color(s)
        if X[1] == []:
            continue
        res1.append(X[0])
        res2.append(X[1])

    return res1, res2


def main():
    #### 未AC ######

    N, M = NMI()
    AB = [NLI() for _ in range(M)]
    AB = [[x-1, y-1] for x, y in AB]
    G = adjlist(N, AB, in_origin=0)

    # 各連結成分について2部グラフかどうか判定する
    # 2部グラフでない成分の頂点には余り0をあてるしかない
    # 2部グラフは「各部の頂点数のどちらかが1, どちらかが2」になるか、全部0になる
    # うまく割り当てて長さNの順列における個数と一致させられるか？

    lims = [0] * 3
    for i in range(1, N+1):
        lims[i%3] += 1

    # 1がi個、2がj個
    dp = [[0]*((N+6)//3) for _ in range(((N+6)//3))]
    dp[0][0] = 1

    Bip, U = is_bipartite(N, G)
    for b, c in zip(Bip, U):
        if not b: continue
        a, b = c

        for i in range((N+6)//3):
            for j in range((N+6)//3):
                if dp[i][j] == 0:
                    continue

                if i+a < (N+6)//3 and j+b < (N+6)//3:
                    dp[i+a][j+b] = 1
                if i+b < (N+6)//3 and j+a < (N+6)//3:
                    dp[i + b][j + a] = 1

    # print(*dp, sep="\n")

    if dp[lims[1]][lims[2]]:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
