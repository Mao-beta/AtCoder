"""強連結成分分解。O(V+E)、非再帰。成分番号はトポロジカル順。
抽出元: _SCC.py。提出時はこのファイルをコピーする（ローカルimport不要）。
PyPy向け。Codonでのコンパイルは未確認。
"""


class SCCGraph:
    """
    強連結成分分解 (SCC: Strongly Connected Components) を行うクラス。

    Kosaraju 法を非再帰 DFS で実装する。
    頂点番号は 0-indexed を前提とする。

    Parameters
    ----------
    n : int
        頂点数。

    Attributes
    ----------
    n : int
        頂点数。
    g : list[list[int]]
        元の有向グラフの隣接リスト。
    rg : list[list[int]]
        逆向きグラフの隣接リスト。

    Notes
    -----
    - 計算量は O(V + E)。
    - DFS は再帰を使用しないため、再帰上限を気にする必要がない。
    - SCC のラベルは縮約 DAG のトポロジカル順に付与される。
      異なる SCC 間に u -> v が存在するなら、

          ids[u] < ids[v]

      となる。
    - add_edge() 後に SCC 情報を要求すると、自動的に再計算される。
    """

    __slots__ = (
        "n",
        "g",
        "rg",
        "_built",
        "_ids",
        "_group_count",
    )

    def __init__(self, n: int = 0):
        """
        SCC ライブラリを初期化する。

        Parameters
        ----------
        n : int
            頂点数。
            頂点番号は 0, 1, ..., n-1。
        """
        assert n >= 0
        self.n = n
        self.g: list[list[int]] = [[] for _ in range(n)]
        self.rg: list[list[int]] = [[] for _ in range(n)]

        self._built = False
        self._ids: list[int] = []
        self._group_count = 0

    def add_edge(self, u: int, v: int) -> None:
        """
        有向辺 u -> v を追加する。

        Parameters
        ----------
        u : int
            始点。
        v : int
            終点。

        Notes
        -----
        ACLと同じく頂点番号が範囲内であることを要求する。
        入力が 1-indexed の場合は呼び出し側で 1 を引く。
        """
        assert 0 <= u < self.n and 0 <= v < self.n
        self.g[u].append(v)
        self.rg[v].append(u)
        self._built = False

    def _build(self) -> None:
        """
        Kosaraju 法で SCC 分解を実行する。

        1回目:
            元グラフで DFS を行い、正しい帰りがけ順を求める。

        2回目:
            帰りがけ順の逆順に逆グラフを DFS し、
            各頂点に SCC ラベルを付与する。

        Notes
        -----
        1回目 DFS では、

            stack = [(vertex, next_edge_index)]

        のようなタプルを大量に生成せず、

            stack : 現在の DFS パス
            edge_index[v] : v から次に調べる辺

        と分離して管理する。

        したがって DFS 中のスタック要素は int のみ。
        """
        n = self.n
        g = self.g
        rg = self.rg

        # ---------------------------------------------------------
        # 1回目の DFS
        #
        # 元グラフ上で正しい帰りがけ順を求める。
        #
        # edge_index[v] は
        # 「v の隣接リストのどこまで探索したか」を表す。
        #
        # これにより (v, i) のタプルを大量に生成する必要がない。
        # ---------------------------------------------------------

        seen = [False] * n
        edge_index = [0] * n
        order: list[int] = []

        for start in range(n):
            if seen[start]:
                continue

            seen[start] = True
            stack = [start]

            while stack:
                v = stack[-1]
                i = edge_index[v]

                if i < len(g[v]):
                    to = g[v][i]
                    edge_index[v] = i + 1

                    if not seen[to]:
                        seen[to] = True
                        stack.append(to)

                else:
                    # v から出る辺をすべて探索し終えた。
                    # 再帰 DFS でいう「帰りがけ」。
                    stack.pop()
                    order.append(v)

        # ---------------------------------------------------------
        # 2回目の DFS
        #
        # 逆グラフを、帰りがけ順の逆順に探索する。
        # ---------------------------------------------------------

        ids = [-1] * n
        group_count = 0

        for start in reversed(order):
            if ids[start] != -1:
                continue

            ids[start] = group_count
            stack = [start]

            while stack:
                v = stack.pop()

                for to in rg[v]:
                    if ids[to] == -1:
                        ids[to] = group_count
                        stack.append(to)

            group_count += 1

        self._ids = ids
        self._group_count = group_count
        self._built = True

    def scc_ids(self) -> list[int]:
        """
        各頂点が属する SCC のラベルを返す。

        Returns
        -------
        list[int]
            ids[v] が頂点 v の SCC ラベル。

        Notes
        -----
        ラベルは 0, 1, ..., group_count - 1。

        SCC ラベルは縮約 DAG のトポロジカル順なので、
        異なる SCC 間の辺 u -> v に対して

            ids[u] < ids[v]

        が成り立つ。
        """
        if not self._built:
            self._build()

        return self._ids

    def group_count(self) -> int:
        """
        強連結成分の個数を返す。

        Returns
        -------
        int
            SCC の総数。
        """
        if not self._built:
            self._build()

        return self._group_count

    def scc(self) -> list[list[int]]:
        """
        各 SCC に含まれる頂点を返す。

        Returns
        -------
        list[list[int]]
            SCC ごとの頂点リスト。

            groups[c] は SCC ラベル c に属する頂点を持つ。

            SCC 自体も縮約 DAG のトポロジカル順に並ぶ。
        """
        ids = self.scc_ids()
        k = self._group_count

        groups = [[] for _ in range(k)]

        for v in range(self.n):
            groups[ids[v]].append(v)

        return groups

    def dag(self) -> list[list[int]]:
        """
        SCC を縮約した DAG を返す。

        Returns
        -------
        list[list[int]]
            SCC を頂点とした縮約グラフ。

            dag[c] は SCC c から直接遷移できる
            SCC ラベルのリスト。

        Notes
        -----
        - 同一 SCC 内の辺は削除される。
        - SCC 間の多重辺は1本にまとめられる。
        - SCC ラベル自体がトポロジカル順なので、

              c -> d

          なら必ず

              c < d

          となる。
        """
        ids = self.scc_ids()
        k = self._group_count

        dag_set = [set() for _ in range(k)]

        for v in range(self.n):
            cv = ids[v]

            for to in self.g[v]:
                ct = ids[to]

                if cv != ct:
                    dag_set[cv].add(ct)

        return [list(to) for to in dag_set]


SCC = SCCGraph  # 旧名


class TwoSAT:
    """(x_i==f) OR (x_j==g)の連言。satisfiable()後にanswer()。O(n+節数)。"""

    def __init__(self, n=0):
        assert n >= 0
        self.n = n
        self.graph = SCCGraph(2 * n)
        self._answer = [False] * n

    def add_clause(self, i, f, j, g):
        if not (0 <= i < self.n and 0 <= j < self.n):
            raise IndexError("invalid variable")
        a, b = 2 * i + int(bool(f)), 2 * j + int(bool(g))
        self.graph.add_edge(a ^ 1, b)
        self.graph.add_edge(b ^ 1, a)

    def satisfiable(self):
        """充足可能ならTrueを返し、answer()を更新する。"""
        ids = self.graph.scc_ids()
        if any(ids[2 * i] == ids[2 * i + 1] for i in range(self.n)):
            return False
        self._answer = [ids[2 * i] < ids[2 * i + 1] for i in range(self.n)]
        return True

    def answer(self):
        """直前のsatisfiable()がTrueのときの解。辺追加後は再判定が必要。"""
        return self._answer[:]

    def solve(self):
        """旧API: 解を返す。充足不能ならNone。"""
        return self.answer() if self.satisfiable() else None
