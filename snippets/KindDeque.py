"""競プロ用スニペット。単体で貼り付け可能。2026-10-17版。"""

from collections import Counter, deque


class KindDeque:
    """要素の出現数と異なる値の種類数を O(1) で追跡する deque。

    D: 実体の collections.deque
    C[x]: 値 x の個数（存在しないキーでも 0、通常の Counter と同じ）
    kind: 現在の異なる値の種類数

    要素はハッシュ可能であること。両端操作・count・kind は償却 O(1)。
    """

    def __init__(self, iterable=()):
        self.D = deque(iterable)
        self.C = Counter(self.D)
        self._k = len(self.C)

    @property
    def kind(self):
        """現在存在する値の種類数。O(1)。"""
        return self._k

    def __len__(self):
        return len(self.D)

    def __iter__(self):
        return iter(self.D)

    def __getitem__(self, i):
        """deque 同様、中央の添字アクセスは O(N)。"""
        return self.D[i]

    def __contains__(self, x):
        return self.C.get(x, 0) > 0

    def count(self, x):
        """x の個数を返す。O(1)。"""
        return self.C.get(x, 0)

    def append(self, x):
        self.D.append(x)
        if self.C[x] == 0:
            self._k += 1
        self.C[x] += 1

    def appendleft(self, x):
        self.D.appendleft(x)
        if self.C[x] == 0:
            self._k += 1
        self.C[x] += 1

    def _remove_count(self, x):
        if self.C[x] == 1:
            del self.C[x]
            self._k -= 1
        else:
            self.C[x] -= 1

    def pop(self):
        """右端から取り出して返す。空なら IndexError。O(1)。"""
        x = self.D.pop()
        self._remove_count(x)
        return x

    def popleft(self):
        """左端から取り出して返す。空なら IndexError。O(1)。"""
        x = self.D.popleft()
        self._remove_count(x)
        return x

    def extend(self, iterable):
        for x in iterable:
            self.append(x)

    def extendleft(self, iterable):
        """deque と同じく、入力の順番を反転して左側へ追加する。"""
        for x in iterable:
            self.appendleft(x)

    def rotate(self, k=1):
        """右に k 個回転する。出現数は不変。"""
        self.D.rotate(k)

    def clear(self):
        self.D.clear()
        self.C.clear()
        self._k = 0

    def __repr__(self):
        return f"KindDeque({list(self.D)!r})"

