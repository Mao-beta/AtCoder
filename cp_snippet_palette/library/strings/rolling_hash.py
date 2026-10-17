"""二重Rolling Hashと一点更新版。出典: _Strings.py, ABC331F。
文字列または整数列。0-indexed・半開区間。衝突はゼロにはならない。
PyPy向け。Codonでも乗算が64bit内になる約10^9の法を使う（コンパイル未確認）。
"""


class RollingHash:
    def __init__(self, values, base=911382323):
        if not 1 < base < 1000000007:
            raise ValueError("base out of range")
        self.n = len(values)
        self.base = base
        self.mods = (1000000007, 1000000009)
        self.hashes, self.powers = [], []
        for mod in self.mods:
            h, p = [0], [1]
            for x in values:
                value = ord(x) if isinstance(x, str) else x
                h.append((h[-1] * base + value % mod) % mod)
                p.append(p[-1] * base % mod)
            self.hashes.append(h)
            self.powers.append(p)

    def query(self, left, right):
        if not 0 <= left <= right <= self.n:
            raise IndexError("invalid range")
        result = []
        for h, p, mod in zip(self.hashes, self.powers, self.mods):
            result.append((h[right] - h[left] * p[right - left]) % mod)
        return tuple(result)


class RollingHashSegTree:
    def __init__(self, values, base=911382323):
        if not 1 < base < 1000000007:
            raise ValueError("base out of range")
        self.n = len(values)
        self.size = 1 << max(0, (self.n - 1).bit_length())
        self.mods = (1000000007, 1000000009)
        self.powers = [[1] for _ in self.mods]
        for p, mod in zip(self.powers, self.mods):
            for _ in range(self.n):
                p.append(p[-1] * base % mod)
        self.data = [(0, 0, 0)] * (2 * self.size)
        for i, x in enumerate(values):
            value = ord(x) if isinstance(x, str) else x
            self.data[self.size + i] = (value % self.mods[0], value % self.mods[1], 1)
        for i in range(self.size - 1, 0, -1):
            self.data[i] = self._merge(self.data[2 * i], self.data[2 * i + 1])

    def _merge(self, a, b):
        return (
            (a[0] * self.powers[0][b[2]] + b[0]) % self.mods[0],
            (a[1] * self.powers[1][b[2]] + b[1]) % self.mods[1],
            a[2] + b[2],
        )

    def set(self, index, value):
        if not 0 <= index < self.n:
            raise IndexError(index)
        if isinstance(value, str):
            value = ord(value)
        i = index + self.size
        self.data[i] = (value % self.mods[0], value % self.mods[1], 1)
        i >>= 1
        while i:
            self.data[i] = self._merge(self.data[2 * i], self.data[2 * i + 1])
            i >>= 1

    def query(self, left, right):
        if not 0 <= left <= right <= self.n:
            raise IndexError("invalid range")
        left += self.size
        right += self.size
        a = b = (0, 0, 0)
        while left < right:
            if left & 1:
                a = self._merge(a, self.data[left])
                left += 1
            if right & 1:
                right -= 1
                b = self._merge(self.data[right], b)
            left >>= 1
            right >>= 1
        result = self._merge(a, b)
        return result[0], result[1]
