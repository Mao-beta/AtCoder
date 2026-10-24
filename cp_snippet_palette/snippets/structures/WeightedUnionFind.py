"""競プロ用スニペット。単体で貼り付け可能。2026-10-17版。

使い方（このファイルを解答の先頭に貼り付けてから実行）
    uf = WeightedUnionFind(3)
    uf.merge(0, 1, 5)  # p[1]-p[0]=5
    # => 0
    uf.merge(1, 2, -2)  # p[2]-p[1]=-2
    # => 0
    uf.diff(0, 2), uf.is_consistent(0, 2, 3), uf.is_consistent(0, 2, 4)  # => (3, True, False)
    uf.merge(0, 2, 3)  # 既存制約と一致。矛盾ならValueError
    # => 0
"""

class WeightedUnionFind:
    """ポテンシャル差を管理する Union-Find（加法群、0-indexed）。

    merge(a,b,w): potential[b]-potential[a]=wを課し、代表元を返す。
    diff(a,b): 同じ成分のpotential[b]-potential[a]。
    potential(a): 所属する根を0としたaのポテンシャル。

    mergeは新規統合・既存制約との一致のどちらも代表元の整数を返す。
    既存の条件と矛盾すればValueError。事前確認には is_consistent を使う。
    diff は未連結なら ValueError（無意味な差を返さない）。
    各種の木操作は償却 O(α(N))。
    入力: Nは非負整数の頂点数。構築O(N)時間・空間。a/bは0..N-1の頂点番号、wはpotential[b]-potential[a]の数値。
    α(N)は逆Ackermann関数。
    """

    def __init__(self, N):
        """入力: Nは非負整数の頂点数。構築O(N)時間・空間。a/bは0..N-1の頂点番号、wはpotential[b]-potential[a]の数値。
        α(N)は逆Ackermann関数。
        """
        n = N
        assert n >= 0
        self.n = n
        self.par = [-1] * n
        self.weight = [0] * n  # 親→自分の差。leader 後は根→自分の差
        self._group_count = n

    def leader(self, a):
        """a の代表元を返す。経路圧縮時に重みも更新（非再帰）。
        償却O(α(N))時間、経路圧縮用の追加空間O(log(N+1))以内。
        """
        assert 0 <= a < self.n
        p, w = self.par, self.weight
        path = []
        v = a
        while p[v] >= 0:
            path.append(v)
            v = p[v]
        root = v
        acc = 0
        for v in reversed(path):
            acc += w[v]
            w[v] = acc
            p[v] = root
        return root


    def same(self, a, b):
        """頂点a,bが同じ連結成分ならTrue。償却O(α(n))。
        """
        return self.leader(a) == self.leader(b)


    def potential(self, a):
        """所属する根のpotentialを0としたaのpotentialを返す。
        償却O(α(N))時間、経路圧縮用の追加空間O(log(N+1))以内。
        """
        self.leader(a)
        return self.weight[a]

    def diff(self, a, b):
        """potential[b]-potential[a]。未連結なら ValueError。
        償却O(α(N))時間、経路圧縮用の追加空間O(log(N+1))以内。
        """
        rx = self.leader(a)
        ry = self.leader(b)
        if rx != ry:
            raise ValueError("a と b は未連結です")
        return self.weight[b] - self.weight[a]

    def is_consistent(self, a, b, w):
        """potential[b]-potential[a]=w が既存の条件と矛盾しないか。
        償却O(α(N))時間、経路圧縮用の追加空間O(log(N+1))以内。
        """
        rx, ry = self.leader(a), self.leader(b)
        return rx != ry or self.weight[b] - self.weight[a] == w

    def merge(self, a, b, w):
        """potential[b]-potential[a]=w を設定し、統合後の代表元を返す。
        既に同じ成分でも代表元を返す。矛盾はValueError。
        償却O(α(N))時間、経路圧縮用の追加空間O(log(N+1))以内。
        """
        x, y = a, b
        rx, ry = self.leader(x), self.leader(y)
        delta = w + self.weight[x] - self.weight[y]
        if rx == ry:
            if delta != 0:
                raise ValueError("既存の重み制約と矛盾します")
            return rx
        p = self.par
        if p[rx] > p[ry]:
            rx, ry = ry, rx
            delta = -delta
        p[rx] += p[ry]
        p[ry] = rx
        self.weight[ry] = delta
        self._group_count -= 1
        return rx


    def size(self, a):
        """aと同じ連結成分の頂点数。償却O(α(n))。
        """
        return -self.par[self.leader(a)]

    def members(self, a):
        """aと同じ成分の全頂点をlistで返す。O(n α(n))。
        """
        root = self.leader(a)
        return [i for i in range(self.n) if self.leader(i) == root]

    def roots(self):
        """各成分の代表元のlist。O(n)。
        """
        return [i for i, v in enumerate(self.par) if v < 0]

    def group_count(self):
        """現在の連結成分数を返す。O(1)。
        """
        return self._group_count

    def all_group_members(self):
        """{代表元:その成分の頂点list}を返す。O(n α(n))。
        """
        res = {}
        for i in range(self.n):
            res.setdefault(self.leader(i), []).append(i)
        return res

    def groups(self):
        """全成分の頂点listのlist。代表元順、成分内は頂点順。O(N α(N))。
        """
        groups = self.all_group_members()
        return [groups[root] for root in self.roots()]

    def weights(self):
        """すべての頂点について、所属根からのポテンシャルを返す。O(Nα(N))。"""
        for i in range(self.n):
            self.leader(i)
        return self.weight[:]

    def __len__(self):
        return self.n

    def __repr__(self):
        return f"WeightedUnionFind({self.groups()!r})"

