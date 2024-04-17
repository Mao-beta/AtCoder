import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.set_int_max_str_digits(10 ** 6)
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



class LowLink:
    def __init__(self, N, edges):
        """
        無向グラフの非再帰LowLink
        LL.bridges: 橋のset
        LL.aps: 関節点のset
        :param N: 頂点数
        :param edges: 辺
        """
        self.INF = 10 ** 16
        self.N = N
        self.edges = edges
        self.adj = [[] for _ in range(N)]
        for a, b in edges:
            self.adj[a].append(b)
            self.adj[b].append(a)

        self.k = 0
        self.ord = [None] * N   # seen を兼ねる
        self.low = [self.INF] * N
        self.finished = [False] * N
        self.aps = set()
        self.bridges = set()
        for u in range(N):
            if self.ord[u] is None:
                self.dfs(u)

    def dfs(self, s):
        todo = [(s, -1)]  # 初期探索場所をpush（スタート地点の帰りがけは不要）
        num_child_of_root = 0
        while todo:
            u, par = todo.pop()    # LIFOでpop
            if u >= 0:
                if self.finished[u]:
                    continue
                # 行きがけ順の処理（DFS木の訪問順にordを付与）
                self.k += 1
                self.ord[u] = self.k
                self.low[u] = self.k
                # 次の位置を探索する
                for v in self.adj[u]:
                    if v == par:
                        continue
                    if self.ord[v] is not None:
                        # 後退辺を発見したら、lowを更新する
                        self.low[u] = min(self.low[u], self.low[v])
                        continue
                    todo.append((~v, u)) # 帰りがけはビット反転
                    todo.append((v, u))
            else:
                v = ~u   # ビット反転を戻す
                if self.finished[v]:
                    continue
                self.finished[v] = True
                # 帰りがけ順の処理（後退辺の影響を逆伝搬する）
                self.low[par] = min(self.low[par], self.low[v])
                # 頂点が関節点となる条件
                if par == s:
                    num_child_of_root += 1
                elif self.ord[par] <= self.low[v]:
                    self.aps.add(par)
                # 辺が橋となる条件
                if self.ord[par] < self.low[v]:
                    self.bridges.add((min(par, v), max(par, v)))
            if num_child_of_root >= 2:
                self.aps.add(s)
        return



def main():
    # https://atcoder.jp/contests/abc075/tasks/abc075_c
    N, M = map(int, input().split())
    S = [list(map(int, input().split())) for _ in range(M)]
    S = [[x-1, y-1] for x, y in S]

    LL = LowLink(N, S)
    print(len(LL.bridges))
    # LowLink().aps は関節点


if __name__ == "__main__":
    main()
