"""等差数列による区間加算/代入・区間和。出典: ABC371Fの未完成実装を修正。
0-indexed・[l,r)。add(l,r,first,step)でa[i]+=first+(i-l)*step。
assignは同じ式で代入。各操作O(log n)、再帰深さO(log n)。PyPy向け。
Codonでは係数×添字和などの中間積も64bit以内にする。

使い方（このファイルを解答の先頭に貼り付けてから実行）
    seg = ArithmeticSegmentTree([0] * 5)
    seg.add(1, 4, first=2, step=3)  # [0,2,5,8,0]
    seg.sum(0, 5)  # => 15
    seg.assign(2, 4, first=10, step=-1)  # [0,2,10,9,0]
    seg.sum(0, 5)  # => 21
"""


class ArithmeticSegmentTree:
    """初期数列valuesに対する等差数列の区間加算・代入と区間和。
    0-indexed、[l,r)。構築O(n)、各操作O(log n)。元のvaluesは変更しない。
    入力: valuesは初期整数列、N=len(values)。構築O(N)時間・空間。0<=l<=r<=Nは整数境界。firstは区間左端の値/加算量、stepは公差でともに整数。
    """
    def __init__(self, values):
        """入力: valuesは初期整数列、N=len(values)。構築O(N)時間・空間。0<=l<=r<=Nは整数境界。firstは区間左端の値/加算量、stepは公差でともに整数。
        """
        self.n = len(values)
        self.size = 1 << max(0, (self.n - 1).bit_length())
        self.data = [0] * (2 * self.size)
        self.has_set = [False] * (2 * self.size)
        self.slope = [0] * (2 * self.size)
        self.intercept = [0] * (2 * self.size)
        self.data[self.size : self.size + self.n] = values
        for i in range(self.size - 1, 0, -1):
            self.data[i] = self.data[2 * i] + self.data[2 * i + 1]

    def _apply(self, k, left, right, slope, intercept, assign):
        length = right - left
        value = slope * ((left + right - 1) * length // 2) + intercept * length
        if assign:
            self.data[k] = value
            self.has_set[k] = True
            self.slope[k], self.intercept[k] = slope, intercept
        else:
            self.data[k] += value
            self.slope[k] += slope
            self.intercept[k] += intercept

    def _push(self, k, left, right):
        if right - left <= 1:
            return
        if self.has_set[k] or self.slope[k] or self.intercept[k]:
            mid = (left + right) // 2
            self._apply(
                2 * k, left, mid, self.slope[k], self.intercept[k], self.has_set[k]
            )
            self._apply(
                2 * k + 1, mid, right, self.slope[k], self.intercept[k], self.has_set[k]
            )
            self.has_set[k] = False
            self.slope[k] = self.intercept[k] = 0

    def _update(self, l, r, slope, intercept, assign, k, left, right):
        if r <= left or right <= l:
            return
        if l <= left and right <= r:
            self._apply(k, left, right, slope, intercept, assign)
            return
        self._push(k, left, right)
        mid = (left + right) // 2
        self._update(l, r, slope, intercept, assign, 2 * k, left, mid)
        self._update(l, r, slope, intercept, assign, 2 * k + 1, mid, right)
        self.data[k] = self.data[2 * k] + self.data[2 * k + 1]

    def _check(self, l, r):
        if not 0 <= l <= r <= self.n:
            raise IndexError("invalid range")

    def add(self, l, r, first, step=0):
        """[l,r)の各A[i]にfirst+(i-l)*stepを加える。firstは位置lの加算量。
        step=0で通常の区間加算。戻り値なし。
        時間O(log(N+1))、探索の追加空間O(log(N+1))以内。
        """
        self._check(l, r)
        self._update(l, r, step, first - l * step, False, 1, 0, self.size)

    def assign(self, l, r, first, step=0):
        """[l,r)の各A[i]をfirst+(i-l)*stepへ置換する。firstは位置lの値。
        step=0で区間代入。戻り値なし。
        時間O(log(N+1))、探索の追加空間O(log(N+1))以内。
        """
        self._check(l, r)
        self._update(l, r, step, first - l * step, True, 1, 0, self.size)

    def _sum(self, l, r, k, left, right):
        if r <= left or right <= l:
            return 0
        if l <= left and right <= r:
            return self.data[k]
        self._push(k, left, right)
        mid = (left + right) // 2
        return self._sum(l, r, 2 * k, left, mid) + self._sum(
            l, r, 2 * k + 1, mid, right
        )

    def sum(self, l, r):
        """[l,r)の現在の和を返す。空区間は0。0<=l<=r<=n。
        時間O(log(N+1))、探索の追加空間O(log(N+1))以内。
        """
        self._check(l, r)
        return self._sum(l, r, 1, 0, self.size)
