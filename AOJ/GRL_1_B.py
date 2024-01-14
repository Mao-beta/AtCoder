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


def main():
    N, M, r = NMI()
    STD = EI(M)
    G = BellmanFord(N)
    for s, t, d in STD:
        G.add(s, t, d)
    ans, hasClosedLoop = G.shortest_path(r)

    if hasClosedLoop:
        print("NEGATIVE CYCLE")
        return

    INF = 10 ** 15
    for a in ans:
        print("INF" if a > INF else a)


if __name__ == "__main__":
    main()
