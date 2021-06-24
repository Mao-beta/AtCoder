import sys
import math
from collections import deque
from heapq import heapify, heappop, heappush

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


class Dijkstra():
    """ ダイクストラ法
    重み付きグラフにおける単一始点最短路アルゴリズム

    * 使用条件
        - 負のコストがないこと
        - 有向グラフ、無向グラフともにOK

    * 計算量はO(E*log(V))

    * ベルマンフォード法より高速なので、負のコストがないならばこちらを使うとよい
    """

    class Edge():
        """ 重み付き有向辺 """

        def __init__(self, _to, _cost, _d):
            self.to = _to
            self.cost = _cost
            self.d = _d


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

    def add(self, _from, _to, _cost, _d):
        """ 2頂点と、辺のコストを追加する """
        self.G[_from].append(self.Edge(_to, _cost, _d))
        self._E += 1

    def best_time(self, d):
        sqd = int(math.sqrt(d))
        res_t = -1
        res_c = 10**20
        for i in range(-2, 3):
            t = sqd + i
            if t < 0: continue
            if t + d // (t+1) <= res_c:
                res_c = t + d // (t+1)
                res_t = t
        return res_t, res_c


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
        heapq.heappush(que, (0, s))  # 始点の(最短距離, 頂点番号)をヒープに追加する

        while len(que) != 0:
            cost, v = heapq.heappop(que)
            # キューに格納されている最短経路の候補がdの距離よりも大きければ、他の経路で最短経路が存在するので、処理をスキップ
            if d[v] < cost: continue

            for i in range(len(self.G[v])):
                # 頂点vに隣接する各頂点に関して、頂点vを経由した場合の距離を計算し、今までの距離(d)よりも小さければ更新する
                e = self.G[v][i]  # vのi個目の隣接辺e
                best_t, _ = self.best_time(e.d)

                if cost < best_t:
                    goto_cost = best_t + e.d // (best_t+1) + e.cost
                    if d[e.to] > goto_cost:
                        d[e.to] = goto_cost  # dの更新
                        heapq.heappush(que, (d[e.to], e.to))  # キューに新たな最短経路の候補(最短距離, 頂点番号)の情報をpush

                else:
                    goto_cost = cost + e.d // (cost+1) + e.cost
                    if d[e.to] > goto_cost:
                        d[e.to] = goto_cost  # dの更新
                        heapq.heappush(que, (d[e.to], e.to))
        return d


def main():
    N, M = NMI()
    edges = [NLI() for _ in range(M)]
    graph = Dijkstra(N)
    for a, b, c, d in edges:
        a, b = a-1, b-1
        graph.add(a, b, c, d)
        graph.add(b, a, c, d)

    ans = graph.shortest_path(0)[N-1]
    print(ans if ans != float("inf") else -1)





if __name__ == "__main__":
    main()
