"""競プロ用スニペット。単体で貼り付け可能。2026-10-17版。

使い方（このファイルを解答の先頭に貼り付けてから実行）

頂点番号は0-indexed。edgesは(u,v)で重みなしの無向木。
    tree = LCATree(4, [(0, 1), (0, 2), (2, 3)])  # root=0
    tree.lca(1, 3), tree.distance(1, 3), tree.kth_ancestor(3, 2)  # => (0, 3, 0)
    tree.jump(1, 3, 2), tree.get_path(1, 3), tree.subtree_size(2)  # => (2, [1, 0, 2, 3], 2)
"""

class LCATree:
    """二分累乗法で LCA を求める木。頂点番号は0-indexed。

    LCATree(n, edges, root=0)。edges は (u,v) の無向辺、頂点 0..n-1。
    入力は連結な木であること。閉路・未連結は ValueError。
    lca(u,v): 最小共通祖先 O(log N)。
    kth_ancestor(v,k): k 個上の祖先（なければ -1） O(log N)。
    distance(u,v): 辺の本数 O(log N)。
    jump(u,v,k): u→v のパスの k 番目の頂点（0-indexed、範囲外 -1）。
    is_ancestor(u,v): u が v の祖先（自身を含む）か。O(1)。
    subtree_size(v): v を根とする部分木の頂点数。O(1)。
    get_path(u,v): パス上の頂点のリスト。O(パス長 + log N)。
    構築 O(N log N)、メモリ O(N log N)。再帰なし。
    入力: nは正整数の頂点数N、edges=[(u,v),...]は無向木の各辺を1本ずつ格納した列。0<=u,v,root<n。構築O(N log(N+1))時間・空間。
    以後の頂点引数・返す頂点番号も0-indexed、kは非負整数の辺数。根の親・存在しない祖先は-1。
    """

    @staticmethod
    def make_adjlist_nond(n, edges):
        """0-indexed の無向隣接リストを構築する。
        nは頂点数、edgesは0-indexedの無向辺tupleの列。時間・出力空間O(n+len(edges))。
        """
        g = [[] for _ in range(n)]
        for edge in edges:
            u, v = edge[0], edge[1]
            if not (0 <= u < n and 0 <= v < n) or u == v:
                raise ValueError("辺の頂点番号が不正です")
            g[u].append(v)
            g[v].append(u)
        return g

    def __init__(self, n, edges, root=0):
        """入力: nは正整数の頂点数N、edges=[(u,v),...]は無向木の各辺を1本ずつ格納した列。0<=u,v,root<n。構築O(N log(N+1))時間・空間。
        以後の頂点引数・返す頂点番号も0-indexed、kは非負整数の辺数。
        """
        if n < 1 or not 0 <= root < n:
            raise ValueError("n>=1、0<=root<n が必要です")
        self.n = n
        self.root = root
        self.max_double = max(1, n.bit_length())
        self.adj = self.make_adjlist_nond(n, edges)
        self.parent = [[-1] * n for _ in range(self.max_double)]
        self.depth = [-1] * n
        self.tin = [-1] * n
        self.tout = [-1] * n

        self.depth[root] = 0
        timer = 0
        stack = [(root, False)]
        par = self.parent[0]
        while stack:
            v, exiting = stack.pop()
            if exiting:
                self.tout[v] = timer
                continue
            self.tin[v] = timer
            timer += 1
            stack.append((v, True))
            for u in reversed(self.adj[v]):
                if u == par[v]:
                    continue
                if self.depth[u] != -1:
                    raise ValueError("入力グラフに閉路があります")
                par[u] = v
                self.depth[u] = self.depth[v] + 1
                stack.append((u, False))

        if timer != n:
            raise ValueError("入力グラフは連結ではありません")

        for j in range(1, self.max_double):
            prev, curr = self.parent[j - 1], self.parent[j]
            for v in range(n):
                p = prev[v]
                curr[v] = prev[p] if p != -1 else -1

    def kth_ancestor(self, v, k):
        """v の k 世代上の祖先。存在しなければ -1。O(log N)。"""
        assert 0 <= v < self.n and k >= 0
        if k > self.depth[v]:
            return -1
        bit = 0
        while k:
            if k & 1:
                v = self.parent[bit][v]
            k >>= 1
            bit += 1
        return v

    def lca(self, u, v):
        """u, v の LCA。O(log N)。"""
        assert 0 <= u < self.n and 0 <= v < self.n
        if self.depth[u] < self.depth[v]:
            u, v = v, u
        u = self.kth_ancestor(u, self.depth[u] - self.depth[v])
        if u == v:
            return u
        for i in range(self.max_double - 1, -1, -1):
            if self.parent[i][u] != self.parent[i][v]:
                u = self.parent[i][u]
                v = self.parent[i][v]
        return self.parent[0][u]


    def distance(self, u, v):
        """u と v の間の辺数。O(log N)。"""
        p = self.lca(u, v)
        return self.depth[u] + self.depth[v] - 2 * self.depth[p]

    def is_ancestor(self, u, v):
        """u が v の祖先か（自身も含む）。O(1)。"""
        assert 0 <= u < self.n and 0 <= v < self.n
        return self.tin[u] <= self.tin[v] < self.tout[u]

    def subtree_size(self, v):
        """v を根とした部分木のサイズ。O(1)。"""
        assert 0 <= v < self.n
        return self.tout[v] - self.tin[v]

    def jump(self, u, v, k):
        """u から v に向かうパスで k 辺進んだ位置。範囲外なら -1。
        時間O(log(N+1))、追加空間O(1)。
        """
        assert 0 <= u < self.n and 0 <= v < self.n and k >= 0
        p = self.lca(u, v)
        a = self.depth[u] - self.depth[p]
        b = self.depth[v] - self.depth[p]
        if k > a + b:
            return -1
        return self.kth_ancestor(u, k) if k <= a else self.kth_ancestor(v, a + b - k)

    def get_path(self, u, v):
        """u→v のパス上の頂点を順に返す。
        返す経路長Lに対しO(L+log(N+1))時間・O(L)空間。
        """
        p = self.lca(u, v)
        left, right = [], []
        par = self.parent[0]
        while u != p:
            left.append(u)
            u = par[u]
        left.append(p)
        while v != p:
            right.append(v)
            v = par[v]
        return left + right[::-1]

    def __len__(self):
        return self.n

