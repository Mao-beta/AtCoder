"""各頂点から1本だけ辺が出るグラフ。閉路・到達数・巨大回数の遷移をまとめて扱う。
0-indexed、next_vertex[v]はvの次の頂点。終端-1は不可（Doublingを使う）。
分解O(N)。jump/distanceを初めて使うときだけO(N log N)の表を作る。
非再帰・標準Pythonのみ。PyPy向け、Codonコンパイル未確認。

使い方（このファイル全体を貼り付けてから実行）
    fg = FunctionalGraph([1, 2, 1, 2])
    fg.cycles, fg.depth  # => ([[1, 2]], [1, 0, 0, 1])
    fg.jump(0, 10**18), fg.distance(3, 1)  # => (2, 2)
    [fg.reachable_count(v) for v in range(4)]  # => [3, 2, 2, 3]
    fg.distance(0, 3)  # => -1
"""

from collections import deque


class FunctionalGraph:
    """FunctionalGraph(next_vertex)。cycle_id/entry/depthは各頂点の閉路ID・入口・距離。
    cycles[id]は辺の向きに並ぶ閉路。配列属性は読み取り専用として扱う。
    入力: next_vertexは長さNの整数列でnext_vertex[v]は0..N-1の唯一の遷移先。終端-1は不可。構築O(N)時間・空間。
    木部分のjump/distanceを初めて必要としたとき、追加でO(N log(N+1))の祖先表を作る。以後の計算量は各メソッドに記載。u/vは0..N-1、kは非負整数の歩数。
    """

    def __init__(self, next_vertex):
        """入力: next_vertexは長さNの整数列でnext_vertex[v]は0..N-1の唯一の遷移先。終端-1は不可。構築O(N)時間・空間。
        木部分のjump/distanceを初めて必要としたとき、追加でO(N log(N+1))の祖先表を作る。以後の計算量は各メソッドに記載。u/vは0..N-1、kは非負整数の歩数。
        """
        self.next = list(next_vertex)
        n = len(self.next)
        indeg = [0] * n
        for v in self.next:
            assert 0 <= v < n
            indeg[v] += 1
        queue = deque(v for v in range(n) if not indeg[v])
        peeled = []
        while queue:
            v = queue.popleft()
            peeled.append(v)
            w = self.next[v]
            indeg[w] -= 1
            if not indeg[w]:
                queue.append(w)
        self.cycles = []
        self.cycle_id = [-1] * n
        self.entry = [-1] * n
        self.depth = [0] * n
        self.position = [-1] * n
        for v in range(n):
            if not indeg[v] or self.cycle_id[v] >= 0:
                continue
            cycle = []
            w = v
            while self.cycle_id[w] < 0:
                self.cycle_id[w] = len(self.cycles)
                self.entry[w] = w
                self.position[w] = len(cycle)
                cycle.append(w)
                w = self.next[w]
            self.cycles.append(cycle)
        for v in reversed(peeled):
            w = self.next[v]
            self.cycle_id[v] = self.cycle_id[w]
            self.entry[v] = self.entry[w]
            self.depth[v] = self.depth[w] + 1
        self._up = None

    def jump(self, v, k):
        """vからk回進んだ頂点。k>=0、巨大整数も可。閉路部分はO(1)、木部分O(log N)。"""
        assert 0 <= v < len(self.next) and k >= 0
        if k >= self.depth[v]:
            cycle = self.cycles[self.cycle_id[v]]
            return cycle[
                (self.position[self.entry[v]] + k - self.depth[v]) % len(cycle)
            ]
        if self._up is None:
            self._up = [self.next]
            for _ in range(1, max(self.depth, default=0).bit_length()):
                row = self._up[-1]
                self._up.append([row[row[i]] for i in range(len(row))])
        bit = 0
        while k:
            if k & 1:
                v = self._up[bit][v]
            k >>= 1
            bit += 1
        return v

    def distance(self, u, v):
        """uからvへ初めて到達するまでの辺数。到達不能は-1、u=vなら0。O(log N)。"""
        assert 0 <= u < len(self.next) and 0 <= v < len(self.next)
        if self.cycle_id[u] != self.cycle_id[v]:
            return -1
        if self.depth[v]:
            d = self.depth[u] - self.depth[v]
            return d if d >= 0 and self.jump(u, d) == v else -1
        cycle = self.cycles[self.cycle_id[u]]
        return self.depth[u] + (self.position[v] - self.position[self.entry[u]]) % len(
            cycle
        )

    def reachable_count(self, v):
        """自分自身を含め、vから到達できる異なる頂点数。O(1)。"""
        assert 0 <= v < len(self.next)
        return self.depth[v] + len(self.cycles[self.cycle_id[v]])
