"""競プロ用スニペット。単体で貼り付け可能。2026-10-17版。"""

class WeightedUnionFind:
    """ポテンシャル差を管理する Union-Find（加法群、0-indexed）。

    unite(x, y, w): potential[y] - potential[x] = w を課す。
    diff(x, y): 同じ集合に属する場合の potential[y] - potential[x]。
    get_weight(x): 所属する根を 0 とした x のポテンシャル。

    unite は新しく統合したら True、既に同一で条件が一致すれば False、
    既存の条件と矛盾すれば ValueError。事前確認には is_consistent を使う。
    diff は未連結なら ValueError（無意味な差を返さない）。
    各種の木操作は償却 O(α(N))。
    """

    def __init__(self, n):
        assert n >= 0
        self.n = n
        self.par = [-1] * n
        self.weight = [0] * n  # 親→自分の差。find 後は根→自分の差
        self._group_count = n

    def find(self, x):
        """x の代表元を返す。経路圧縮時に重みも更新（非再帰）。"""
        p, w = self.par, self.weight
        path = []
        v = x
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

    leader = find

    def is_same(self, x, y):
        return self.find(x) == self.find(y)

    same = is_same

    def get_weight(self, x):
        self.find(x)
        return self.weight[x]

    def diff(self, x, y):
        """potential[y]-potential[x]。未連結なら ValueError。"""
        rx = self.find(x)
        ry = self.find(y)
        if rx != ry:
            raise ValueError("x と y は未連結です")
        return self.weight[y] - self.weight[x]

    def is_consistent(self, x, y, w):
        """potential[y]-potential[x]=w が既存の条件と矛盾しないか。"""
        rx, ry = self.find(x), self.find(y)
        return rx != ry or self.weight[y] - self.weight[x] == w

    def unite(self, x, y, w=0):
        """potential[y]-potential[x]=w を設定。矛盾は ValueError。"""
        rx, ry = self.find(x), self.find(y)
        delta = w + self.weight[x] - self.weight[y]
        if rx == ry:
            if delta != 0:
                raise ValueError("既存の重み制約と矛盾します")
            return False
        p = self.par
        if p[rx] > p[ry]:
            rx, ry = ry, rx
            delta = -delta
        p[rx] += p[ry]
        p[ry] = rx
        self.weight[ry] = delta
        self._group_count -= 1
        return True

    merge = unite      # 重み付き版の merge は unite と同じ真偽値を返す
    potential = get_weight

    def size(self, x):
        return -self.par[self.find(x)]

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, v in enumerate(self.par) if v < 0]

    def group_count(self):
        return self._group_count

    def all_group_members(self):
        res = {}
        for i in range(self.n):
            res.setdefault(self.find(i), []).append(i)
        return res

    def groups(self):
        return list(self.all_group_members().values())

    def weights(self):
        """すべての頂点について、所属根からのポテンシャルを返す。O(Nα(N))。"""
        for i in range(self.n):
            self.find(i)
        return self.weight[:]

    def __len__(self):
        return self.n

    def __repr__(self):
        return f"WeightedUnionFind({self.groups()!r})"

