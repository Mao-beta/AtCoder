"""疎なFenwick Tree。出典: ABC324G。0-indexed・半開区間。
1D:O(log n)、2D:O(log h log w)。2Dも必要な辞書要素だけ確保する。
PyPy向け。Codonでは座標・累積値を64bit以内にする。
"""


class DynamicFenwickTree:
    def __init__(self, n):
        if n < 0:
            raise ValueError("negative size")
        self.n = n
        self.data = {}

    def add(self, index, value):
        if not 0 <= index < self.n:
            raise IndexError(index)
        i = index + 1
        while i <= self.n:
            self.data[i] = self.data.get(i, 0) + value
            i += i & -i

    def prefix_sum(self, right):
        if not 0 <= right <= self.n:
            raise IndexError(right)
        result = 0
        while right:
            result += self.data.get(right, 0)
            right -= right & -right
        return result

    def sum(self, left, right):
        if not 0 <= left <= right <= self.n:
            raise IndexError("invalid range")
        return self.prefix_sum(right) - self.prefix_sum(left)

    def lower_bound(self, target):
        """全要素非負を前提に、prefix_sum(i+1)>=targetとなる最小i。なければn。"""
        if target <= 0:
            return 0
        index = 0
        bit = 1 << max(0, self.n.bit_length() - 1)
        while bit:
            nxt = index + bit
            if nxt <= self.n and self.data.get(nxt, 0) < target:
                target -= self.data.get(nxt, 0)
                index = nxt
            bit >>= 1
        return index


class DynamicFenwickTree2D:
    def __init__(self, height, width):
        if height < 0 or width < 0:
            raise ValueError("negative size")
        self.height, self.width = height, width
        self.data = {}

    def add(self, row, col, value):
        if not (0 <= row < self.height and 0 <= col < self.width):
            raise IndexError("invalid position")
        i = row + 1
        while i <= self.height:
            j = col + 1
            while j <= self.width:
                self.data[i, j] = self.data.get((i, j), 0) + value
                j += j & -j
            i += i & -i

    def prefix_sum(self, bottom, right):
        if not (0 <= bottom <= self.height and 0 <= right <= self.width):
            raise IndexError("invalid prefix")
        result = 0
        i = bottom
        while i:
            j = right
            while j:
                result += self.data.get((i, j), 0)
                j -= j & -j
            i -= i & -i
        return result

    def sum(self, top, left, bottom, right):
        if not (0 <= top <= bottom <= self.height and 0 <= left <= right <= self.width):
            raise IndexError("invalid rectangle")
        return (
            self.prefix_sum(bottom, right)
            - self.prefix_sum(top, right)
            - self.prefix_sum(bottom, left)
            + self.prefix_sum(top, left)
        )
