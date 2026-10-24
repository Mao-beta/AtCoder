"""非再帰HLDと非可換セグ木。0-indexed、半開区間。構築O(n)、経路集約O(log²n)。

抽出元: LibraryChecker/vertex_set_path_composite.py。提出時はこのファイルをコピーする（ローカルimport不要）。
PyPy向け。Codonでのコンパイルは未確認。

使い方（このファイルを解答の先頭に貼り付けてから実行）
    hld = HLD(3, [[1, 2], [0], [0]])
    seg = BiSegTree(hld.reorder_by_pos_from_node_values(['a', 'b', 'c']), lambda a, b: a + b, '')
    path_prod(hld, seg, 1, 2)  # => 'bac'
    hld.lca(1, 2), hld.distance(1, 2)  # => (0, 2)
    hld.kth_ancestor(1, 1), hld.jump(1, 2, 2)  # => (0, 2)
    seg.set(hld.pos[0], 'X')
    path_prod(hld, seg, 1, 2)  # => 'bXc'
    arr = hld.reorder_by_pos_from_edge_values([(0, 1), (0, 2)], [4, 7])
    arr[hld.pos[0]] = 0
    edges = BiSegTree(arr, lambda a, b: a + b, 0)
    path_prod(hld, edges, 1, 2, edge=True)  # => 11
"""

from typing import List, Tuple, Callable


class BiSegTree:
    """順方向・逆方向の集約を保持する非可換セグメント木。
    Vは初期配列。OP(a,b)はaの後にbを処理する結合的演算。
    Eは左右の単位元。演算で引数を書き換えないこと。構築O(n)、更新・集約O(log n)。
    入力: Vは集約値の列。n=len(V)。OPは結合的な二引数関数、Eはその単位元。構築O(n)時間・空間（OPをO(1)とする）。
    p/iは0-indexed、区間は0<=l<=r<=n。
    """

    def __init__(self, V, OP: Callable, E):
        """入力: Vは集約値の列。n=len(V)。OPは結合的な二引数関数、Eはその単位元。構築O(n)時間・空間（OPをO(1)とする）。
        p/iは0-indexed、区間は0<=l<=r<=n。
        """
        arr = list(V)
        n = len(arr)
        op, e = OP, E
        self.n = n
        self.op = op
        self.e = e
        size = 1
        while size < n:
            size <<= 1
        self.size = size
        # data_lr[k]: fold of the segment in LR order
        # data_rl[k]: fold of the segment in RL order
        self.data_lr = [e] * (2 * size)
        self.data_rl = [e] * (2 * size)
        for i, x in enumerate(arr):
            self.data_lr[size + i] = x
            self.data_rl[size + i] = x
        for i in range(size - 1, 0, -1):
            L, R = 2 * i, 2 * i + 1
            self.data_lr[i] = op(self.data_lr[L], self.data_lr[R])
            self.data_rl[i] = op(self.data_rl[R], self.data_rl[L])

    def set(self, p: int, x):
        """0-indexedの位置pをxに置換する。戻り値なし、O(log n)。
        """
        assert 0 <= p < self.n
        i = p + self.size
        self.data_lr[i] = x
        self.data_rl[i] = x
        i >>= 1
        while i:
            L, R = 2 * i, 2 * i + 1
            self.data_lr[i] = self.op(self.data_lr[L], self.data_lr[R])
            self.data_rl[i] = self.op(self.data_rl[R], self.data_rl[L])
            i >>= 1

    def get(self, p: int):
        """位置pの値を返す。O(1)。0<=p<n。
        """
        assert 0 <= p < self.n
        return self.data_lr[self.size + p]

    def prod(self, l: int, r: int):
        """[l,r)を左から右へopで集約する。空区間はe。O(log n)。
        """
        assert 0 <= l <= r <= self.n
        op, e, size = self.op, self.e, self.size
        l += size
        r += size
        left, right = e, e
        while l < r:
            if l & 1:
                left = op(left, self.data_lr[l])
                l += 1
            if r & 1:
                r -= 1
                right = op(self.data_lr[r], right)
            l >>= 1
            r >>= 1
        return op(left, right)

    def prod_reverse(self, l: int, r: int):
        """[l,r)を右から左へopで集約する。空区間はe。O(log n)。
        """
        assert 0 <= l <= r <= self.n
        op, e, size = self.op, self.e, self.size
        l += size
        r += size
        left, right = e, e
        while l < r:
            if l & 1:
                # RL: new left-part becomes node.rl followed by current
                left = op(self.data_rl[l], left)
                l += 1
            if r & 1:
                r -= 1
                # RL: right-part grows to the right in RL sense
                right = op(right, self.data_rl[r])
            l >>= 1
            r >>= 1
        return op(right, left)


class HLD:
    """n頂点の無向木adjをrootで根付き木にしてHeavy-Light分解する。非再帰O(n)。
    adj[v]は隣接頂点番号のlist。pos[v]は配列上の位置、inv[i]は元頂点。
    parent[root]=-1、depthは辺数、sizeは部分木頂点数。連結・閉路なしが前提。
    値はreorder_by_pos_from_node_valuesで並べ替えてからBiSegTreeへ渡す。
    入力: nは頂点数、adjは長さnの隣接頂点listのlist。0<=root<n、連結無向木の各辺を両方向に格納する。構築O(n)時間・空間。
    メソッドのu/vは元の頂点番号、kは非負整数の辺数。
    """

    def __init__(self, n: int, adj: List[List[int]], root: int = 0):
        """入力: nは頂点数、adjは長さnの隣接頂点listのlist。0<=root<n、連結無向木の各辺を両方向に格納する。構築O(n)時間・空間。
        メソッドのu/vは元の頂点番号、kは非負整数の辺数。
        """
        self.n = n
        self.adj = adj
        self.root = root
        self.parent = [-1] * n
        self.depth = [0] * n
        self.size = [0] * n
        self.heavy = [-1] * n
        self.head = [0] * n
        self.pos = [0] * n
        self.inv = [0] * n
        self.tin = [0] * n
        self.tout = [0] * n
        self._build()

    def _build(self):
        if self.n == 0:
            return
        # 1) sizes & heavy (iterative DFS)
        st = [(self.root, -1, 0)]
        while st:
            u, p, state = st.pop()
            if state == 0:
                self.parent[u] = p
                self.size[u] = 1
                st.append((u, p, 1))
                for v in self.adj[u]:
                    if v == p:
                        continue
                    self.depth[v] = self.depth[u] + 1
                    st.append((v, u, 0))
            else:
                max_sz, hv = 0, -1
                for v in self.adj[u]:
                    if v == p:
                        continue
                    self.size[u] += self.size[v]
                    if self.size[v] > max_sz:
                        max_sz, hv = self.size[v], v
                self.heavy[u] = hv

        # 2) assign head & pos (heavy-first order)
        cur = 0
        stack = [self.root]
        while stack:
            h = stack.pop()
            u = h
            while u != -1:
                self.head[u] = h
                self.pos[u] = cur
                self.inv[cur] = u
                self.tin[u] = cur
                cur += 1
                # push light children to process later
                for v in self.adj[u]:
                    if v == self.parent[u] or v == self.heavy[u]:
                        continue
                    stack.append(v)
                u = self.heavy[u]
        # 3) tout as half-open
        for u in range(self.n):
            self.tout[u] = self.tin[u] + self.size[u]

    # Utilities
    def lca(self, u: int, v: int) -> int:
        """頂点u,vの最小共通祖先の頂点番号。O(log n)。
        """
        while self.head[u] != self.head[v]:
            if self.depth[self.head[u]] > self.depth[self.head[v]]:
                u = self.parent[self.head[u]]
            else:
                v = self.parent[self.head[v]]
        return u if self.depth[u] < self.depth[v] else v

    def distance(self, u: int, v: int) -> int:
        """頂点u,v間の辺の本数。重み付き距離ではない。O(log n)。
        """
        w = self.lca(u, v)
        return self.depth[u] + self.depth[v] - 2 * self.depth[w]

    def subtree_range(self, u: int) -> Tuple[int, int]:
        """uの部分木に対応するpos上の半開区間(l,r)。u自身を含む。O(1)。
        """
        return (self.tin[u], self.tout[u])

    def kth_ancestor(self, v, k):
        """vからk辺上の祖先。k=0ならv、根を越える場合は-1。O(log n)。"""
        if k < 0:
            raise ValueError("negative distance")
        if k > self.depth[v]:
            return -1
        while k > self.depth[v] - self.depth[self.head[v]]:
            k -= self.depth[v] - self.depth[self.head[v]] + 1
            v = self.parent[self.head[v]]
        return self.inv[self.pos[v] - k]

    def jump(self, u, v, k):
        """uからvへの経路でuからk辺先の頂点。範囲外は-1。O(log n)。"""
        if k < 0:
            return -1
        w = self.lca(u, v)
        up, down = self.depth[u] - self.depth[w], self.depth[v] - self.depth[w]
        if k > up + down:
            return -1
        return self.kth_ancestor(u, k) if k <= up else self.kth_ancestor(v, up + down - k)

    # Helpers for mapping values
    def reorder_by_pos_from_node_values(self, node_vals: List):
        """長さnの頂点値node_valsをpos順に並べた新しいlistを返す。O(n)。
        """
        return [node_vals[self.inv[i]] for i in range(self.n)]

    def reorder_by_pos_from_edge_values(
        self, edges: List[Tuple[int, int]], edge_vals: List
    ):
        """edges=[(u,v),...]と同じ順のedge_valsから、子のposに辺値を置いたlistを返す。
        根の位置はNoneなので、BiSegTree構築前にarr[pos[root]]=eとする。
        全ての木の辺を一度ずつ渡す。経路集約はedge=Trueを指定する。
        時間・出力空間O(n)。edge_valsは各辺に対応する任意の集約値の列。
        """
        arr = [None] * self.n
        for (a, b), w in zip(edges, edge_vals):
            if self.parent[a] == b:
                arr[self.pos[a]] = w
            elif self.parent[b] == a:
                arr[self.pos[b]] = w
            else:
                raise ValueError(
                    "Edge does not match parent-child relation for the chosen root."
                )
        # root has no incoming edge; set identity later when building BiSegTree
        return arr


def path_prod(hld: HLD, seg: BiSegTree, u: int, v: int, *, edge: bool = False):
    """hldのpos順で構築したsegを使い、uからvへ進む順で値を集約する。O(log² n)。
    edge=Falseは両端の頂点値を含む。edge=Trueは子位置に格納した辺値を集約し、
    u==vならe。頂点vの値の更新はseg.set(hld.pos[v],value)。
    hld/segはそれぞれ構築済みHLD/BiSegTree、u/vは0..n-1の頂点、n=hld.n。edgeは辺値を集約するかのbool。opをO(1)として追加空間O(1)。
    """
    op, e = seg.op, seg.e
    up = e  # accumulator for u-side (u -> LCA), correct order via RL folds
    down = e  # accumulator for LCA -> v, correct order via LR folds (prepended)

    while hld.head[u] != hld.head[v]:
        if hld.depth[hld.head[u]] >= hld.depth[hld.head[v]]:
            hu = hld.head[u]
            up = op(up, seg.prod_reverse(hld.pos[hu], hld.pos[u] + 1))
            u = hld.parent[hu]
        else:
            hv = hld.head[v]
            # prepend so that upper segments come before lower ones
            down = op(seg.prod(hld.pos[hv], hld.pos[v] + 1), down)
            v = hld.parent[hv]

    # same head
    if hld.depth[u] >= hld.depth[v]:
        l = hld.pos[v] + (1 if edge else 0)
        up = op(up, seg.prod_reverse(l, hld.pos[u] + 1))
    else:
        l = hld.pos[u] + (1 if edge else 0)
        down = op(seg.prod(l, hld.pos[v] + 1), down)

    return op(up, down)
