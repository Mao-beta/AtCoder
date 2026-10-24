"""値候補を事前登録する多重集合。順位・小さい順k個の和・絶対値和をO(log σ)で処理。
二本のFenwick木で個数と総和を管理。負数・重複可、全メソッドは元の値を受け取る。
候補が未知のオンライン挿入にはSortedMultiset等を使う。Codonコンパイル未確認。

使い方（このファイル全体を貼り付けてから実行）
    bag = FenwickMultiset([1, 3, 5, 8], [5, 1, 5, 3])
    bag.kth(2), bag.sum_smallest(3), bag.sum_largest(2)  # => (5, 9, 10)
    bag.count(5), bag.bisect_left(5), bag.bisect_right(5)  # => (2, 2, 4)
    bag.discard(5)
    bag.add(8)
    len(bag), bag.total, bag.sum_abs(4)  # => (4, 17, 9)
"""

from bisect import bisect_left, bisect_right


class FenwickMultiset:
    """FenwickMultiset(universe, values=())。universeは今後追加する全ての値。
    構築O(σ log σ+N log σ)、空間O(σ)。totalは総和、lenは重複込みの個数。
    入力: universeは今後登録する全整数値の列、valuesは初期要素の整数列。Uはuniverseの長さ、σは異なる登録値数、Nは初期要素数。
    構築O(U+σ log(σ+1)+N log(σ+1))期待時間・O(σ)空間。countは追加削除個数の非負整数、kは順位または取得個数。
    """

    def __init__(self, universe, values=()):
        """入力: universeは今後登録する全整数値の列、valuesは初期要素の整数列。Uはuniverseの長さ、σは異なる登録値数、Nは初期要素数。
        構築O(U+σ log(σ+1)+N log(σ+1))期待時間・O(σ)空間。countは追加削除個数の非負整数、kは順位または取得個数。
        """
        self._values = sorted(set(universe))
        self._index = {v: i for i, v in enumerate(self._values)}
        n = len(self._values)
        self._freq, self._count, self._sum = [0] * n, [0] * (n + 1), [0] * (n + 1)
        self._size, self.total = 0, 0
        for value in values:
            self.add(value)

    def __len__(self):
        return self._size

    def _prefix(self, tree, r):
        value = 0
        while r:
            value += tree[r]
            r -= r & -r
        return value

    def _change(self, i, count):
        value = self._values[i]
        self._freq[i] += count
        self._size += count
        self.total += value * count
        i += 1
        while i < len(self._count):
            self._count[i] += count
            self._sum[i] += value * count
            i += i & -i

    def add(self, value, count=1):
        """事前登録済みvalueをcount個追加。count>=0。未登録値はKeyError。
        時間O(log(σ+1))、追加空間O(1)。σは異なる登録値数。valueは整数。
        """
        assert count >= 0
        self._change(self._index[value], count)

    def discard(self, value, count=1):
        """最大count個削除し、実際に削除した個数を返す。未登録・存在しない値は0。
        時間O(log(σ+1))、追加空間O(1)。σは異なる登録値数。valueは整数。
        """
        assert count >= 0
        i = self._index.get(value)
        if i is None:
            return 0
        removed = min(count, self._freq[i])
        self._change(i, -removed)
        return removed

    def count(self, value):
        """valueの個数。O(1)期待時間。未登録なら0。"""
        i = self._index.get(value)
        return self._freq[i] if i is not None else 0

    def bisect_left(self, value):
        """value未満の要素数。valueは未登録でもよい。O(log σ)。"""
        return self._prefix(self._count, bisect_left(self._values, value))

    def bisect_right(self, value):
        """value以下の要素数。O(log σ)。"""
        return self._prefix(self._count, bisect_right(self._values, value))

    def _select(self, k):
        index, count, total = 0, 0, 0
        step = 1 << (len(self._values).bit_length() - 1)
        while step:
            nxt = index + step
            if nxt < len(self._count) and count + self._count[nxt] <= k:
                index = nxt
                count += self._count[nxt]
                total += self._sum[nxt]
            step >>= 1
        return index, count, total

    def kth(self, k):
        """0-indexedでk番目に小さい値。0<=k<len(self)。O(log σ)。"""
        if not 0 <= k < self._size:
            raise IndexError("rank out of range")
        return self._values[self._select(k)[0]]

    def sum_smallest(self, k):
        """小さい順にk個取った和。0<=k<=len(self)、k=0なら0。O(log σ)。"""
        assert 0 <= k <= self._size
        if k == self._size:
            return self.total
        if k == 0:
            return 0
        i, count, total = self._select(k)
        return total + (k - count) * self._values[i]

    def sum_largest(self, k):
        """大きい順にk個取った和。0<=k<=len(self)。O(log σ)。"""
        assert 0 <= k <= self._size
        return self.total - self.sum_smallest(self._size - k)

    def sum_abs(self, value):
        """sum(abs(x-value))。valueは未登録でもよい。中央値の最小化にも使える。
        時間O(log(σ+1))、追加空間O(1)。σは異なる登録値数。valueは整数。
        """
        i = bisect_left(self._values, value)
        count, total = self._prefix(self._count, i), self._prefix(self._sum, i)
        return value * count - total + self.total - total - value * (self._size - count)
