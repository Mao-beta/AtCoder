"""二重Rolling Hashと一点更新版。出典: _Strings.py, ABC331F。

文字列または整数列。0-indexed・半開区間。衝突はゼロにはならない。
PyPy向け。Codonでも乗算が64bit内になる約10^9の法を使う（コンパイル未確認）。

使い方（このファイルを解答の先頭に貼り付けてから実行）
    rh = RollingHash('abcabc')
    rh.query(0, 3) == rh.query(3, 6)  # => True
    dynamic = RollingHashSegTree('abc')
    dynamic.set(1, 'x')
    dynamic.query(0, 3) == RollingHash('axc').query(0, 3)  # => True
"""


class RollingHash:
    """文字列または整数列valuesの静的な二重Rolling Hash。構築O(n)、queryはO(1)。
    異なるオブジェクト間ではbaseを揃える。比較時は長さも一致することを確認する。
    ハッシュ一致は確率的な判定で、衝突の可能性がある。
    入力: valuesはstrまたは整数列、baseはハッシュの基数の整数。n/N=len(values)。構築O(N)時間・空間。
    問い合わせは0<=left<=right<=Nの半開区間、更新添字は0-indexed。
    """
    def __init__(self, values, base=911382323):
        """入力: valuesはstrまたは整数列、baseはハッシュの基数の整数。n/N=len(values)。構築O(N)時間・空間。
        問い合わせは0<=left<=right<=Nの半開区間、更新添字は0-indexed。
        """
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
        """[left,right)のハッシュを2つの整数のtupleで返す。空区間は(0,0)。
        位置には依存しないため、同じbaseで同じ長さの部分列同士を比較できる。
        left/rightは整数の半開区間境界。時間・追加空間O(1)。
        """
        if not 0 <= left <= right <= self.n:
            raise IndexError("invalid range")
        result = []
        for h, p, mod in zip(self.hashes, self.powers, self.mods):
            result.append((h[right] - h[left] * p[right - left]) % mod)
        return tuple(result)


class RollingHashSegTree:
    """文字列または整数列valuesへの一点更新付き二重Rolling Hash。
    構築O(n)、set/queryはO(log n)。baseを揃えればRollingHashとも比較可能。
    比較時は部分列の長さも確認する。衝突の可能性は残る。
    入力: valuesはstrまたは整数列、baseはハッシュの基数の整数。n/N=len(values)。構築O(N)時間・空間。
    問い合わせは0<=left<=right<=Nの半開区間、更新添字は0-indexed。
    """
    def __init__(self, values, base=911382323):
        """入力: valuesはstrまたは整数列、baseはハッシュの基数の整数。n/N=len(values)。構築O(N)時間・空間。
        問い合わせは0<=left<=right<=Nの半開区間、更新添字は0-indexed。
        """
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
        """0-indexedの位置indexをvalue（1文字または整数）に変更する。戻り値なし。
        valueは1文字のstrまたは整数。indexは0..N-1。時間O(log(N+1))、追加空間O(1)。
        """
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
        """[left,right)の二重ハッシュtuple。空区間は(0,0)。O(log n)。
        """
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
