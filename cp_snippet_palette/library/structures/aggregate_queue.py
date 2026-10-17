"""SWAG: 結合的な演算のキュー集約。非可換な関数合成にも対応。
append/popleftは償却O(1)回のop、prodはO(1)回のop、空間O(n)。
op(x,y)は左側xの後ろにyを連結した集約。opは引数を変更しないこと。
PyPy向け。Codonでは要素・単位元・opの戻り値を同じ型にする。コンパイル未確認。
"""


class AggregateQueue:
    """AggregateQueue(op, e)。prod()は先頭から末尾への集約、空ならe。"""

    def __init__(self, op, e):
        self.op = op
        self.e = e
        self._front = []
        self._back = []

    def __len__(self):
        return len(self._front) + len(self._back)

    def append(self, value):
        """末尾へ追加する。"""
        back = self._back
        total = self.op(back[-1][1], value) if back else value
        back.append((value, total))

    def popleft(self):
        """先頭を削除して返す。空ならIndexError。"""
        if not self._front:
            while self._back:
                value = self._back.pop()[0]
                total = self.op(value, self._front[-1][1]) if self._front else value
                self._front.append((value, total))
        if not self._front:
            raise IndexError("pop from empty queue")
        return self._front.pop()[0]

    def prod(self):
        """キュー全体の集約。空なら単位元。"""
        if not self._front:
            return self._back[-1][1] if self._back else self.e
        if not self._back:
            return self._front[-1][1]
        return self.op(self._front[-1][1], self._back[-1][1])

    def clear(self):
        self._front.clear()
        self._back.clear()
