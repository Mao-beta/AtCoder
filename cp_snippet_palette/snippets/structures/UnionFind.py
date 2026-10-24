"""Union-Find。APIはshakayami/ACL-for-pythonのdsuに準拠。

使い方（このファイルを解答の先頭に貼り付けてから実行）
    uf = dsu(4)
    root = uf.merge(0, 1)  # 代表元を返す。統合の成否をboolで判定しない
    uf.same(0, 1), uf.same(0, 2), uf.size(0)  # => (True, False, 2)
    if not uf.same(1, 2):
        uf.merge(1, 2)
    uf.groups(), uf.group_count()  # => ([[0, 1, 2], [3]], 2)
"""


class dsu:
    """dsu(N)。頂点0..N-1の集合を統合する。merge(a,b)は統合後の代表元。
    leader/same/size/mergeは償却O(α(N))。groupsは代表元順、各集合は頂点番号順。
    group_count/members/roots/all_group_membersは独自拡張。
    入力: Nは非負整数の頂点数。構築O(N)時間・空間。a/b/xは0..N-1の頂点番号。α(N)は逆Ackermann関数。
    """

    def __init__(self, N):
        """入力: Nは非負整数の頂点数。構築O(N)時間・空間。a/b/xは0..N-1の頂点番号。α(N)は逆Ackermann関数。
        """
        n = N
        assert n >= 0
        self.n = n
        self.parent_or_size = [-1] * n  # 根では -サイズ、他では親の番号
        self._group_count = n

    def leader(self, a):
        """頂点aの代表元。経路圧縮、非再帰、償却O(α(N))。"""
        x = a
        assert 0 <= x < self.n
        p = self.parent_or_size
        root = x
        while p[root] >= 0:
            root = p[root]
        while x != root:
            nxt = p[x]
            p[x] = root
            x = nxt
        return root

    def same(self, a, b):
        """a,bが同じ集合ならTrue。償却O(α(N))。"""
        return self.leader(a) == self.leader(b)

    def merge(self, a, b):
        """集合を統合して代表元を返す。既に同じ集合なら変更しない。
        償却O(α(N))時間、経路探索の追加空間O(1)。
        """
        x, y = self.leader(a), self.leader(b)
        if x == y:
            return x
        p = self.parent_or_size
        if p[x] > p[y]:
            x, y = y, x
        p[x] += p[y]
        p[y] = x
        self._group_count -= 1
        return x

    def size(self, a):
        """aが属する集合の頂点数を返す。償却O(α(n))。"""
        return -self.parent_or_size[self.leader(a)]

    def members(self, x):
        """xと同じ集合の全頂点を昇順listで返す。全頂点を走査するためO(n α(n))。"""
        root = self.leader(x)
        return [i for i in range(self.n) if self.leader(i) == root]

    def roots(self):
        """現在の各集合の代表元をlistで返す。O(n)。"""
        return [i for i, v in enumerate(self.parent_or_size) if v < 0]

    def group_count(self):
        """連結成分数。O(1)。"""
        return self._group_count

    def all_group_members(self):
        """{代表元: 頂点リスト} を一度の走査で作る。O(N α(N))。"""
        res = {}
        for i in range(self.n):
            res.setdefault(self.leader(i), []).append(i)
        return res

    def groups(self):
        """全連結成分の頂点リストを返す（ACL 形式）。
        時間O(N α(N))、返すlistの空間O(N)。
        """
        members = self.all_group_members()
        return [members[root] for root in sorted(members)]

    def __len__(self):
        return self.n

    def __repr__(self):
        return f"dsu({self.groups()!r})"
