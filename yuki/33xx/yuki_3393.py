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


class Dijkstra():
    """ ダイクストラ法
    重み付きグラフにおける単一始点最短路アルゴリズム

    * 使用条件
        - 負のコストがないこと
        - 有向グラフ、無向グラフともにOK

    * 計算量はO(E*log(V))

    * ベルマンフォード法より高速なので、負のコストがないならばこちらを使うとよい
    """

    def __init__(self, V):
        """ 重み付き有向辺
        無向辺を表現したいときは、_fromと_toを逆にした有向辺を加えればよい

        Args:
            V(int): 頂点の数
        """
        self.G = [[] for i in range(V)]  # 隣接リストG[u][i] := 頂点uのi個目の隣接辺
        self._E = 0  # 辺の数
        self._V = V  # 頂点の数

    @property
    def E(self):
        """ 辺数
        無向グラフのときは、辺数は有向グラフの倍になる
        """
        return self._E

    @property
    def V(self):
        """ 頂点数 """
        return self._V

    def add(self, _from, _to, _cost):
        """ 2頂点と、辺のコストを追加する """
        self.G[_from].append([_to, _cost])
        self._E += 1

    def shortest_path(self, s):
        """ 始点sから頂点iまでの最短路を格納したリストを返す
        Args:
            s(int): 始点s
        Returns:
            d(list): d[i] := 始点sから頂点iまでの最短コストを格納したリスト。
                     到達不可の場合、値はfloat("inf")
        """
        import heapq
        que = []  # プライオリティキュー（ヒープ木）
        d = [float("inf")] * self.V
        d[s] = 0
        heapq.heappush(que, 0 * self.V + s)  # 始点の(最短距離, 頂点番号)をヒープに追加する

        while len(que) != 0:
            cost_v = heapq.heappop(que)
            cost, v = divmod(cost_v, self.V)
            # キューに格納されている最短経路の候補がdの距離よりも大きければ、他の経路で最短経路が存在するので、処理をスキップ
            if d[v] < cost: continue

            for i in range(len(self.G[v])):
                # 頂点vに隣接する各頂点に関して、頂点vを経由した場合の距離を計算し、今までの距離(d)よりも小さければ更新する
                e = self.G[v][i]  # vのi個目の隣接辺e
                if d[e[0]] > d[v] + e[1]:
                    d[e[0]] = d[v] + e[1]  # dの更新
                    heapq.heappush(que, d[e[0]] * self.V + e[0])  # キューに新たな最短経路の候補(最短距離, 頂点番号)の情報をpush
        return d


def main():
    N, M, C = NMI()
    UVW = EI(M)
    UVW = [[x-1, y-1, w] for x, y, w in UVW]
    G = Dijkstra(2*N)
    for u, v, w in UVW:
        G.add(u, v, w+C)
        G.add(v, u, w+C)
    D = G.shortest_path(0)
    for u, v, w in UVW:
        G.add(u+N, v+N, w+C)
        G.add(v+N, u+N, w+C)
        G.add(u, v+N, C)
        G.add(v, u+N, C)
    D2 = G.shortest_path(N-1)
    ans = []
    for i in range(1, N):
        res = min(D[i] + min(D2[i], D2[i+N]), D[N-1])
        ans.append(str(res))
    print(*ans, sep="\n")


if __name__ == "__main__":
    main()
