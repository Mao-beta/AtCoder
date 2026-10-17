"""競プロ用スニペット。単体で貼り付け可能。2026-10-17版。"""


class SegTree:
    """一般のセグメント木。0-indexed / 半開区間 [l,r)。

    SegTree(op, e, v)。v は初期配列、または要素が e の長さ N（整数）。
    OP は結合的二項演算、E は左右の単位元。可換性は不要。
    set / prod / max_right / min_left: O(log N)、get / all_prod: O(1)。
    境界探索の判定関数 f は f(E)=True で、拡張に対して True→False に単調。
    """

    def __init__(self, op, e, v):
        """ACL Python版と同じ SegTree(op, e, v)。vは長さまたは初期配列。"""
        V, OP, E = v, op, e
        if isinstance(V, int):
            assert V >= 0
            n = V
            V = [E] * n
        else:
            n = len(V)
        self.n = n
        self.op = OP
        self.e = E
        self.log = (n - 1).bit_length() if n else 0
        self.size = 1 << self.log
        d = [E] * (2 * self.size)
        d[self.size : self.size + n] = V
        for k in range(self.size - 1, 0, -1):
            d[k] = OP(d[k << 1], d[k << 1 | 1])
        self.d = d

    def update(self, k):
        """内部ノード k を子から再計算する。O(1)。通常の要素変更は set。"""
        self.d[k] = self.op(self.d[k << 1], self.d[k << 1 | 1])

    def set(self, p, x):
        """V[p] = x。O(log N)。"""
        assert 0 <= p < self.n
        p += self.size
        d, op = self.d, self.op
        d[p] = x
        while p > 1:
            p >>= 1
            d[p] = op(d[p << 1], d[p << 1 | 1])

    def get(self, p):
        """V[p] を返す。O(1)。"""
        assert 0 <= p < self.n
        return self.d[p + self.size]

    def prod(self, l, r):
        """[l,r) の OP 集約値。空区間は E。O(log N)。"""
        assert 0 <= l <= r <= self.n
        l += self.size
        r += self.size
        sm_l = sm_r = self.e
        d, op = self.d, self.op
        while l < r:
            if l & 1:
                sm_l = op(sm_l, d[l])
                l += 1
            if r & 1:
                r -= 1
                sm_r = op(d[r], sm_r)
            l >>= 1
            r >>= 1
        return op(sm_l, sm_r)

    def all_prod(self):
        """配列全体の集約値。O(1)。"""
        return self.d[1]

    def max_right(self, l, f):
        """f(prod(l,r)) が True である最大 r（0<=l<=r<=N）。O(log N)。

        f(E)=True、r を右に伸ばすと True→False で戻らないこと。
        全域で True なら N を返す。
        """
        assert 0 <= l <= self.n
        assert f(self.e)
        if l == self.n:
            return self.n
        l += self.size
        sm, d, op = self.e, self.d, self.op
        while True:
            while (l & 1) == 0:
                l >>= 1
            nxt = op(sm, d[l])
            if not f(nxt):
                while l < self.size:
                    l <<= 1
                    nxt = op(sm, d[l])
                    if f(nxt):
                        sm = nxt
                        l += 1
                return l - self.size
            sm = nxt
            l += 1
            if (l & -l) == l:
                break
        return self.n

    def min_left(self, r, f):
        """f(prod(l,r)) が True である最小 l（0<=l<=r<=N）。O(log N)。

        f(E)=True、l を左に伸ばすと True→False で戻らないこと。
        全域で True なら 0 を返す。
        """
        assert 0 <= r <= self.n
        assert f(self.e)
        if r == 0:
            return 0
        r += self.size
        sm, d, op = self.e, self.d, self.op
        while True:
            r -= 1
            while r > 1 and (r & 1):
                r >>= 1
            nxt = op(d[r], sm)
            if not f(nxt):
                while r < self.size:
                    r = r << 1 | 1
                    nxt = op(d[r], sm)
                    if f(nxt):
                        sm = nxt
                        r -= 1
                return r + 1 - self.size
            sm = nxt
            if (r & -r) == r:
                break
        return 0

    def to_list(self):
        """全要素をリストで取得する。O(N)。"""
        return self.d[self.size : self.size + self.n]

    def __len__(self):
        return self.n

    def __getitem__(self, p):
        return self.get(p)

    def __str__(self):
        return str(self.to_list())


class segtree(SegTree):
    """旧引数順の互換用。新規コードは SegTree(op, e, v) を使う。"""

    def __init__(self, V, OP, E):
        super().__init__(OP, E, V)
