"""キー付き最大値取得・削除。出典: _GetMax_and_Delete.py。
同じキーの更新・削除後の再追加に対応。set/discard/top/popは償却O(log n)。
PyPy向け。値は数値、キーはhashable。キー同士の比較は不要。
"""

from heapq import heappush, heappop, heapify


class MaxQueue:
    def __init__(self):
        self.heap = []
        self.current = {}
        self.serial = 0

    def __len__(self):
        return len(self.current)

    def set(self, key, value):
        self.serial += 1
        self.current[key] = (value, self.serial)
        heappush(self.heap, (-value, self.serial, key))
        self._compact()

    def discard(self, key):
        if key not in self.current:
            return False
        del self.current[key]
        self._compact()
        return True

    def _compact(self):
        if len(self.heap) > max(64, 2 * len(self.current)):
            self.heap = [
                (-value, serial, key) for key, (value, serial) in self.current.items()
            ]
            heapify(self.heap)

    def top(self):
        """(キー,値)。空ならIndexError。"""
        while self.heap:
            negative, serial, key = self.heap[0]
            if self.current.get(key) == (-negative, serial):
                return key, -negative
            heappop(self.heap)
        raise IndexError("empty queue")

    def pop(self):
        key, value = self.top()
        heappop(self.heap)
        del self.current[key]
        return key, value
