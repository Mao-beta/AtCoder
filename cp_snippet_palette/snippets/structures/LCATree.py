"""競プロ用スニペット。単体で貼り付け可能。2026-10-17版。"""

class LCATree:
    """二分累乗法で LCA を求める木（元コード互換の 1-indexed）。

    LCATree(n, edges, root=1)。edges は (u,v) の非向辺、頂点 1..n。
    入力は連結な木であること。閉路・未連結は ValueError。
    get_LCA / lca(u,v): 最小共通祖先 O(log N)。
    kth_ancestor(v,k): k 個上の祖先（なければ -1） O(log N)。
    distance(u,v): 辺の本数 O(log N)。
    jump(u,v,k): u→v のパスの k 番目の頂点（0-indexed、範囲外 -1）。
    is_ancestor(u,v): u が v の祖先（自身を含む）か。O(1)。
    subtree_size(v): v を根とする部分木の頂点数。O(1)。
    get_path(u,v): パス上の頂点のリスト。O(パス長 + log N)。
    構築 O(N log N)、メモリ O(N log N)。再帰なし。
    """

    @staticmethod
    def make_adjlist_nond(n, edges):
        """1-indexed の無向隣接リストを構築する。"""
        g = [[] for _ in range(n + 1)]
        for edge in edges:
            u, v = edge[0], edge[1]
            if not (1 <= u <= n and 1 <= v <= n) or u == v:
                raise ValueError("辺の頂点番号が不正です")
            g[u].append(v)
            g[v].append(u)
        return g

    def __init__(self, n, edges, root=1):
        if n < 1 or not 1 <= root <= n:
            raise ValueError("n>=1、1<=root<=n が必要です")
        self.n = n
        self.root = root
        self.max_double = max(1, n.bit_length())
        self.adj = self.make_adjlist_nond(n, edges)
        self.parent = [[-1] * (n + 1) for _ in range(self.max_double)]
        self.depth = [-1] * (n + 1)
        self.tin = [-1] * (n + 1)
        self.tout = [-1] * (n + 1)

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
            for v in range(1, n + 1):
                p = prev[v]
                curr[v] = prev[p] if p != -1 else -1

    def kth_ancestor(self, v, k):
        """v の k 世代上の祖先。存在しなければ -1。O(log N)。"""
        assert 1 <= v <= self.n and k >= 0
        if k > self.depth[v]:
            return -1
        bit = 0
        while k:
            if k & 1:
                v = self.parent[bit][v]
            k >>= 1
            bit += 1
        return v

    def get_LCA(self, x, y):
        """x, y の LCA。O(log N)。"""
        assert 1 <= x <= self.n and 1 <= y <= self.n
        if self.depth[x] < self.depth[y]:
            x, y = y, x
        x = self.kth_ancestor(x, self.depth[x] - self.depth[y])
        if x == y:
            return x
        for i in range(self.max_double - 1, -1, -1):
            if self.parent[i][x] != self.parent[i][y]:
                x = self.parent[i][x]
                y = self.parent[i][y]
        return self.parent[0][x]

    lca = get_LCA

    def distance(self, x, y):
        """x と y の間の辺数。O(log N)。"""
        p = self.get_LCA(x, y)
        return self.depth[x] + self.depth[y] - 2 * self.depth[p]

    def is_ancestor(self, u, v):
        """u が v の祖先か（自身も含む）。O(1)。"""
        assert 1 <= u <= self.n and 1 <= v <= self.n
        return self.tin[u] <= self.tin[v] < self.tout[u]

    def subtree_size(self, v):
        """v を根とした部分木のサイズ。O(1)。"""
        assert 1 <= v <= self.n
        return self.tout[v] - self.tin[v]

    def jump(self, u, v, k):
        """u から v に向かうパスで k 辺進んだ位置。範囲外なら -1。"""
        assert 1 <= u <= self.n and 1 <= v <= self.n and k >= 0
        p = self.get_LCA(u, v)
        a = self.depth[u] - self.depth[p]
        b = self.depth[v] - self.depth[p]
        if k > a + b:
            return -1
        return self.kth_ancestor(u, k) if k <= a else self.kth_ancestor(v, a + b - k)

    def get_path(self, u, v):
        """u→v のパス上の頂点を順に返す。"""
        p = self.get_LCA(u, v)
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

