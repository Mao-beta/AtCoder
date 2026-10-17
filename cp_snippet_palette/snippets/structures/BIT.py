"""競プロ用スニペット。単体で貼り付け可能。2026-10-17版。"""


class FenwickTree:
    """Fenwick Tree（区間和）。0-indexed。

    FenwickTree(n=0)。拡張として初期配列も O(N) で構築可能。
    add(i,x): A[i]+=x、set(i,x): A[i]=x、get(i): A[i]。
    sum(left,right): [left,right) の和（ACL準拠）。
    prefix_sum(r): [0,r)、prod(l,r): [l,r)、all_sum(): 全体。
    lower_bound(w): prefix_sum(i+1)>=w を満たす最小の i。なければ n。
    lower_bound は全要素非負（累積和が単調）である場合だけ有効。
    構築 O(N)、get O(1)、add/set/sum/prod/lower_bound O(log N)。
    """

    def __init__(self, n=0):
        if isinstance(n, int):
            assert n >= 0
            arr = [0] * n
        else:
            arr = list(n)
        self.n = len(arr)
        self.each = [0] + arr[:]  # 元コードの 1-indexed 内部配列を維持
        self.data = self.each[:]
        for i in range(1, self.n + 1):
            j = i + (i & -i)
            if j <= self.n:
                self.data[j] += self.data[i]

    def prefix_sum(self, r):
        """[0,r) の和。0<=r<=N。O(log N)。"""
        assert 0 <= r <= self.n
        s, data = 0, self.data
        while r:
            s += data[r]
            r -= r & -r
        return s

    def sum(self, left, right):
        """[left,right) の和。ACLと同じ2引数。O(log N)。"""
        return self.prod(left, right)

    def prod(self, l, r):
        """[l,r) の和。O(log N)。"""
        assert 0 <= l <= r <= self.n
        return self.prefix_sum(r) - self.prefix_sum(l)

    range_sum = prod

    def all_sum(self):
        return self.prefix_sum(self.n)

    def add(self, i, x):
        """A[i]+=x。O(log N)。"""
        assert 0 <= i < self.n
        i += 1
        self.each[i] += x
        data, n = self.data, self.n
        while i <= n:
            data[i] += x
            i += i & -i

    def get(self, i):
        """A[i]。O(1)。"""
        assert 0 <= i < self.n
        return self.each[i + 1]

    def set(self, i, x):
        """A[i]=x。O(log N)。"""
        self.add(i, x - self.get(i))

    def lower_bound(self, w):
        """prefix_sum(i+1)>=w となる最小 i（0-indexed）。なければ N。

        w<=0 なら 0 を返す。要素が非負であることが前提。O(log N)。
        """
        if w <= 0:
            return 0
        idx = 0
        bit = 1 << (self.n.bit_length() - 1) if self.n else 0
        data, n = self.data, self.n
        while bit:
            nxt = idx + bit
            if nxt <= n and data[nxt] < w:
                w -= data[nxt]
                idx = nxt
            bit >>= 1
        return idx if idx < n else n

    def to_list(self):
        return self.each[1:]

    def __getitem__(self, i):
        return self.get(i)

    def __len__(self):
        return self.n

    def __repr__(self):
        return f"{type(self).__name__}({self.to_list()!r})"


class BIT(FenwickTree):
    """旧コード用。sum(i)=[0,i] を保持。新規コードはFenwickTreeを使う。"""

    def sum(self, left, right=None):
        if right is None:
            assert -1 <= left < self.n
            return self.prefix_sum(left + 1)
        return super().sum(left, right)
