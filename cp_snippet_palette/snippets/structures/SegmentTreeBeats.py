"""競プロ用スニペット。単体で貼り付け可能。2026-10-17版。

使い方（このファイルを解答の先頭に貼り付けてから実行）
    seg = SegmentTreeBeats([1, 5, 3, 7])
    seg.chmin(0, 4, 4)  # chmin: [1,4,3,4]
    seg.chmax(0, 2, 2)  # chmax: [2,4,3,4]
    seg.add(1, 3, 10)   # [2,14,13,4]
    seg.prod(0, 4)  # (最小,最大,和)
    # => (2, 14, 33)
    seg.assign(2, 4, 0)
    seg.to_list()  # => [2, 14, 0, 0]
"""

from math import inf


class SegmentTreeBeats:
    """Segment Tree Beats。0-indexed / 半開区間 [l,r)。

    SegmentTreeBeats(V)へ初期数値列を渡す。長さNの全0なら[0]*N。
    chmin(l,r,x): A[i] = min(A[i], x)（range chmin）。
    chmax(l,r,x): A[i] = max(A[i], x)（range chmax）。
    add(l,r,x): A[i] += x。
    assign(l,r,x): A[i] = x（range assign）。
    min(l,r)/max(l,r)/sum(l,r): 区間最小値/最大値/和。
    prod(l,r): (min, max, sum) のタプル。
    get(i) / set(i,x) / all_min/max/sum / to_list を追加。

    空区間の min/max/sum はそれぞれ inf/-inf/0。
    典型的な chmin/chmax 更新は償却計算量で評価する（毎回の最悪 O(log N)
    ではない）。区間加算・代入・クエリは O(log N)。構築 O(N)。
    入力: Vは初期数値列、N=len(V)。構築O(N)時間・空間。
    p/iは0-indexed、区間引数l/rは0<=l<=r<=N、xは上限/下限/加算量/代入値。
    """

    def __init__(self, V):
        """入力: Vは初期数値列、N=len(V)。構築O(N)時間・空間。
        p/iは0-indexed、区間引数l/rは0<=l<=r<=N、xは上限/下限/加算量/代入値。
        """
        a = list(V)
        n = len(a)
        self.n = n
        self.n0 = 1 << ((n - 1).bit_length() if n else 0)
        m = 2 * self.n0 - 1  # 0-indexed 完全二分木
        self.inf = inf
        self.max_v = [-inf] * m
        self.smax_v = [-inf] * m
        self.max_c = [0] * m
        self.min_v = [inf] * m
        self.smin_v = [inf] * m
        self.min_c = [0] * m
        self.len = [0] * m  # 実在要素数（ダミー葉を数えない）
        self._sum = [0] * m
        self.ladd = [0] * m
        self.lval = [None] * m  # None は代入なし（実値の ±inf と区別する）
        base = self.n0 - 1
        for i in range(n):
            k = base + i
            v = a[i]
            self.max_v[k] = self.min_v[k] = self._sum[k] = v
            self.max_c[k] = self.min_c[k] = self.len[k] = 1
        for k in range(base - 1, -1, -1):
            self.len[k] = self.len[2 * k + 1] + self.len[2 * k + 2]
            self._update(k)

    def _update(self, k):
        """内部ノード k を両子から集約。O(1)。"""
        lc, rc = 2 * k + 1, 2 * k + 2
        self._sum[k] = self._sum[lc] + self._sum[rc]
        max_v, smax_v, max_c = self.max_v, self.smax_v, self.max_c
        if max_v[lc] < max_v[rc]:
            max_v[k] = max_v[rc]
            max_c[k] = max_c[rc]
            smax_v[k] = max(max_v[lc], smax_v[rc])
        elif max_v[lc] > max_v[rc]:
            max_v[k] = max_v[lc]
            max_c[k] = max_c[lc]
            smax_v[k] = max(smax_v[lc], max_v[rc])
        else:
            max_v[k] = max_v[lc]
            max_c[k] = max_c[lc] + max_c[rc]
            smax_v[k] = max(smax_v[lc], smax_v[rc])
        min_v, smin_v, min_c = self.min_v, self.smin_v, self.min_c
        if min_v[lc] < min_v[rc]:
            min_v[k] = min_v[lc]
            min_c[k] = min_c[lc]
            smin_v[k] = min(smin_v[lc], min_v[rc])
        elif min_v[lc] > min_v[rc]:
            min_v[k] = min_v[rc]
            min_c[k] = min_c[rc]
            smin_v[k] = min(min_v[lc], smin_v[rc])
        else:
            min_v[k] = min_v[lc]
            min_c[k] = min_c[lc] + min_c[rc]
            smin_v[k] = min(smin_v[lc], smin_v[rc])

    def _update_node_max(self, k, x):
        """ノード全体の最大値のみを x に下げる（必要条件確認済み）。
        kは内部ノード番号、xは新しい極値。内部処理で時間・空間O(1)。
        """
        if self.max_c[k] == 0 or self.max_v[k] <= x:
            return
        old = self.max_v[k]
        self._sum[k] += (x - old) * self.max_c[k]
        if old == self.min_v[k]:
            self.min_v[k] = x
        elif old == self.smin_v[k]:
            self.smin_v[k] = x
        self.max_v[k] = x
        if self.lval[k] is not None:
            self.lval[k] = min(self.lval[k], x)

    def _update_node_min(self, k, x):
        """ノード全体の最小値のみを x に上げる（必要条件確認済み）。
        kは内部ノード番号、xは新しい極値。内部処理で時間・空間O(1)。
        """
        if self.min_c[k] == 0 or x <= self.min_v[k]:
            return
        old = self.min_v[k]
        self._sum[k] += (x - old) * self.min_c[k]
        if old == self.max_v[k]:
            self.max_v[k] = x
        elif old == self.smax_v[k]:
            self.smax_v[k] = x
        self.min_v[k] = x
        if self.lval[k] is not None:
            self.lval[k] = max(self.lval[k], x)

    def _addall(self, k, x):
        """ノード全体へ加算（内部用）。O(1)。
        kは内部の木のノード番号（配列の要素添字ではない）。利用側の区間更新にはadd_val/update_valを使う。
        """
        if self.len[k] == 0:
            return
        self.max_v[k] += x
        self.min_v[k] += x
        if self.smax_v[k] != -inf:
            self.smax_v[k] += x
        if self.smin_v[k] != inf:
            self.smin_v[k] += x
        self._sum[k] += self.len[k] * x
        if self.lval[k] is not None:
            self.lval[k] += x
        else:
            self.ladd[k] += x

    def _updateall(self, k, x):
        """ノード全体を x に代入（内部用）。O(1)。
        kは内部の木のノード番号（配列の要素添字ではない）。利用側の区間更新にはadd_val/update_valを使う。
        """
        if self.len[k] == 0:
            return
        self.max_v[k] = self.min_v[k] = x
        self.smax_v[k] = -inf
        self.smin_v[k] = inf
        self.max_c[k] = self.min_c[k] = self.len[k]
        self._sum[k] = x * self.len[k]
        self.lval[k] = x
        self.ladd[k] = 0

    def _push(self, k):
        """未伝播の代入・加算・chmin/chmax 制約を子へ渡す。O(1)。
        kは内部の木のノード番号（配列の要素添字ではない）。利用側の区間更新にはadd_val/update_valを使う。
        """
        if k >= self.n0 - 1:
            return
        lc, rc = 2 * k + 1, 2 * k + 2
        if self.lval[k] is not None:
            self._updateall(lc, self.lval[k])
            self._updateall(rc, self.lval[k])
            self.lval[k] = None
            return
        if self.ladd[k]:
            self._addall(lc, self.ladd[k])
            self._addall(rc, self.ladd[k])
            self.ladd[k] = 0
        for c in (lc, rc):
            if self.max_v[c] > self.max_v[k]:
                self._update_node_max(c, self.max_v[k])
            if self.min_v[c] < self.min_v[k]:
                self._update_node_min(c, self.min_v[k])

    def _update_min(self, x, a, b, k, l, r):
        if b <= l or r <= a or self.max_v[k] <= x:
            return
        if a <= l and r <= b and self.smax_v[k] < x:
            self._update_node_max(k, x)
            return
        self._push(k)
        mid = (l + r) >> 1
        self._update_min(x, a, b, 2 * k + 1, l, mid)
        self._update_min(x, a, b, 2 * k + 2, mid, r)
        self._update(k)

    def _update_max(self, x, a, b, k, l, r):
        if b <= l or r <= a or x <= self.min_v[k]:
            return
        # chmax では「2番目に小さい値」を比較する（元コードの smax_v は誤り）。
        if a <= l and r <= b and x < self.smin_v[k]:
            self._update_node_min(k, x)
            return
        self._push(k)
        mid = (l + r) >> 1
        self._update_max(x, a, b, 2 * k + 1, l, mid)
        self._update_max(x, a, b, 2 * k + 2, mid, r)
        self._update(k)

    def _add_val(self, x, a, b, k, l, r):
        if b <= l or r <= a:
            return
        if a <= l and r <= b:
            self._addall(k, x)
            return
        self._push(k)
        mid = (l + r) >> 1
        self._add_val(x, a, b, 2 * k + 1, l, mid)
        self._add_val(x, a, b, 2 * k + 2, mid, r)
        self._update(k)

    def _update_val(self, x, a, b, k, l, r):
        if b <= l or r <= a:
            return
        if a <= l and r <= b:
            self._updateall(k, x)
            return
        self._push(k)
        mid = (l + r) >> 1
        self._update_val(x, a, b, 2 * k + 1, l, mid)
        self._update_val(x, a, b, 2 * k + 2, mid, r)
        self._update(k)

    def chmin(self, l, r, x):
        """[l,r) の各要素を min(A[i],x) に更新（chmin）。償却計算量。
        1回の最悪時間O(N)、作業スタックO(log(N+1))以内。高速性は操作列に対する償却解析によるもので、毎回O(log N)ではない。
        """
        assert 0 <= l <= r <= self.n
        if l != r:
            self._update_min(x, l, r, 0, 0, self.n0)


    def chmax(self, l, r, x):
        """[l,r) の各要素を max(A[i],x) に更新（chmax）。償却計算量。
        1回の最悪時間O(N)、作業スタックO(log(N+1))以内。高速性は操作列に対する償却解析によるもので、毎回O(log N)ではない。
        """
        assert 0 <= l <= r <= self.n
        if l != r:
            self._update_max(x, l, r, 0, 0, self.n0)


    def add(self, l, r, x):
        """[l,r) の各要素に x を足す。O(log N)。"""
        assert 0 <= l <= r <= self.n
        if l != r:
            self._add_val(x, l, r, 0, 0, self.n0)


    def assign(self, l, r, x):
        """[l,r) の各要素を x にする。O(log N)。"""
        assert 0 <= l <= r <= self.n
        if l != r:
            self._update_val(x, l, r, 0, 0, self.n0)


    def _query_max(self, a, b, k, l, r):
        if b <= l or r <= a:
            return -inf
        if a <= l and r <= b:
            return self.max_v[k]
        self._push(k)
        mid = (l + r) >> 1
        return max(self._query_max(a, b, 2 * k + 1, l, mid),
                   self._query_max(a, b, 2 * k + 2, mid, r))

    def _query_min(self, a, b, k, l, r):
        if b <= l or r <= a:
            return inf
        if a <= l and r <= b:
            return self.min_v[k]
        self._push(k)
        mid = (l + r) >> 1
        return min(self._query_min(a, b, 2 * k + 1, l, mid),
                   self._query_min(a, b, 2 * k + 2, mid, r))

    def _query_sum(self, a, b, k, l, r):
        if b <= l or r <= a:
            return 0
        if a <= l and r <= b:
            return self._sum[k]
        self._push(k)
        mid = (l + r) >> 1
        return self._query_sum(a, b, 2 * k + 1, l, mid) + self._query_sum(a, b, 2 * k + 2, mid, r)

    def _query_stats(self, a, b, k, l, r):
        if b <= l or r <= a:
            return inf, -inf, 0
        if a <= l and r <= b:
            return self.min_v[k], self.max_v[k], self._sum[k]
        self._push(k)
        mid = (l + r) >> 1
        x = self._query_stats(a, b, 2 * k + 1, l, mid)
        y = self._query_stats(a, b, 2 * k + 2, mid, r)
        return min(x[0], y[0]), max(x[1], y[1]), x[2] + y[2]

    def max(self, l, r):
        """[l,r) の最大値。空区間は -inf。O(log N)。"""
        assert 0 <= l <= r <= self.n
        return -inf if l == r else self._query_max(l, r, 0, 0, self.n0)

    def min(self, l, r):
        """[l,r) の最小値。空区間は inf。O(log N)。"""
        assert 0 <= l <= r <= self.n
        return inf if l == r else self._query_min(l, r, 0, 0, self.n0)

    def sum(self, l, r):
        """[l,r) の和。空区間は 0。O(log N)。"""
        assert 0 <= l <= r <= self.n
        return 0 if l == r else self._query_sum(l, r, 0, 0, self.n0)

    def prod(self, l, r):
        """[l,r) の (最小値, 最大値, 和) を一度の探索で返す。O(log N)。"""
        assert 0 <= l <= r <= self.n
        return (inf, -inf, 0) if l == r else self._query_stats(l, r, 0, 0, self.n0)

    def all_max(self):
        """全要素の最大値。空なら-inf。O(1)。
        """
        return self.max_v[0]

    def all_min(self):
        """全要素の最小値。空ならinf。O(1)。
        """
        return self.min_v[0]

    def all_sum(self):
        """全要素の和。空なら0。O(1)。
        """
        return self._sum[0]

    def get(self, p):
        """A[p] を取得する。O(log N)。"""
        assert 0 <= p < self.n
        k, l, r = 0, 0, self.n0
        while r - l > 1:
            self._push(k)
            mid = (l + r) >> 1
            if p < mid:
                k = 2 * k + 1
                r = mid
            else:
                k = 2 * k + 2
                l = mid
        return self._sum[k]

    def set(self, p, x):
        """A[p]=x。O(log N)。"""
        assert 0 <= p < self.n
        self.assign(p, p + 1, x)

    def to_list(self):
        """実要素の配列を返す。保留操作を全展開し、O(N)。"""
        for k in range(self.n0 - 1):
            self._push(k)
        base = self.n0 - 1
        return self._sum[base:base + self.n]

    def __len__(self):
        return self.n

    def __getitem__(self, i):
        return self.get(i)

    def __str__(self):
        return str(self.to_list())

