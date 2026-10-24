"""両端キューの集約。結合則と単位元があれば非可換な演算にも対応。
両端の追加・削除は償却O(1)回のop、prodはO(1)回、空間O(n)。
片側が空になった際に半分ずつ再構築する。PyPy向け、Codon未確認。

使い方（このファイルを解答の先頭に貼り付けてから実行）
    d = AggregateDeque(lambda a, b: a + b, '')
    d.append('b'); d.appendleft('a'); d.append('c')
    d.prod(), d.popleft(), d.pop(), d.prod()  # => ('abc', 'a', 'c', 'b')
    mod = 998244353
    compose = lambda f, g: (g[0]*f[0] % mod, (g[0]*f[1]+g[1]) % mod)
    d = AggregateDeque(compose, (1, 0))
    d.append((2, 1)); d.append((3, 4))
    a, b = d.prod()
    (a*10+b) % mod  # => 67
"""


class AggregateDeque:
    """op(a,b)で左側aの後ろに右側bを連結する。eは左右の単位元。
    opは引数を変更しないこと。len(d)は要素数。
    入力: opは二つの集約値を同じ型の値へ結合する関数、eは左右の単位元。opは結合則を満たし引数を変更しないこと。構築O(1)時間・空間。valueはopが受け取れる要素。
    Nは現在の要素数、保持領域O(N)。以下はopと要素のコピーをO(1)とした計算量。
    """

    def __init__(self, op, e):
        """入力: opは二つの集約値を同じ型の値へ結合する関数、eは左右の単位元。opは結合則を満たし引数を変更しないこと。構築O(1)時間・空間。valueはopが受け取れる要素。
        Nは現在の要素数、保持領域O(N)。以下はopと要素のコピーをO(1)とした計算量。
        """
        self.op, self.e = op, e
        self._left, self._right = [], []

    def __len__(self):
        return len(self._left) + len(self._right)

    def appendleft(self, value):
        """先頭へvalueを追加する。償却O(1)回のop。"""
        stack = self._left
        stack.append((value, self.op(value, stack[-1][1]) if stack else value))

    def append(self, value):
        """末尾へvalueを追加する。償却O(1)回のop。
        時間は償却O(1)回のop、1回の再配置は最悪O(N)。
        """
        stack = self._right
        stack.append((value, self.op(stack[-1][1], value) if stack else value))

    def _balance(self, left):
        values = [x[0] for x in reversed(self._left)] + [x[0] for x in self._right]
        if not values:
            raise IndexError("pop from empty deque")
        middle = (len(values) + int(left)) // 2
        self._left.clear()
        self._right.clear()
        for value in reversed(values[:middle]):
            self.appendleft(value)
        for value in values[middle:]:
            self.append(value)

    def popleft(self):
        """先頭を削除して返す。空ならIndexError。償却O(1)回のop。
        時間は償却O(1)回のop、1回の再配置は最悪O(N)。
        """
        if not self._left:
            self._balance(True)
        return self._left.pop()[0]

    def pop(self):
        """末尾を削除して返す。空ならIndexError。償却O(1)回のop。"""
        if not self._right:
            self._balance(False)
        return self._right.pop()[0]

    def prod(self):
        """先頭から末尾の順の集約。空ならe。O(1)回のop。
        時間・追加空間O(1)回のop。
        """
        a = self._left[-1][1] if self._left else self.e
        b = self._right[-1][1] if self._right else self.e
        return self.op(a, b)

    def clear(self):
        """全要素を削除する。
        時間O(N)（保持参照の解放）、追加空間O(1)。
        """
        self._left.clear()
        self._right.clear()
