"""追加・削除に対応するmex（存在しない最小の非負整数）。更新O(log limit)、取得O(1)。
0..limitの個数を管理する。値域外はmexに影響しない前提で無視する。
集合の最大要素数<=limitなら、この範囲だけで必ず正確なmexが見つかる。

使い方（このファイル全体を貼り付けてから実行）
    mex = DynamicMex(4, [0, 1, 1, 3])
    mex.mex()  # => 2
    mex.discard(1)
    mex.mex()  # => 2
    mex.add(2)
    mex.mex()  # => 4
    mex.discard(0)
    mex.mex()  # => 0
"""


class DynamicMex:
    """DynamicMex(limit, values=())。初期構築O(limit+N)、追加空間O(limit)。
    0..limitが全て存在するとmex()はNone。上限外のmexを推測して返すことはない。
    入力: limitは追跡する最大値Lの非負整数、valuesは初期多重集合の整数列。Nは初期要素数。値域0..L以外は無視する。構築O(L+N+1)時間・O(L+1)空間。
    以後のvalueも整数。
    """

    def __init__(self, limit, values=()):
        """入力: limitは追跡する最大値Lの非負整数、valuesは初期多重集合の整数列。Nは初期要素数。値域0..L以外は無視する。構築O(L+N+1)時間・O(L+1)空間。
        以後のvalueも整数。
        """
        assert limit >= 0
        self.limit = limit
        self._freq = [0] * (limit + 1)
        for value in values:
            if 0 <= value <= limit:
                self._freq[value] += 1
        self._size = 1 << limit.bit_length()
        self._tree = [limit + 1] * (2 * self._size)
        for i, count in enumerate(self._freq):
            if count == 0:
                self._tree[self._size + i] = i
        for i in range(self._size - 1, 0, -1):
            self._tree[i] = min(self._tree[2 * i], self._tree[2 * i + 1])

    def _update(self, value):
        i = self._size + value
        self._tree[i] = value if self._freq[value] == 0 else self.limit + 1
        while i > 1:
            i >>= 1
            self._tree[i] = min(self._tree[2 * i], self._tree[2 * i + 1])

    def add(self, value):
        """valueを1個追加。値域外は無視。O(log limit)。"""
        if 0 <= value <= self.limit:
            self._freq[value] += 1
            if self._freq[value] == 1:
                self._update(value)

    def discard(self, value):
        """valueを1個削除。追跡範囲内で実際に削除したらTrue、それ以外False。
        時間O(log(limit+2))、追加空間O(1)。
        """
        if not 0 <= value <= self.limit or self._freq[value] == 0:
            return False
        self._freq[value] -= 1
        if self._freq[value] == 0:
            self._update(value)
        return True

    def mex(self):
        """0..limit内の最小の欠損値、全て存在すればNone。O(1)。"""
        value = self._tree[1]
        return value if value <= self.limit else None
