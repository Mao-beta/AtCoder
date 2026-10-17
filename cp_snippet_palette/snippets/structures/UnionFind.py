"""競プロ用スニペット。単体で貼り付け可能。2026-10-17版。"""


class DSU:
    """素集合データ構造（Union by size + 経路圧縮）。頂点は 0..n-1。

    find / leader: 代表元、unite: 異なる集合を統合したら True。
    merge: 統合後の代表元（ACL 流）、is_same / same: 同じ集合か。
    find / unite / size: 償却 O(α(N))。
    groups / all_group_members: O(N α(N))、members(x): O(N α(N))。
    """

    def __init__(self, n=0):
        assert n >= 0
        self.n = n
        self.par = [-1] * n  # 根では -サイズ、他では親の番号
        self._group_count = n

    def find(self, x):
        """x の代表元を返す。非再帰。"""
        assert 0 <= x < self.n
        p = self.par
        root = x
        while p[root] >= 0:
            root = p[root]
        while x != root:
            nxt = p[x]
            p[x] = root
            x = nxt
        return root

    leader = find

    def is_same(self, x, y):
        return self.find(x) == self.find(y)

    same = is_same

    def merge(self, x, y):
        """集合を統合して代表元を返す。既に同じ集合なら変更しない。"""
        x, y = self.find(x), self.find(y)
        if x == y:
            return x
        p = self.par
        if p[x] > p[y]:
            x, y = y, x
        p[x] += p[y]
        p[y] = x
        self._group_count -= 1
        return x

    def unite(self, x, y):
        """異なる集合を統合したら True、既に同じなら False。"""
        x, y = self.find(x), self.find(y)
        if x == y:
            return False
        p = self.par
        if p[x] > p[y]:
            x, y = y, x
        p[x] += p[y]
        p[y] = x
        self._group_count -= 1
        return True

    def size(self, x):
        return -self.par[self.find(x)]

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, v in enumerate(self.par) if v < 0]

    def group_count(self):
        """連結成分数。O(1)。"""
        return self._group_count

    def all_group_members(self):
        """{代表元: 頂点リスト} を一度の走査で作る。O(N α(N))。"""
        res = {}
        for i in range(self.n):
            res.setdefault(self.find(i), []).append(i)
        return res

    def groups(self):
        """全連結成分の頂点リストを返す（ACL 形式）。"""
        return list(self.all_group_members().values())

    def __len__(self):
        return self.n

    def __repr__(self):
        return f"UnionFind({self.groups()!r})"


UnionFind = DSU  # 旧名。mergeは成否ではなく代表元を返す。
