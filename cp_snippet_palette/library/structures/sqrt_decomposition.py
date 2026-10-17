"""区間加算・区間和の平方分割。出典: PAST003N/PAST014Oのバケット方式を汎用化。
0-indexed・半開区間。O(sqrt n)/操作。PyPy向け、Codonは64bit整数内。
"""

from math import isqrt


class SqrtDecomposition:
    def __init__(self, values):
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
