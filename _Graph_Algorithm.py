import sys
import math
from collections import defaultdict
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
INF = 10 ** 20
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


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


from collections import deque
def diameter(N, graph):
    """
    :param N: 木の頂点数
    :param graph: 木の隣接行列(1-index)
    :return: 直径
    """

    def dfs(start):
        depth = [-1] * (N+1)
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

    depth1 = dfs(1)
    idx = depth1.index(max(depth1))
    depth2 = dfs(idx)

    return max(depth2)


class Dijkstra:
    """ ダイクストラ法
    重み付きグラフにおける単一始点最短路アルゴリズム

    * 使用条件
        - 負のコストがないこと
        - 有向グラフ、無向グラフともにOK

    * 計算量はO(E*log(V))

    * ベルマンフォード法より高速なので、負のコストがないならばこちらを使うとよい
    """

    def __init__(self, n, edges, is_one_index=False):
        """
        :param n: 頂点数 頂点は数字じゃなくてもよい
        :param edges: [from, to, cost]の形の辺のList
        :param is_one_index: 1-indexならTrue
        """
        from collections import defaultdict

        self.n = n
        self.edges = edges
        self.INF = 10**20

        self.graph = defaultdict(list)
        for a, b, c in edges:
            if is_one_index:
                a, b = a-1, b-1
            self.graph[a].append((b, c))

    def get_mincost(self, start):
        from collections import defaultdict
        import heapq

        hq = []
        heapq.heappush(hq, (0, start))

        res = defaultdict(lambda: self.INF)
        temp_costs = defaultdict(lambda: self.INF)

        while hq:
            now_c, now = heapq.heappop(hq)
            if res[now] < now_c:
                continue

            res[now] = now_c
            for goto, cost in self.graph[now]:
                goto_c = now_c + cost

                if temp_costs[goto] > goto_c:
                    heapq.heappush(hq, (goto_c, goto))
                    temp_costs[goto] = goto_c

        return res


class __Dijkstra():
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


"""
燃やす埋める問題について
各頂点をRBの二色に塗り分ける
R->Bの辺の重みを全部足したもの（コスト>=0）を最小にする
報酬を得るときは先にもらっておいて否定形をコストとする

異色でコスト条件、同色で報酬条件は可能　逆は一般には難しい(二部グラフなら反転すれば可能かも)
異色でコストはR->Bにコストの辺を貼る
両方Rで報酬：報酬もらっておいて, S->Z: cost, Z->X, Y: inf
両方Bで報酬：報酬もらっておいて, Z->T: cost, X, Y->Z: inf
"""


# ACL_maxflow(Dinic)
from typing import NamedTuple, Optional, List, cast
class MFGraph:
    class Edge(NamedTuple):
        src: int
        dst: int
        cap: int
        flow: int

    class _Edge:
        def __init__(self, dst: int, cap: int) -> None:
            self.dst = dst
            self.cap = cap
            self.rev: Optional[MFGraph._Edge] = None

    def __init__(self, n: int) -> None:
        self._n = n
        self._g: List[List[MFGraph._Edge]] = [[] for _ in range(n)]
        self._edges: List[MFGraph._Edge] = []

    def add_edge(self, src: int, dst: int, cap: int) -> int:
        assert 0 <= src < self._n
        assert 0 <= dst < self._n
        assert 0 <= cap
        m = len(self._edges)
        e = MFGraph._Edge(dst, cap)
        re = MFGraph._Edge(src, 0)
        e.rev = re
        re.rev = e
        self._g[src].append(e)
        self._g[dst].append(re)
        self._edges.append(e)
        return m

    def get_edge(self, i: int) -> Edge:
        assert 0 <= i < len(self._edges)
        e = self._edges[i]
        re = cast(MFGraph._Edge, e.rev)
        return MFGraph.Edge(
            re.dst,
            e.dst,
            e.cap + re.cap,
            re.cap
        )

    def edges(self) -> List[Edge]:
        return [self.get_edge(i) for i in range(len(self._edges))]

    def change_edge(self, i: int, new_cap: int, new_flow: int) -> None:
        assert 0 <= i < len(self._edges)
        assert 0 <= new_flow <= new_cap
        e = self._edges[i]
        e.cap = new_cap - new_flow
        assert e.rev is not None
        e.rev.cap = new_flow

    def flow(self, s: int, t: int, flow_limit: Optional[int] = None) -> int:
        assert 0 <= s < self._n
        assert 0 <= t < self._n
        assert s != t
        if flow_limit is None:
            flow_limit = cast(int, sum(e.cap for e in self._g[s]))

        current_edge = [0] * self._n
        level = [0] * self._n

        def fill(arr: List[int], value: int) -> None:
            for i in range(len(arr)):
                arr[i] = value

        def bfs() -> bool:
            fill(level, self._n)
            queue = []
            q_front = 0
            queue.append(s)
            level[s] = 0
            while q_front < len(queue):
                v = queue[q_front]
                q_front += 1
                next_level = level[v] + 1
                for e in self._g[v]:
                    if e.cap == 0 or level[e.dst] <= next_level:
                        continue
                    level[e.dst] = next_level
                    if e.dst == t:
                        return True
                    queue.append(e.dst)
            return False

        def dfs(lim: int) -> int:
            stack = []
            edge_stack: List[MFGraph._Edge] = []
            stack.append(t)
            while stack:
                v = stack[-1]
                if v == s:
                    flow = min(lim, min(e.cap for e in edge_stack))
                    for e in edge_stack:
                        e.cap -= flow
                        assert e.rev is not None
                        e.rev.cap += flow
                    return flow
                next_level = level[v] - 1
                while current_edge[v] < len(self._g[v]):
                    e = self._g[v][current_edge[v]]
                    re = cast(MFGraph._Edge, e.rev)
                    if level[e.dst] != next_level or re.cap == 0:
                        current_edge[v] += 1
                        continue
                    stack.append(e.dst)
                    edge_stack.append(re)
                    break
                else:
                    stack.pop()
                    if edge_stack:
                        edge_stack.pop()
                    level[v] = self._n
            return 0

        flow = 0
        while flow < flow_limit:
            if not bfs():
                break
            fill(current_edge, 0)
            while flow < flow_limit:
                f = dfs(flow_limit - flow)
                flow += f
                if f == 0:
                    break
        return flow

    def min_cut(self, s: int) -> List[bool]:
        visited = [False] * self._n
        stack = [s]
        visited[s] = True
        while stack:
            v = stack.pop()
            for e in self._g[v]:
                if e.cap > 0 and not visited[e.dst]:
                    visited[e.dst] = True
                    stack.append(e.dst)
        return visited


"""
class Dinic:
    __slots__ = ["n", "graph", "level", "it"]

    class Edge:
        def __init__(self, to, cap, rev=None):
            self.to = to
            self.cap = cap
            self.rev = rev

    def __init__(self, n):
        self.n = n
        self.graph = [[] for i in range(n)]
        self.level = [self.n] * self.n
        self.it = [0] * self.n

    def add_edge(self, fr, to, cap=1):
        forward = self.Edge(to, cap, None)
        forward.rev = backward = self.Edge(fr, 0, forward)
        self.graph[fr].append(forward)
        self.graph[to].append(backward)

    def bfs(self, s, t):
        graph = self.graph

        for i in range(self.n):
            self.level[i] = self.n

        level = self.level
        q = deque([s])
        level[s] = 0
        while q:
            x = q.popleft()
            lx = level[x] + 1
            for e in graph[x]:
                y = e.to
                if e.cap and level[y] > lx:
                    level[y] = lx
                    if y == t:
                        return True
                    q.append(y)
        return False

    def dfs(self, s, t, f):
        graph = self.graph
        level = self.level
        it = self.it
        q = deque([t])
        while q:
            x = q[-1]
            if x == s:
                q.pop()
                for y in q:
                    cap = graph[y][it[y]].rev.cap
                    if cap < f:
                        f = cap
                for y in q:
                    e = graph[y][it[y]]
                    e.cap += f
                    e.rev.cap -= f
                return f
            lx = level[x] - 1
            while it[x] < len(graph[x]):
                e = graph[x][it[x]]
                y = e.to
                rev = e.rev
                if rev.cap == 0 or lx != level[y]:
                    it[x] += 1
                    continue
                q.append(y)
                break
            if it[x] == len(graph[x]):
                q.pop()
                level[x] = self.n
        return 0

    def flow(self, s, t):
        flow = 0
        while self.bfs(s, t):
            for i in range(self.n):
                self.it[i] = 0
            f = self.dfs(s, t, float("inf"))
            while f:
                flow += f
                f = self.dfs(s, t, float("inf"))
        return flow
"""



from heapq import heappush, heappop
class MinCostFlow:
    """最小費用流"""
    INF = 10**18

    def __init__(self, N):
        self.N = N
        self.G = [[] for i in range(N)]

    def add_edge(self, fr, to, cap, cost):
        G = self.G
        G[fr].append([to, cap, cost, len(G[to])])
        G[to].append([fr, 0, -cost, len(G[fr])-1])

    def flow(self, s, t, f):
        N = self.N; G = self.G
        INF = MinCostFlow.INF

        res = 0
        H = [0]*N
        prv_v = [0]*N
        prv_e = [0]*N

        while f:
            dist = [INF]*N
            dist[s] = 0
            que = [(0, s)]

            while que:
                c, v = heappop(que)
                if dist[v] < c:
                    continue
                for i, (w, cap, cost, rev) in enumerate(G[v]):
                    if cap > 0 and dist[w] > dist[v] + cost + H[v] - H[w]:
                        dist[w] = r = dist[v] + cost + H[v] - H[w]
                        prv_v[w] = v
                        prv_e[w] = i
                        heappush(que, (r, w))
            if dist[t] == INF:
                return -1

            for i in range(N):
                H[i] += dist[i]

            d = f; v = t
            while v != s:
                d = min(d, G[prv_v[v]][prv_e[v]][1])
                v = prv_v[v]
            f -= d
            res += d * H[t]
            v = t
            while v != s:
                e = G[prv_v[v]][prv_e[v]]
                e[1] -= d
                G[v][e[3]][1] += d
                v = prv_v[v]
        return res


def Salesman(dist, need_return):
    """
    巡回セールスマン問題、始点0から全ノードを回る最短経路を返す
    :param dist: N^2の隣接行列
    :param need_return: 始点に帰ってくるかどうか
    :return:
    """
    N = len(dist)
    INF = 10**20
    dp = [[INF]*(1<<N) for _ in range(N)]
    dp[0][1] = 0

    for S in range(1<<N):
        for i in range(N):
            if dp[i][S] == INF: continue
            for k in range(1, N):
                if (S>>k) & 1 == 0:
                    dp[k][S + 2**k] = min(dp[i][S] + dist[i][k], dp[k][S + 2**k])

    ans = INF
    for i in range(1, N):
        if need_return:
            ans = min(dp[i][(1<<N)-1] + dist[i][0], ans)
        else:
            ans = min(dp[i][(1 << N) - 1], ans)
    return ans


def main():
    N = NI()
    P = [NLI() for _ in range(N)]
    dist = [[10**20]*N for _ in range(N)]
    for i, p in enumerate(P):
        for j, q in enumerate(P):
            cost = abs(p[0] - q[0]) + abs(p[1] - q[1]) + max(0, q[2] - p[2])
            dist[i][j] = cost

    print(Salesman(dist, True))

if __name__ == "__main__":
    main()