"""非再帰Dinic。最大流・辺の流量・最小カット。一般グラフO(V²E)。

抽出元: _Graph_Algorithm.py。提出時はこのファイルをコピーする（ローカルimport不要）。
PyPy向け。Codonでのコンパイルは未確認。

使い方（このファイルを解答の先頭に貼り付けてから実行）
    g = mf_graph(3)
    e0 = g.add_edge(0, 1, 3)
    e1 = g.add_edge(1, 2, 2)
    g.flow(0, 2), g.get_edge(e0).Flow  # => (2, 2)
    g.min_cut(0)  # => [True, True, False]
"""

from typing import Optional, List, cast


class mf_graph:
    """n頂点の有向グラフ（0-indexed）に非負整数容量を追加して最大流を求める。
    add_edge→flow(s,t)→get_edge/min_cutの順に使う。逆辺は自動生成する。
    flowは残余グラフを変更し、再呼び出しは追加で流せた量を返す。一般O(V²E)。
    入力: n_は非負整数の頂点数V。構築O(V)時間・空間。各メソッドの頂点は0..V-1、Eはadd_edgeで追加した辺数。容量・流量は非負整数。
    """

    class edge:
        """get_edge(i)/edges(False)の辺情報。From,To,Cap,Flowを参照する。"""

        def __init__(self, from_, to_, cap_, flow_):
            self.From = from_
            self.To = to_
            self.Cap = cap_
            self.Flow = flow_

    class _Edge:
        def __init__(self, dst: int, cap: int) -> None:
            self.dst = dst
            self.cap = cap
            self.rev: Optional[mf_graph._Edge] = None

    def __init__(self, n_) -> None:
        """入力: n_は非負整数の頂点数V。構築O(V)時間・空間。各メソッドの頂点は0..V-1、Eはadd_edgeで追加した辺数。容量・流量は非負整数。
        """
        n = n_
        self._n = n
        self._g: List[List[mf_graph._Edge]] = [[] for _ in range(n)]
        self._edges: List[mf_graph._Edge] = []

    def add_edge(self, From_, To_, Cap_) -> int:
        """src→dstに容量cap>=0の辺を追加し、入力順の辺IDを返す。多重辺可。O(1)。
        From_/To_は始点/終点の頂点番号、Cap_は容量。配列への追加は償却O(1)。
        """
        src, dst, cap = From_, To_, Cap_
        assert 0 <= src < self._n
        assert 0 <= dst < self._n
        assert 0 <= cap
        m = len(self._edges)
        e = mf_graph._Edge(dst, cap)
        re = mf_graph._Edge(src, 0)
        e.rev = re
        re.rev = e
        self._g[src].append(e)
        self._g[dst].append(re)
        self._edges.append(e)
        return m

    def get_edge(self, i: int) -> edge:
        """辺ID iのedge(From,To,Cap,Flow)を返す。capは元容量、flowは現在の流量。O(1)。"""
        assert 0 <= i < len(self._edges)
        e = self._edges[i]
        re = cast(mf_graph._Edge, e.rev)
        return mf_graph.edge(re.dst, e.dst, e.cap + re.cap, re.cap)

    def edges(self, isdict=True):
        """追加順の辺情報。既定はdictのlist、Falseならedgeのlist。O(E)。
        dictキーは'from','to','cap','flow'。get_edge(i)は常にedgeオブジェクト。
        isdictはboolで、Trueなら辞書、Falseならedgeオブジェクトのlistを返す。
        """
        edges = [self.get_edge(i) for i in range(len(self._edges))]
        if isdict:
            return [
                {"from": e.From, "to": e.To, "cap": e.Cap, "flow": e.Flow}
                for e in edges
            ]
        return edges

    def change_edge(self, i: int, new_cap: int, new_flow: int) -> None:
        """辺iを容量new_cap、流量new_flowに設定する。0<=new_flow<=new_cap。
        流量保存則は検査しないため、呼び出し側で実行可能な流れを維持する。O(1)。
        """
        assert 0 <= i < len(self._edges)
        assert 0 <= new_flow <= new_cap
        e = self._edges[i]
        e.cap = new_cap - new_flow
        assert e.rev is not None
        e.rev.cap = new_flow

    def flow(self, s: int, t: int, flow_limit: int = (1 << 63) - 1) -> int:
        """sからtへ追加で流せた流量を返す。s!=t、flow_limit>=0（省略時は2**63-1）。
        残余グラフを変更する。過去の流量を含む合計が必要なら戻り値を累積する。
        s/tは始点/終点。flow_limitは今回追加で流す量の上限。一般グラフで最悪O(V²E)時間、追加空間O(V)。
        """
        assert 0 <= s < self._n
        assert 0 <= t < self._n
        assert s != t
        assert flow_limit >= 0

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
            edge_stack: List[mf_graph._Edge] = []
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
                    re = cast(mf_graph._Edge, e.rev)
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
        """現在の残余グラフでsから到達可能かを示す長さnのboolリスト。O(V+E)。
        制限で打ち切らず最大流を流し切った後に呼ぶと、True側が最小カットのs側。
        """
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
