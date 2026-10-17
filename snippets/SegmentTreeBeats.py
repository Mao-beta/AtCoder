"""競プロ用スニペット。単体で貼り付け可能。2026-10-17版。"""

from math import inf


class SegmentTreeBeats:
    """Segment Tree Beats。0-indexed / 半開区間 [l,r)。

    SegmentTreeBeats(n, a=None) または SegmentTreeBeats(初期配列)。
    update_min(l,r,x): A[i] = min(A[i], x)（range chmin）。
    update_max(l,r,x): A[i] = max(A[i], x)（range chmax）。
    add_val(l,r,x): A[i] += x。
    update_val(l,r,x): A[i] = x（range assign）。
    query_min/max/sum(l,r): 区間最小値/最大値/和。
    query(l,r): (min, max, sum) のタプル。
    get(i) / set(i,x) / all_min/max/sum / to_list を追加。

    空区間の min/max/sum はそれぞれ inf/-inf/0。
    典型的な chmin/chmax 更新は償却計算量で評価する（毎回の最悪 O(log N)
    ではない）。区間加算・代入・クエリは O(log N)。構築 O(N)。
    """

    def __init__(self, n, a=None):
        if not isinstance(n, int):
            if a is not None:
                raise ValueError("配列を第一引数にする場合、第二引数は省略してください")
            a = list(n)
            n = len(a)
        if n < 0:
            raise ValueError("n は非負の整数としてください")
        if a is None:
            a = [0] * n
        elif len(a) != n:
            raise ValueError("a の長さは n と一致させてください")
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
        self.sum = [0] * m
        self.ladd = [0] * m
        self.lval = [None] * m  # None は代入なし（実値の ±inf と区別する）
        base = self.n0 - 1
        for i in range(n):
            k = base + i
            v = a[i]
            self.max_v[k] = self.min_v[k] = self.sum[k] = v
            self.max_c[k] = self.min_c[k] = self.len[k] = 1
        for k in range(base - 1, -1, -1):
            self.len[k] = self.len[2 * k + 1] + self.len[2 * k + 2]
            self.update(k)

    def update(self, k):
        """内部ノード k を両子から集約。O(1)。"""
        lc, rc = 2 * k + 1, 2 * k + 2
        self.sum[k] = self.sum[lc] + self.sum[rc]
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

    def update_node_max(self, k, x):
        """ノード全体の最大値のみを x に下げる（必要条件確認済み）。"""
        if self.max_c[k] == 0 or self.max_v[k] <= x:
            return
        old = self.max_v[k]
        self.sum[k] += (x - old) * self.max_c[k]
        if old == self.min_v[k]:
            self.min_v[k] = x
        elif old == self.smin_v[k]:
            self.smin_v[k] = x
        self.max_v[k] = x
        if self.lval[k] is not None:
            self.lval[k] = min(self.lval[k], x)

    def update_node_min(self, k, x):
        """ノード全体の最小値のみを x に上げる（必要条件確認済み）。"""
        if self.min_c[k] == 0 or x <= self.min_v[k]:
            return
        old = self.min_v[k]
        self.sum[k] += (x - old) * self.min_c[k]
        if old == self.max_v[k]:
            self.max_v[k] = x
        elif old == self.smax_v[k]:
            self.smax_v[k] = x
        self.min_v[k] = x
        if self.lval[k] is not None:
            self.lval[k] = max(self.lval[k], x)

    def addall(self, k, x):
        """ノード全体へ加算（内部用）。O(1)。"""
        if self.len[k] == 0:
            return
        self.max_v[k] += x
        self.min_v[k] += x
        if self.smax_v[k] != -inf:
            self.smax_v[k] += x
        if self.smin_v[k] != inf:
            self.smin_v[k] += x
        self.sum[k] += self.len[k] * x
        if self.lval[k] is not None:
            self.lval[k] += x
        else:
            self.ladd[k] += x

    def updateall(self, k, x):
        """ノード全体を x に代入（内部用）。O(1)。"""
        if self.len[k] == 0:
            return
        self.max_v[k] = self.min_v[k] = x
        self.smax_v[k] = -inf
        self.smin_v[k] = inf
        self.max_c[k] = self.min_c[k] = self.len[k]
        self.sum[k] = x * self.len[k]
        self.lval[k] = x
        self.ladd[k] = 0

    def push(self, k):
        """未伝播の代入・加算・chmin/chmax 制約を子へ渡す。O(1)。"""
        if k >= self.n0 - 1:
            return
        lc, rc = 2 * k + 1, 2 * k + 2
        if self.lval[k] is not None:
            self.updateall(lc, self.lval[k])
            self.updateall(rc, self.lval[k])
            self.lval[k] = None
            return
        if self.ladd[k]:
            self.addall(lc, self.ladd[k])
            self.addall(rc, self.ladd[k])
            self.ladd[k] = 0
        for c in (lc, rc):
            if self.max_v[c] > self.max_v[k]:
                self.update_node_max(c, self.max_v[k])
            if self.min_v[c] < self.min_v[k]:
                self.update_node_min(c, self.min_v[k])

    def _update_min(self, x, a, b, k, l, r):
        if b <= l or r <= a or self.max_v[k] <= x:
            return
        if a <= l and r <= b and self.smax_v[k] < x:
            self.update_node_max(k, x)
            return
        self.push(k)
        mid = (l + r) >> 1
        self._update_min(x, a, b, 2 * k + 1, l, mid)
        self._update_min(x, a, b, 2 * k + 2, mid, r)
        self.update(k)

    def _update_max(self, x, a, b, k, l, r):
        if b <= l or r <= a or x <= self.min_v[k]:
            return
        # chmax では「2番目に小さい値」を比較する（元コードの smax_v は誤り）。
        if a <= l and r <= b and x < self.smin_v[k]:
            self.update_node_min(k, x)
            return
        self.push(k)
        mid = (l + r) >> 1
        self._update_max(x, a, b, 2 * k + 1, l, mid)
        self._update_max(x, a, b, 2 * k + 2, mid, r)
        self.update(k)

    def _add_val(self, x, a, b, k, l, r):
        if b <= l or r <= a:
            return
        if a <= l and r <= b:
            self.addall(k, x)
            return
        self.push(k)
        mid = (l + r) >> 1
        self._add_val(x, a, b, 2 * k + 1, l, mid)
        self._add_val(x, a, b, 2 * k + 2, mid, r)
        self.update(k)

    def _update_val(self, x, a, b, k, l, r):
        if b <= l or r <= a:
            return
        if a <= l and r <= b:
            self.updateall(k, x)
            return
        self.push(k)
        mid = (l + r) >> 1
        self._update_val(x, a, b, 2 * k + 1, l, mid)
        self._update_val(x, a, b, 2 * k + 2, mid, r)
        self.update(k)

    def update_min(self, a, b, x):
        """[a,b) の各要素を min(A[i],x) に更新（chmin）。償却計算量。"""
        assert 0 <= a <= b <= self.n
        if a != b:
            self._update_min(x, a, b, 0, 0, self.n0)

    range_chmin = update_min

    def update_max(self, a, b, x):
        """[a,b) の各要素を max(A[i],x) に更新（chmax）。償却計算量。"""
        assert 0 <= a <= b <= self.n
        if a != b:
            self._update_max(x, a, b, 0, 0, self.n0)

    range_chmax = update_max

    def add_val(self, a, b, x):
        """[a,b) の各要素に x を足す。O(log N)。"""
        assert 0 <= a <= b <= self.n
        if a != b:
            self._add_val(x, a, b, 0, 0, self.n0)

    range_add = add_val

    def update_val(self, a, b, x):
        """[a,b) の各要素を x にする。O(log N)。"""
        assert 0 <= a <= b <= self.n
        if a != b:
            self._update_val(x, a, b, 0, 0, self.n0)

    range_assign = update_val

    def _query_max(self, a, b, k, l, r):
        if b <= l or r <= a:
            return -inf
        if a <= l and r <= b:
            return self.max_v[k]
        self.push(k)
        mid = (l + r) >> 1
        return max(self._query_max(a, b, 2 * k + 1, l, mid),
                   self._query_max(a, b, 2 * k + 2, mid, r))

    def _query_min(self, a, b, k, l, r):
        if b <= l or r <= a:
            return inf
        if a <= l and r <= b:
            return self.min_v[k]
        self.push(k)
        mid = (l + r) >> 1
        return min(self._query_min(a, b, 2 * k + 1, l, mid),
                   self._query_min(a, b, 2 * k + 2, mid, r))

    def _query_sum(self, a, b, k, l, r):
        if b <= l or r <= a:
            return 0
        if a <= l and r <= b:
            return self.sum[k]
        self.push(k)
        mid = (l + r) >> 1
        return self._query_sum(a, b, 2 * k + 1, l, mid) + self._query_sum(a, b, 2 * k + 2, mid, r)

    def _query_stats(self, a, b, k, l, r):
        if b <= l or r <= a:
            return inf, -inf, 0
        if a <= l and r <= b:
            return self.min_v[k], self.max_v[k], self.sum[k]
        self.push(k)
        mid = (l + r) >> 1
        x = self._query_stats(a, b, 2 * k + 1, l, mid)
        y = self._query_stats(a, b, 2 * k + 2, mid, r)
        return min(x[0], y[0]), max(x[1], y[1]), x[2] + y[2]

    def query_max(self, a, b):
        """[a,b) の最大値。空区間は -inf。O(log N)。"""
        assert 0 <= a <= b <= self.n
        return -inf if a == b else self._query_max(a, b, 0, 0, self.n0)

    def query_min(self, a, b):
        """[a,b) の最小値。空区間は inf。O(log N)。"""
        assert 0 <= a <= b <= self.n
        return inf if a == b else self._query_min(a, b, 0, 0, self.n0)

    def query_sum(self, a, b):
        """[a,b) の和。空区間は 0。O(log N)。"""
        assert 0 <= a <= b <= self.n
        return 0 if a == b else self._query_sum(a, b, 0, 0, self.n0)

    def query(self, a, b):
        """[a,b) の (最小値, 最大値, 和) を一度の探索で返す。O(log N)。"""
        assert 0 <= a <= b <= self.n
        return (inf, -inf, 0) if a == b else self._query_stats(a, b, 0, 0, self.n0)

    def all_max(self):
        return self.max_v[0]

    def all_min(self):
        return self.min_v[0]

    def all_sum(self):
        return self.sum[0]

    def get(self, i):
        """A[i] を取得する。O(log N)。"""
        assert 0 <= i < self.n
        k, l, r = 0, 0, self.n0
        while r - l > 1:
            self.push(k)
            mid = (l + r) >> 1
            if i < mid:
                k = 2 * k + 1
                r = mid
            else:
                k = 2 * k + 2
                l = mid
        return self.sum[k]

    def set(self, i, x):
        """A[i]=x。O(log N)。"""
        assert 0 <= i < self.n
        self.update_val(i, i + 1, x)

    def to_list(self):
        """実要素の配列を返す。保留操作を全展開し、O(N)。"""
        for k in range(self.n0 - 1):
            self.push(k)
        base = self.n0 - 1
        return self.sum[base:base + self.n]

    def __len__(self):
        return self.n

    def __getitem__(self, i):
        return self.get(i)

    def __str__(self):
        return str(self.to_list())

