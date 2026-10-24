"""Implicit Treapによる動的数列。挿入・削除・反転・区間一次変換・区間和。
0-indexed、半開区間。構築O(N)、各操作は期待O(log N)、空間O(N+挿入回数)。
mod=998244353が既定、mod=0なら剰余を取らず整数として計算する。
優先度は内部の疑似乱数で生成。再帰の深さは期待O(log N)。PyPy向け、Codon未確認。
厳密な最悪計算量保証はない。削除したノードの領域は再利用しない。

使い方（このファイルを解答の先頭に貼り付けてから実行）
    s = DynamicSequence([1, 2, 3])
    s.insert(1, 9)  # [1,9,2,3]
    s.reverse(1, 4)  # [1,3,2,9]
    s.apply(0, 2, 2, 1)  # [3,7,2,9]
    s.prod(0, 3), s.erase(3), s.get(1), len(s)  # => (12, 9, 7, 3)
    s.to_list()  # => [3, 7, 2]
"""


class DynamicSequence:
    """valuesを初期値とする動的数列。区間和prodと一次変換applyに対応。
    modは0または正の整数。負の添字は不可。元のvaluesは変更しない。
    入力: valuesは初期値の整数列（省略は空）、modは非負整数で0なら剰余なし。Nは現在の要素数。構築は単調スタックでO(N)時間・空間。
    操作のiは0-indexed、0<=l<=r<=N、a/bは一次変換の整数係数。通常の各操作は期待O(log(N+1))、最悪O(N)。
    削除ノードも配列に残るため保持空間は累計挿入数に依存する。
    """

    def __init__(self, values=(), mod=998244353):
        """入力: valuesは初期値の整数列（省略は空）、modは非負整数で0なら剰余なし。Nは現在の要素数。構築は単調スタックでO(N)時間・空間。
        操作のiは0-indexed、0<=l<=r<=N、a/bは一次変換の整数係数。通常の各操作は期待O(log(N+1))、最悪O(N)。
        削除ノードも配列に残るため保持空間は累計挿入数に依存する。
        """
        if mod < 0:
            raise ValueError("mod must be nonnegative")
        self.mod, self._seed = mod, 2463534242
        self._left, self._right, self._size = [0], [0], [0]
        self._value, self._sum, self._priority = [0], [0], [0]
        self._rev, self._mul, self._add = [False], [1], [0]
        stack = []
        for value in values:
            node, last = self._new(value), 0
            while stack and self._priority[stack[-1]] < self._priority[node]:
                last = stack.pop()
                self._pull(last)
            self._left[node] = last
            if stack:
                self._right[stack[-1]] = node
            stack.append(node)
        self._root = stack[0] if stack else 0
        for node in reversed(stack):
            self._pull(node)

    def __len__(self):
        return self._size[self._root]

    def _new(self, value):
        x = self._seed
        x ^= (x << 13) & 0xFFFFFFFF
        x ^= x >> 17
        x ^= (x << 5) & 0xFFFFFFFF
        self._seed = x
        value = value % self.mod if self.mod else value
        self._left.append(0)
        self._right.append(0)
        self._size.append(1)
        self._value.append(value)
        self._sum.append(value)
        self._priority.append(x)
        self._rev.append(False)
        self._mul.append(1)
        self._add.append(0)
        return len(self._size) - 1

    def _pull(self, t):
        l, r = self._left[t], self._right[t]
        self._size[t] = self._size[l] + self._size[r] + 1
        total = self._sum[l] + self._sum[r] + self._value[t]
        self._sum[t] = total % self.mod if self.mod else total

    def _affine(self, t, a, b):
        if not t:
            return
        self._value[t] = a * self._value[t] + b
        self._sum[t] = a * self._sum[t] + b * self._size[t]
        self._mul[t] *= a
        self._add[t] = a * self._add[t] + b
        if self.mod:
            self._value[t] %= self.mod
            self._sum[t] %= self.mod
            self._mul[t] %= self.mod
            self._add[t] %= self.mod

    def _reverse(self, t):
        if t:
            self._left[t], self._right[t] = self._right[t], self._left[t]
            self._rev[t] = not self._rev[t]

    def _push(self, t):
        l, r = self._left[t], self._right[t]
        if self._rev[t]:
            self._reverse(l)
            self._reverse(r)
            self._rev[t] = False
        a, b = self._mul[t], self._add[t]
        if a != 1 or b != 0:
            self._affine(l, a, b)
            self._affine(r, a, b)
            self._mul[t], self._add[t] = 1, 0

    def _split(self, t, k):
        if not t:
            return 0, 0
        self._push(t)
        size = self._size[self._left[t]]
        if k <= size:
            a, self._left[t] = self._split(self._left[t], k)
            self._pull(t)
            return a, t
        self._right[t], b = self._split(self._right[t], k - size - 1)
        self._pull(t)
        return t, b

    def _merge(self, a, b):
        if not a or not b:
            return a or b
        if self._priority[a] >= self._priority[b]:
            self._push(a)
            self._right[a] = self._merge(self._right[a], b)
            self._pull(a)
            return a
        self._push(b)
        self._left[b] = self._merge(a, self._left[b])
        self._pull(b)
        return b

    def _range(self, l, r):
        if not 0 <= l <= r <= len(self):
            raise IndexError("invalid range")
        a, b = self._split(self._root, l)
        b, c = self._split(b, r - l)
        return a, b, c

    def insert(self, i, value):
        """位置iの直前へ挿入する。i==len(s)なら末尾。期待O(log N)。
        valueは挿入する整数値。
        """
        if not 0 <= i <= len(self):
            raise IndexError("invalid index")
        a, b = self._split(self._root, i)
        self._root = self._merge(self._merge(a, self._new(value)), b)

    def erase(self, i):
        """位置iを削除し、その値を返す。期待O(log N)。"""
        a, b, c = self._range(i, i + 1)
        value = self._value[b]
        self._root = self._merge(a, c)
        return value

    def reverse(self, l, r):
        """[l,r)の順序を反転する。期待O(log N)。"""
        a, b, c = self._range(l, r)
        self._reverse(b)
        self._root = self._merge(self._merge(a, b), c)

    def apply(self, l, r, a, b):
        """[l,r)の各値xをa*x+bに置き換える。mod>0なら剰余を取る。期待O(log N)。"""
        x, y, z = self._range(l, r)
        if self.mod:
            a, b = a % self.mod, b % self.mod
        self._affine(y, a, b)
        self._root = self._merge(self._merge(x, y), z)

    def prod(self, l, r):
        """[l,r)の和。空区間は0。mod>0なら剰余を返す。期待O(log N)。"""
        a, b, c = self._range(l, r)
        result = self._sum[b]
        self._root = self._merge(self._merge(a, b), c)
        return result

    def get(self, i):
        """位置iの値を返す。期待O(log N)。"""
        return self.prod(i, i + 1)

    def to_list(self):
        """現在の要素を順に並べた新しいlistを返す。O(N)。"""
        result, stack, t = [], [], self._root
        while stack or t:
            while t:
                self._push(t)
                stack.append(t)
                t = self._left[t]
            t = stack.pop()
            result.append(self._value[t])
            t = self._right[t]
        return result
