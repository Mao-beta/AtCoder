"""区間加算・区間和の平方分割。出典: PAST003N/PAST014Oのバケット方式を汎用化。
0-indexed・半開区間。O(sqrt n)/操作。PyPy向け、Codonは64bit整数内。

使い方（このファイルを解答の先頭に貼り付けてから実行）
    s = SqrtDecomposition([1, 2, 3, 4])
    s.add(1, 3, 10)
    s.sum(0, 4), s.sum(1, 3)  # => (30, 25)
"""

from math import isqrt


class SqrtDecomposition:
    """初期数列valuesに区間加算・区間和を行う平方分割。
    0-indexed、半開区間。構築O(n)、各操作O(√n)。元配列は変更しない。
    入力: valuesは初期数値列、N=len(values)。構築O(N)時間・空間。0<=l<=r<=Nは整数境界、valueは一律に加える数値。
    """
    def __init__(self, values):
        """入力: valuesは初期数値列、N=len(values)。構築O(N)時間・空間。0<=l<=r<=Nは整数境界、valueは一律に加える数値。
        """
        self.n = len(values)
        self.width = max(1, isqrt(self.n))
        self.data = [
            list(values[i : i + self.width]) for i in range(0, self.n, self.width)
        ]
        self.lazy = [0] * len(self.data)
        self.totals = [sum(row) for row in self.data]

    def _check(self, l, r):
        if not 0 <= l <= r <= self.n:
            raise IndexError("invalid range")

    def add(self, l, r, value):
        """[l,r)の各要素にvalueを足す。0<=l<=r<=n。戻り値なし。
        時間O(sqrt(N)+1)、追加空間O(1)。
        """
        self._check(l, r)
        while l < r:
            b, i = divmod(l, self.width)
            take = min(r - l, len(self.data[b]) - i)
            if i == 0 and take == len(self.data[b]):
                self.lazy[b] += value
            else:
                for j in range(i, i + take):
                    self.data[b][j] += value
            self.totals[b] += take * value
            l += take

    def sum(self, l, r):
        """[l,r)の和を返す。空区間なら0。
        時間O(sqrt(N)+1)、追加空間O(1)。
        """
        self._check(l, r)
        result = 0
        while l < r:
            b, i = divmod(l, self.width)
            take = min(r - l, len(self.data[b]) - i)
            if i == 0 and take == len(self.data[b]):
                result += self.totals[b]
            else:
                result += sum(self.data[b][i : i + take]) + take * self.lazy[b]
            l += take
        return result
