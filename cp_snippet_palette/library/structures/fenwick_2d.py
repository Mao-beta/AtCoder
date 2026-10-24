"""更新座標を事前登録する、座標圧縮付き二次元Fenwick木。
点加算・長方形和O(log² N)、構築O(N log² N)、空間O(N log N)。
座標は整数、和は通常の整数。負の加算も可能。PyPy向け、Codon未確認。

使い方（このファイルを解答の先頭に貼り付けてから実行）
    bit = OfflineFenwick2D([(1, 2), (4, 3)])  # 全ての更新先を先に登録
    bit.add(1, 2, 5); bit.add(4, 3, 7)
    bit.sum(0, 0, 4, 4), bit.sum(0, 0, 5, 4)  # => (5, 12)
    bit.add(1, 2, -2)
    bit.prefix_sum(4, 3)  # => 3（x<4 かつ y<3）
"""

from bisect import bisect_left


class OfflineFenwick2D:
    """points=[(x,y),...]は全更新先。重複可。初期値は全点0。
    クエリの境界座標は登録不要。未登録の点へのaddはValueError。
    入力: pointsは今後更新する全座標(x,y)の整数tupleの列。N=len(points)。構築O(N log²(N+1))時間・O(N log(N+1))空間。
    x/yや長方形境界は元の座標値、valueは加算する整数。
    """

    def __init__(self, points):
        """入力: pointsは今後更新する全座標(x,y)の整数tupleの列。N=len(points)。構築O(N log²(N+1))時間・O(N log(N+1))空間。
        x/yや長方形境界は元の座標値、valueは加算する整数。
        """
        points = list(set(points))
        self._points = set(points)
        self._xs = sorted({x for x, y in points})
        n = len(self._xs)
        self._ys = [[] for _ in range(n + 1)]
        for x, y in points:
            i = bisect_left(self._xs, x) + 1
            while i <= n:
                self._ys[i].append(y)
                i += i & -i
        self._ys = [sorted(set(row)) for row in self._ys]
        self._bit = [[0] * (len(row) + 1) for row in self._ys]

    def add(self, x, y, value):
        """登録済みの点(x,y)へvalueを加算する。O(log² N)。"""
        if (x, y) not in self._points:
            raise ValueError("update coordinate was not registered")
        i = bisect_left(self._xs, x) + 1
        while i < len(self._ys):
            j = bisect_left(self._ys[i], y) + 1
            row = self._bit[i]
            while j < len(row):
                row[j] += value
                j += j & -j
            i += i & -i

    def prefix_sum(self, x, y):
        """座標がx未満かつy未満である全点の和。O(log² N)。"""
        total = 0
        i = bisect_left(self._xs, x)
        while i:
            j = bisect_left(self._ys[i], y)
            row = self._bit[i]
            while j:
                total += row[j]
                j -= j & -j
            i -= i & -i
        return total

    def sum(self, left, bottom, right, top):
        """[left,right)×[bottom,top)の和。空の長方形は0。O(log² N)。"""
        if left > right or bottom > top:
            raise ValueError("reversed rectangle")
        return (
            self.prefix_sum(right, top)
            - self.prefix_sum(left, top)
            - self.prefix_sum(right, bottom)
            + self.prefix_sum(left, bottom)
        )
