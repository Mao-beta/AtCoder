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


from typing import List, Tuple

class BellmanFord():
    """ ベルマンフォード法
        重み付き有向グラフにおける単一始点最短路アルゴリズム

        * 使用条件
            - DAG（有向グラフで閉路を持たない）であること
            - 負のコストがあってもOK

        * 負の閉路がある場合、最短路は求まらないが、負の閉路の検出はできる

        * 計算量はO(V*E)
    """
    class Edge():
        """ 重み付き有向辺 """

        def __init__(self, _from, _to, _cost):
            self.from_ = _from
            self.to = _to
            self.cost = _cost

    def __init__(self, n):
        self.V = n
        self.edges = []  # 辺

    def add(self, _from, _to, _cost):
        """ 2頂点と、辺のコストを追加する """
        self.edges.append(self.Edge(_from, _to, _cost))

    def shortest_path(self, s) -> Tuple[List[int], bool]:
        """
        頂点sからの最短経路長のリスト
        到達不可能ならINF
        負の閉路があればhasClosedLoop == Trueで返ってくる
        :return: res, hasClosedLoop
        """
        INF = float("inf")
        res = [INF] * self.V
        res[s] = 0
        hasClosedLoop = False

        for cnt in range(self.V):
            hasClosedLoop = False
            for edge in self.edges:
                fr, to, c = edge.from_, edge.to, edge.cost
                if res[to] > res[fr] + c:
                    res[to] = res[fr] + c
                    hasClosedLoop = True

        return res, hasClosedLoop


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
    N, M, P = NMI()
    ABC = EI(M)
    ABC_rev = [[b, a, c] for a, b, c in ABC]

    # 0から到達可能な頂点と、Nに到達可能な頂点をそれぞれもとめる
    G = adjlist(N, ABC, directed=True)
    R = adjlist(N, ABC_rev, directed=True)

    def bfs(s, graph):
        steps = [-1] * N
        que = deque()
        que.append(s)
        steps[s] = 0
        while que:
            now = que.popleft()
            step = steps[now]
            for goto, c in graph[now]:
                if steps[goto] != -1:
                    continue
                que.append(goto)
                steps[goto] = step + 1

        V = set()
        for v, s in enumerate(steps):
            if s >= 0:
                V.add(v)
        return V

    valid = bfs(0, G) & bfs(N-1, R)

    Bell = BellmanFord(N)
    for a, b, c in ABC:
        a, b = a-1, b-1
        if a in valid and b in valid:
            Bell.add(a, b, P-c)

    d, bad = Bell.shortest_path(0)
    # print(d, bad)
    if bad:
        print(-1)
    else:
        print(-d[-1] if -d[-1] >= 0 else 0)


if __name__ == "__main__":
    main()
