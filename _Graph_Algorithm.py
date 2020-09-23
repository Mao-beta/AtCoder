import sys
import math
from collections import defaultdict
from collections import deque

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

        def __init__(self, _to, _cost):
            self.to = _to
            self.cost = _cost

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
        self.G[_from].append(self.Edge(_to, _cost))
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
        heapq.heappush(que, (0, s))  # 始点の(最短距離, 頂点番号)をヒープに追加する

        while len(que) != 0:
            cost, v = heapq.heappop(que)
            # キューに格納されている最短経路の候補がdの距離よりも大きければ、他の経路で最短経路が存在するので、処理をスキップ
            if d[v] < cost: continue

            for i in range(len(self.G[v])):
                # 頂点vに隣接する各頂点に関して、頂点vを経由した場合の距離を計算し、今までの距離(d)よりも小さければ更新する
                e = self.G[v][i]  # vのi個目の隣接辺e
                if d[e.to] > d[v] + e.cost:
                    d[e.to] = d[v] + e.cost  # dの更新
                    heapq.heappush(que, (d[e.to], e.to))  # キューに新たな最短経路の候補(最短距離, 頂点番号)の情報をpush
        return d


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

    def __init__(self):
        self.edges = []  # 辺
        self.v_set = set()  # 頂点の集合

    @property
    def E(self):
        """ 辺数 """
        return len(self.edges)

    @property
    def V(self):
        """ 頂点数 """
        return len(self.v_set)

    def add(self, _from, _to, _cost):
        """ 2頂点と、辺のコストを追加する """
        self.edges.append(self.Edge(_from, _to, _cost))
        self.v_set.add(_from)
        self.v_set.add(_to)

    def shortest_path(self, s):
        """ 始点sから頂点iまでの最短路を格納したリストを返す
        Args:
            s(int): 始点s
        Returns:
            d(list): d[i] := 始点sから頂点iまでの最短路
        """
        d = [float("inf")] * self.V
        d[s] = 0

        while True:
            do_update = False
            for i in range(self.E):
                e = self.edges[i]
                if d[e.from_] != float("inf") and d[e.to] > d[e.from_] + e.cost:
                    d[e.to] = d[e.from_] + e.cost
                    do_update = True

            if not do_update: break

        return d

    def exist_negative_loop(self):
        """ 負の閉路が存在するか否か
        Returns:
            (bool): 負の閉路が存在する(True)/しない(False)
        """
        d = [0] * self.V
        for i in range(self.V):
            for j in range(self.E):
                e = self.edges[j]
                if d[e.to] > d[e.from_] + e.cost:
                    d[e.to] = d[e.from_] + e.cost
                    # n回目にも更新があるなら負の閉路が存在する
                    if i == self.V - 1: return True
        return False


class mf_graph:
    def __init__(self, n=0):
        self._n = n
        self.g = [[] for _ in range(n)]
        self.pos = []

    def add_edge(self, frm, to, cap):
        m = len(self.pos)
        e1 = mf_graph._edge(to, cap)
        e2 = mf_graph._edge(frm, 0)
        e1.rev = e2
        e2.rev = e1
        self.pos.append(e1)
        self.g[frm].append(e1)
        self.g[to].append(e2)
        return m

    class edge:
        def __init__(self, frm, to, cap, flow):
            self.frm = frm
            self.to = to
            self.cap = cap
            self.flow = flow

        def __iter__(self):
            yield self.frm
            yield self.to
            yield self.cap
            yield self.flow

    def get_edge(self, i):
        e1 = self.pos[i]
        e2 = e1.rev
        return mf_graph.edge(e2.to, e1.to, e1.cap + e2.cap, e2.cap)

    def edges(self):
        return [self.get_edge(i) for i in range(len(self.pos))]

    def change_edge(self, i, new_cap, new_flow):
        e = self.pos[i]
        e.cap = new_cap - new_flow
        e.rev.cap = new_flow

    def flow(self, s, t, flow_limit=0XFFFFFFFFFFFFFFF):
        g = self.g
        flow = 0
        while flow < flow_limit:
            level = [-1] * self._n
            level[s] = 0
            que = [None] * self._n
            ql = 0
            qr = 1
            que[0] = s
            unreached = True
            while unreached and ql < qr:
                v = que[ql]
                ql += 1
                for e in g[v]:
                    to = e.to
                    if e.cap and level[to] < 0:
                        level[to] = level[v] + 1
                        if to == t:
                            unreached = False
                            break
                        que[qr] = to
                        qr += 1
            if unreached:
                return flow
            ptr = [len(es) for es in g]
            stack = []
            v = t
            up = flow_limit - flow
            res = 0
            while True:
                if v == s or not ptr[v]:
                    if v == s:
                        res = up
                    while stack:
                        tmp = res
                        e, up, res = stack.pop()
                        e.cap -= tmp
                        e.rev.cap += tmp
                        res += tmp
                        if res < up:
                            v = e.to
                            break
                    else:
                        flow += res
                        break
                i = ptr[v]
                while i:
                    i -= 1
                    e = g[v][i]
                    if level[e.to] == level[v] - 1 and e.rev.cap:
                        ptr[v] = i
                        stack.append((e.rev, up, res))
                        v = e.to
                        up = min(up, e.rev.cap)
                        res = 0
                        break
                else:
                    ptr[v] = i
        return flow

    def min_cut(self, s):
        visited = [False] * self._n
        que = [None] * self._n
        ql = 0
        qr = 1
        que[0] = s
        visited[s] = True
        while ql < qr:
            p = que[ql]
            ql += 1
            for e in self.g[p]:
                if e.cap and not visited[e.to]:
                    visited[e.to] = True
                    que[qr] = e.to
                    qr += 1
        return visited

    class _edge:
        def __init__(self, to, cap):
            self.to = to
            self.cap = cap


def main():
    pass


if __name__ == "__main__":
    main()