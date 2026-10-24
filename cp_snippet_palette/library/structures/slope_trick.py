"""区分線形凸関数のSlope Trick。出典: ABC127F, ABC365F。
f(x)=0から開始。絶対値追加・片側最小化・区間シフトを提供。

ヒープ操作O(log n)、シフトO(1)。PyPy向け。Codonは64bit内の整数に限定。

使い方（このファイルを解答の先頭に貼り付けてから実行）
    f = SlopeTrick()
    f.add_abs(2); f.add_abs(5)
    f.minimum, f.argmin(), f.evaluate(0)  # => (3, (2, 5), 7)
    f.shift(1, 1)  # f(x) <- f(x-1)
    f.argmin()  # => (3, 6)
"""

from heapq import heappush, heappop


class SlopeTrick:
    """f(x)=0から始まる区分線形凸関数を保持する。
    add_abs等で関数を更新し、minimum属性で最小値、argmin()で最小点の範囲を取得。
    ヒープ操作O(log n)、shiftはO(1)。関数全体の値が必要な少数クエリにはevaluate。
    引数なしでf(x)=0をO(1)時間・空間で構築する。a/x/value/left/rightは数値。nは保持する折れ点の個数、空間O(n)。
    """
    def __init__(self):
        """引数なしでf(x)=0をO(1)時間・空間で構築する。a/x/value/left/rightは数値。nは保持する折れ点の個数、空間O(n)。
        """
        self.left, self.right = [], []
        self.offset_left = self.offset_right = 0
        self.minimum = 0

    def add_constant(self, value):
        """全xについてf(x)にvalueを加える。最小値もvalue増える。O(1)。
        """
        self.minimum += value

    def add_a_minus_x(self, a):
        """max(a-x,0)を加える。
        時間O(log(n+1))、追加する折れ点はO(1)個。aは折れ曲がるx座標。
        """
        if self.right:
            r = self.right[0] + self.offset_right
            self.minimum += max(0, a - r)
        heappush(self.right, a - self.offset_right)
        value = heappop(self.right) + self.offset_right
        heappush(self.left, -value + self.offset_left)

    def add_x_minus_a(self, a):
        """max(x-a,0)を加える。
        時間O(log(n+1))、追加する折れ点はO(1)個。aは折れ曲がるx座標。
        """
        if self.left:
            l = -self.left[0] + self.offset_left
            self.minimum += max(0, l - a)
        heappush(self.left, -a + self.offset_left)
        value = -heappop(self.left) + self.offset_left
        heappush(self.right, value - self.offset_right)

    def add_abs(self, a):
        """f(x)にabs(x-a)を加える。戻り値なし。O(log n)。
        """
        self.add_a_minus_x(a)
        self.add_x_minus_a(a)

    def shift(self, left, right):
        """f(x)←min(f(y): x-right<=y<=x-left)。left<=right。
        left/rightは移動量の数値でleft<=right。時間・追加空間O(1)。
        """
        if left > right:
            raise ValueError("left must be <= right")
        self.offset_left += left
        self.offset_right += right

    def prefix_min(self):
        """f(x)←min_{y<=x} f(y)。
        引数なし。ヒープの参照解放を含め最悪O(n)時間、追加空間O(1)。
        """
        self.right.clear()

    def suffix_min(self):
        """f(x)←min_{y>=x} f(y)。
        引数なし。ヒープの参照解放を含め最悪O(n)時間、追加空間O(1)。
        """
        self.left.clear()

    def argmin(self):
        """最小値をとる閉区間。無限端はNone。
        引数なし。時間・追加空間O(1)。
        """
        l = -self.left[0] + self.offset_left if self.left else None
        r = self.right[0] + self.offset_right if self.right else None
        return l, r

    def evaluate(self, x):
        """O(n)で値を計算。検証・少数の評価用。"""
        return (
            self.minimum
            + sum(max(0, -v + self.offset_left - x) for v in self.left)
            + sum(max(0, x - v - self.offset_right) for v in self.right)
        )
