"""競プロ用スニペット。単体で貼り付け可能。2026-10-17版。

使い方（このファイルを解答の先頭に貼り付けてから実行）
    q = KindDeque([1, 2, 1])
    q.kind, q.count(1), len(q)  # => (2, 2, 3)
    q.popleft(), q.popleft(), q.kind  # => (1, 2, 1)
    q.append(3)
    list(q), q.kind  # => ([1, 3], 2)
"""

from collections import Counter, deque


class KindDeque:
    """要素の出現数と異なる値の種類数を O(1) で追跡する deque。

    D: 実体の collections.deque
    C[x]: 値 x の個数（存在しないキーでも 0、通常の Counter と同じ）
    kind: 現在の異なる値の種類数

    要素はハッシュ可能であること。両端操作・count・kind は償却 O(1)。
    入力: iterableはhashableな要素の列。Nは初期要素数。構築O(N)期待時間・O(N)空間。xは任意のhashable値、kは符号付き整数の回転量。
    """

    def __init__(self, iterable=()):
        """入力: iterableはhashableな要素の列。Nは初期要素数。構築O(N)期待時間・O(N)空間。xは任意のhashable値、kは符号付き整数の回転量。
        """
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
        """右端へhashableなxを1個追加し、出現数・種類数を更新する。戻り値なし。
        償却O(1)回のdeque/辞書操作（期待時間）。
        """
        self.D.append(x)
        if self.C[x] == 0:
            self._k += 1
        self.C[x] += 1

    def appendleft(self, x):
        """左端へhashableなxを1個追加し、出現数・種類数を更新する。戻り値なし。
        償却O(1)回のdeque/辞書操作（期待時間）。
        """
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
        """iterableを順に右端へ追加する。O(k)。
        """
        for x in iterable:
            self.append(x)

    def extendleft(self, iterable):
        """deque と同じく、入力の順番を反転して左側へ追加する。
        iterableは追加要素の列、Kはその個数。時間O(K)期待、追加要素の空間O(K)。
        """
        for x in iterable:
            self.appendleft(x)

    def rotate(self, k=1):
        """右に k 個回転する。出現数は不変。
        現在の要素数N、t=k mod Nに対しO(1+min(t,N-t))時間・O(1)追加空間。空の場合O(1)。
        """
        self.D.rotate(k)

    def clear(self):
        """全要素と出現数を消し、kindを0にする。戻り値なし。
        時間O(N)、追加空間O(1)。
        """
        self.D.clear()
        self.C.clear()
        self._k = 0

    def __repr__(self):
        return f"KindDeque({list(self.D)!r})"

