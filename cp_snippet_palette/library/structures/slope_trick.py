"""区分線形凸関数のSlope Trick。出典: ABC127F, ABC365F。
f(x)=0から開始。絶対値追加・片側最小化・区間シフトを提供。
ヒープ操作O(log n)、シフトO(1)。PyPy向け。Codonは64bit内の整数に限定。
"""

from heapq import heappush, heappop


class SlopeTrick:
    def __init__(self):
        self.left, self.right = [], []
        self.offset_left = self.offset_right = 0
        self.minimum = 0

    def add_constant(self, value):
        self.minimum += value

    def add_a_minus_x(self, a):
        """max(a-x,0)を加える。"""
        if self.right:
            r = self.right[0] + self.offset_right
            self.minimum += max(0, a - r)
        heappush(self.right, a - self.offset_right)
        value = heappop(self.right) + self.offset_right
        heappush(self.left, -value + self.offset_left)

    def add_x_minus_a(self, a):
        """max(x-a,0)を加える。"""
        if self.left:
            l = -self.left[0] + self.offset_left
            self.minimum += max(0, l - a)
        heappush(self.left, -a + self.offset_left)
        value = -heappop(self.left) + self.offset_left
        heappush(self.right, value - self.offset_right)

    def add_abs(self, a):
        self.add_a_minus_x(a)
        self.add_x_minus_a(a)

    def shift(self, left, right):
        """f(x)←min(f(y): x-right<=y<=x-left)。left<=right。"""
        if left > right:
            raise ValueError("left must be <= right")
        self.offset_left += left
        self.offset_right += right

    def prefix_min(self):
        """f(x)←min_{y<=x} f(y)。"""
        self.right.clear()

    def suffix_min(self):
        """f(x)←min_{y>=x} f(y)。"""
        self.left.clear()

    def argmin(self):
        """最小値をとる閉区間。無限端はNone。"""
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
