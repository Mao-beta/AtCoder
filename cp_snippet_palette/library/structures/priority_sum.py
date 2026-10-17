"""小さい方からk個の和。出典: ABC306Eと既存Heapq。
k=0・重複・存在しない値の削除・k変更に対応。更新償却O(log n)、query O(1)。
PyPy向け。CodonのCounter対応は未確認。
"""

from collections import Counter
from heapq import heapify, heappop, heappush


class _PriorityHeap:
    """heapq を使う削除可能な最小ヒープ（遅延削除方式）。

    push / pop / top / erase / clean / build を提供。
    erase(x): 存在する x のうち1個を削除し True、なければ False。
    top / pop: 空なら exc（デフォルト None）。
    len(H): 論理上存在する要素数。count(x): x の個数。
    push / pop / erase は償却 O(log N)、top も clean が必要なときは
    償却 O(log N)（clean 不要なら O(1)）。compact() は O(N)。
    削除済み要素が多い場合は自動的に再構築してメモリを抑える。
    """

    def __init__(self, iterable=()):
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
        heappush(self.q, x)
        self.C[x] += 1
        self._size += 1

    def erase(self, x):
        """現在存在する x を1個削除する。なければ False。"""
        if self.C.get(x, 0) == 0:
            return False
        self.C[x] -= 1
        if self.C[x] == 0:
            del self.C[x]
        self._size -= 1
        heappush(self.p, x)
        self.clean()
        if len(self.q) > max(64, 2 * self._size):
            self.compact()
        return True

    def compact(self):
        """論理上存在する要素だけでヒープを作り直す。O(N)。"""
        self.q = list(self.C.elements())
        heapify(self.q)
        self.p = []

    def clean(self):
        """削除予約と物理ヒープの最小値が一致する限り掃除する。"""
        q, p = self.q, self.p
        while q and p and q[0] == p[0]:
            heappop(q)
            heappop(p)

    def pop(self, exc=None):
        """最小値を取り出す。空なら exc。"""
        self.clean()
        if not self.q:
            return exc
        x = heappop(self.q)
        self.C[x] -= 1
        if self.C[x] == 0:
            del self.C[x]
        self._size -= 1
        return x

    def top(self, exc=None):
        """最小値を返す（削除しない）。空なら exc。"""
        self.clean()
        return self.q[0] if self.q else exc

    peek = top

    def count(self, x):
        return self.C.get(x, 0)

    def __contains__(self, x):
        return self.C.get(x, 0) > 0

    def __len__(self):
        return self._size

    def __bool__(self):
        return self._size > 0


class PrioritySumStructure:
    def __init__(self, k):
        if k < 0:
            raise ValueError("k must be nonnegative")
        self.k = k
        self.low = _PriorityHeap()
        self.high = _PriorityHeap()
        self.total = 0

    def __len__(self):
        return len(self.low) + len(self.high)

    def _balance(self):
        target = min(self.k, len(self))
        while len(self.low) > target:
            value = -self.low.pop()
            self.total -= value
            self.high.push(value)
        while len(self.low) < target:
            value = self.high.pop()
            self.total += value
            self.low.push(-value)

    def add(self, value):
        if self.low and value <= -self.low.top():
            self.low.push(-value)
            self.total += value
        else:
            self.high.push(value)
        self._balance()

    def discard(self, value):
        if self.low.erase(-value):
            self.total -= value
        elif not self.high.erase(value):
            return False
        self._balance()
        return True

    def set_k(self, k):
        if k < 0:
            raise ValueError("k must be nonnegative")
        self.k = k
        self._balance()

    def query(self):
        return self.total
