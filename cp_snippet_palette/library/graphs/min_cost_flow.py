"""最小費用流。非負の辺費用を要求。flow/slopeで残余グラフを変更する。

抽出元: _Graph_Algorithm.py。提出時はこのファイルをコピーする（ローカルimport不要）。
PyPy向け。Codonでのコンパイルは未確認。

使い方（このファイルを解答の先頭に貼り付けてから実行）
    g = mcf_graph(3)
    _ = g.add_edge(0, 1, 3, 2)
    _ = g.add_edge(1, 2, 3, 4)
    sent, cost = g.flow(0, 2, 2)
    sent, cost  # sent == 必要流量 を確認する
    # => (2, 12)
    h = mcf_graph(2)  # slopeを試すときは別オブジェクト
    _ = h.add_edge(0, 1, 3, 5)
    h.slope(0, 1)  # => [(0, 0), (3, 15)]
"""

import heapq
from typing import Optional, List, Tuple, cast


class mcf_graph:
    """n頂点の有向グラフに非負整数容量・非負整数費用の辺を追加する。
    add_edgeを全て済ませてからflowまたはslopeを一度だけ呼ぶ。逆辺は自動生成。
    頂点は0-indexed。負費用・計算後の辺追加・再計算は非対応。
    入力: Nは非負整数の頂点数V。構築O(V)時間・空間。各頂点番号は0..V-1、Eは追加辺数。容量・費用・流量は非負整数。
    """

    class _Edge:
        def __init__(self, dst: int, cap: int, cost: int) -> None:
            self.dst = dst
            self.cap = cap
            self.cost = cost
            self.rev: Optional[mcf_graph._Edge] = None

    def __init__(self, N) -> None:
        """入力: Nは非負整数の頂点数V。構築O(V)時間・空間。各頂点番号は0..V-1、Eは追加辺数。容量・費用・流量は非負整数。
        """
        n = N
        self._n = n
        self._g: List[List[mcf_graph._Edge]] = [[] for _ in range(n)]
        self._edges: List[mcf_graph._Edge] = []
        self._used = False

    def add_edge(self, From, To, cap, cost):
        """src→dstへ容量cap、単位流量当たり費用costの辺を追加する。戻り値はNone。辺IDは追加順の0始まり。
        cap>=0,cost>=0。負費用やflow/slope後の追加はValueError。O(1)。
        From/Toは始点/終点の頂点番号。配列への追加は償却O(1)。
        """
        src, dst = From, To
        if self._used:
            raise ValueError("cannot add edges after flow")
        if cost < 0:
            raise ValueError("nonnegative original costs required")
        assert 0 <= src < self._n
        assert 0 <= dst < self._n
        assert 0 <= cap
        e = mcf_graph._Edge(dst, cap, cost)
        re = mcf_graph._Edge(src, 0, -cost)
        e.rev = re
        re.rev = e
        self._g[src].append(e)
        self._g[dst].append(re)
        self._edges.append(e)

    def get_edge(self, i: int) -> dict:
        """辺ID iのdict（キー'from','to','cap','flow','cost'）を返す。capは元容量。O(1)。"""
        assert 0 <= i < len(self._edges)
        e = self._edges[i]
        re = cast(mcf_graph._Edge, e.rev)
        return {
            "from": re.dst,
            "to": e.dst,
            "cap": e.cap + re.cap,
            "flow": re.cap,
            "cost": e.cost,
        }

    def edges(self) -> List[dict]:
        """追加順のdictのlist。逆辺を含めない。O(E)。"""
        return [self.get_edge(i) for i in range(len(self._edges))]

    def flow(self, s: int, t: int, flow_limit: int = (1 << 63) - 1) -> Tuple[int, int]:
        """sからtへ最大flow_limitまで流し、(実際の流量,最小総費用)を返す。
        省略時の上限は2**63-1。指定量を送れない場合も部分的な結果を返すので流量を確認する。
        残余グラフを変更。flow/slopeを合わせて1オブジェクト1回のみ。
        s/tは異なる始点/終点、flow_limitは非負整数の流量上限。Fを実際の流量とすると、最短路反復は高々F回でO((F+1)*(V+E)*log(V+E+2))時間が上界。
        空間O(V+E+F)以内（slopeの出力を含む）。
        """
        return self.slope(s, t, flow_limit)[-1]

    def slope(
        self, s: int, t: int, flow_limit: int = (1 << 63) - 1
    ) -> List[Tuple[int, int]]:
        """流量と最小総費用の折れ線の端点[(0,0),...,(最大流量,費用)]を返す。
        同じ傾きの区間はまとめる。s!=t、flow_limit>=0。残余グラフを変更する。
        flow/slopeを合わせて1回のみ。反復ごとに最短路探索と増加を行う。
        s/tは異なる始点/終点、flow_limitは非負整数の流量上限。Fを実際の流量とすると、最短路反復は高々F回でO((F+1)*(V+E)*log(V+E+2))時間が上界。
        空間O(V+E+F)以内（slopeの出力を含む）。
        """
        if self._used:
            raise ValueError("flow/slope may be called once per graph")
        if flow_limit is not None and flow_limit < 0:
            raise ValueError("negative flow limit")
        self._used = True
        assert 0 <= s < self._n
        assert 0 <= t < self._n
        assert s != t
        assert flow_limit >= 0

        dual = [0] * self._n
        prev: List[Optional[Tuple[int, mcf_graph._Edge]]] = [None] * self._n

        def refine_dual() -> bool:
            pq = [(0, s)]
            visited = [False] * self._n
            dist: List[Optional[int]] = [None] * self._n
            dist[s] = 0
            while pq:
                dist_v, v = heapq.heappop(pq)
                if visited[v]:
                    continue
                visited[v] = True
                if v == t:
                    break
                dual_v = dual[v]
                for e in self._g[v]:
                    w = e.dst
                    if visited[w] or e.cap == 0:
                        continue
                    reduced_cost = e.cost - dual[w] + dual_v
                    new_dist = dist_v + reduced_cost
                    dist_w = dist[w]
                    if dist_w is None or new_dist < dist_w:
                        dist[w] = new_dist
                        prev[w] = v, e
                        heapq.heappush(pq, (new_dist, w))
            else:
                return False
            dist_t = dist[t]
            for v in range(self._n):
                if visited[v]:
                    dual[v] -= cast(int, dist_t) - cast(int, dist[v])
            return True

        flow = 0
        cost = 0
        prev_cost_per_flow: Optional[int] = None
        result = [(flow, cost)]
        while flow < flow_limit:
            if not refine_dual():
                break
            f = flow_limit - flow
            v = t
            while prev[v] is not None:
                u, e = cast(Tuple[int, mcf_graph._Edge], prev[v])
                f = min(f, e.cap)
                v = u
            v = t
            while prev[v] is not None:
                u, e = cast(Tuple[int, mcf_graph._Edge], prev[v])
                e.cap -= f
                assert e.rev is not None
                e.rev.cap += f
                v = u
            c = -dual[s]
            flow += f
            cost += f * c
            if c == prev_cost_per_flow:
                result.pop()
            result.append((flow, cost))
            prev_cost_per_flow = c
        return result
