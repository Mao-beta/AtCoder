"""競プロ用スニペット。単体で貼り付け可能。2026-10-17版。

使い方（このファイルを解答の先頭に貼り付けてから実行）
    h = Heapq([3, 1, 3])
    h.discard(3), h.count(3), len(h)  # => (True, 1, 2)
    h.push(2)
    h.top(), h.pop(), h.pop(), h.pop()  # => (1, 1, 2, 3)
    bool(h)  # => False
    # 空のtop/popはIndexError
"""

from collections import Counter
from heapq import heapify, heappop, heappush


class Heapq:
    """heapq を使う削除可能な最小ヒープ（遅延削除方式）。

    push / pop / top / discard / build を提供。
    discard(x): 存在する x のうち1個を削除し True、なければ False。
    top / pop: 空ならIndexError。
    len(H): 論理上存在する要素数。count(x): x の個数。
    push / pop / discard は償却 O(log N)、top も _clean が必要なときは
    償却 O(log N)（_clean 不要なら O(1)）。compact() は O(N)。
    削除済み要素が多い場合は自動的に再構築してメモリを抑える。
    入力: iterableは大小比較可能かつhashableな要素の列。Nは初期要素数、構築O(N)時間・空間。
    xは追加/削除/計数する値、aは再構築用の列。Hは保留削除を含む物理ヒープの長さ。
    """

    def __init__(self, iterable=()):
        """入力: iterableは大小比較可能かつhashableな要素の列。Nは初期要素数、構築O(N)時間・空間。
        xは追加/削除/計数する値、aは再構築用の列。Hは保留削除を含む物理ヒープの長さ。
        """
        self.q = []
        self.p = []
        self.C = Counter()
        self._size = 0
        self.build(iterable)

    def build(self, a):
        """入力をコピーして再構築。既存の保留削除も消す。O(N)。"""
        self.q = list(a)
        heapify(self.q)
        self.p = []
        self.C = Counter(self.q)
        self._size = len(self.q)

    def push(self, x):
        """xを1個追加する。重複可。戻り値なし。償却O(log n)。
        """
        heappush(self.q, x)
        self.C[x] += 1
        self._size += 1

    def discard(self, x):
        """現在存在する x を1個削除する。なければ False。
        時間は掃除を含め償却O(log(H+1))。1回でD個の古い要素を除く場合O((D+1) log(H+1))。
        """
        if self.C.get(x, 0) == 0:
            return False
        self.C[x] -= 1
        if self.C[x] == 0:
            del self.C[x]
        self._size -= 1
        heappush(self.p, x)
        self._clean()
        if len(self.q) > max(64, 2 * self._size):
            self.compact()
        return True

    def compact(self):
        """論理上存在する要素だけでヒープを作り直す。O(N)。"""
        self.q = list(self.C.elements())
        heapify(self.q)
        self.p = []

    def _clean(self):
        """削除予約と物理ヒープの最小値が一致する限り掃除する。
        削除する古い要素数Dに対してO((D+1) log(H+1))時間、追加空間O(1)。Hは物理ヒープ長。
        """
        q, p = self.q, self.p
        while q and p and q[0] == p[0]:
            heappop(q)
            heappop(p)

    def pop(self):
        """最小値を取り出す。空ならIndexError。
        時間は掃除を含め償却O(log(H+1))。1回でD個の古い要素を除く場合O((D+1) log(H+1))。
        """
        self._clean()
        if not self.q:
            raise IndexError("empty heap")
        x = heappop(self.q)
        self.C[x] -= 1
        if self.C[x] == 0:
            del self.C[x]
        self._size -= 1
        return x

    def top(self):
        """最小値を返す（削除しない）。空ならIndexError。
        時間は掃除を含め償却O(log(H+1))。1回でD個の古い要素を除く場合O((D+1) log(H+1))。
        """
        self._clean()
        if not self.q:
            raise IndexError("empty heap")
        return self.q[0]


    def count(self, x):
        """現在存在するxの個数を返す。遅延削除済みの個体は含めない。O(1)。
        """
        return self.C.get(x, 0)

    def __contains__(self, x):
        return self.C.get(x, 0) > 0

    def __len__(self):
        return self._size

    def __bool__(self):
        return self._size > 0

