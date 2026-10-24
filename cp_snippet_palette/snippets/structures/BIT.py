"""Fenwick Tree。APIはshakayami/ACL-for-pythonのfenwick_treeに準拠。

使い方（このファイルを解答の先頭に貼り付けてから実行）
添字は0始まり。sum(l,r)は半開区間、sum0(r)は[0,r)。
    bit = fenwick_tree(3)
    for i, value in enumerate([1, 2, 3]):
        bit.add(i, value)
    bit.add(1, 5)
    bit.sum(0, 2), bit.sum0(2), bit.get(1)  # => (8, 8, 7)
    bit.lower_bound(9)  # 非負列で累積和が9以上となる最初の添字
    # => 2
    fenwick_tree.from_list([1, 2, 3]).to_list()  # => [1, 2, 3]
from_list/get/set/lower_bound/to_listは独自拡張。sumは常に2引数。
"""


class fenwick_tree:
    """Fenwick Tree（区間和）。0-indexed。

    fenwick_tree(N)で全て0。独自拡張from_list(values)なら初期配列からO(N)。
    add(i,x): A[i]+=x、set(i,x): A[i]=x、get(i): A[i]。
    sum(l,r): [l,r) の和（ACL準拠）。
    sum0(r): [0,r)、all_sum(): 全体。
    lower_bound(w): sum0(i+1)>=w を満たす最小の i。なければ n。
    lower_bound は全要素非負（累積和が単調）である場合だけ有効。
    構築 O(N)、get O(1)、add/set/sum/lower_bound O(log N)。
    入力: Nは非負整数の配列長。構築O(N)時間・空間。valuesは初期整数列、p/iは0..N-1、0<=l<=r<=N。xは加算/代入する整数、wは累積和の閾値。
    """

    def __init__(self, N):
        """入力: Nは非負整数の配列長。構築O(N)時間・空間。valuesは初期整数列、p/iは0..N-1、0<=l<=r<=N。xは加算/代入する整数、wは累積和の閾値。
        """
        assert N >= 0
        self.n = N
        self.each = [0] * N
        self.data = [0] * N

    @classmethod
    def from_list(cls, values):
        """独自拡張: 初期配列valuesからO(N)で構築する。
        valuesは長さNの整数列。出力オブジェクトの空間O(N)。
        """
        tree = cls(len(values))
        tree.each = list(values)
        tree.data = list(values)
        for i in range(1, tree.n + 1):
            j = i + (i & -i)
            if j <= tree.n:
                tree.data[j - 1] += tree.data[i - 1]
        return tree

    def sum0(self, r):
        """[0,r) の和。0<=r<=N。O(log N)。"""
        assert 0 <= r <= self.n
        s, data = 0, self.data
        while r:
            s += data[r - 1]
            r -= r & -r
        return s


    def sum(self, l, r):
        """[l,r) の和。O(log N)。"""
        assert 0 <= l <= r <= self.n
        return self.sum0(r) - self.sum0(l)


    def all_sum(self):
        """配列全体の和を返す。O(log n)。"""
        return self.sum0(self.n)

    def add(self, p, x):
        """A[p]+=x。O(log N)。"""
        i = p
        assert 0 <= i < self.n
        i += 1
        self.each[i - 1] += x
        data, n = self.data, self.n
        while i <= n:
            data[i - 1] += x
            i += i & -i

    def get(self, p):
        """A[p]。O(1)。"""
        assert 0 <= p < self.n
        return self.each[p]

    def set(self, p, x):
        """A[p]=x。O(log N)。"""
        self.add(p, x - self.get(p))

    def lower_bound(self, w):
        """sum0(i+1)>=w となる最小 i（0-indexed）。なければ N。

        w<=0 なら 0 を返す。要素が非負であることが前提。O(log N)。
        """
        if w <= 0:
            return 0
        idx = 0
        bit = 1 << (self.n.bit_length() - 1) if self.n else 0
        data, n = self.data, self.n
        while bit:
            nxt = idx + bit
            if nxt <= n and data[nxt - 1] < w:
                w -= data[nxt - 1]
                idx = nxt
            bit >>= 1
        return idx if idx < n else n

    def to_list(self):
        """現在の全要素を新しいlistとして返す。O(n)。"""
        return self.each[:]

    def __getitem__(self, i):
        return self.get(i)

    def __len__(self):
        return self.n

    def __repr__(self):
        return f"{type(self).__name__}({self.to_list()!r})"
