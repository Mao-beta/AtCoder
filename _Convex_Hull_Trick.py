import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.set_int_max_str_digits(10 ** 6)
sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
MOD99 = 998244353

input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()
SMI = lambda: input().split()
SLI = lambda: list(SMI())
EI = lambda m: [NLI() for _ in range(m)]

from fractions import Fraction
from typing import Optional, Union


class LineCHT:
    """
    直線 y = m*x + b を表すクラス（すべて整数）。
    """
    __slots__ = ('m', 'b')

    def __init__(self, m: int, b: int):
        self.m = m
        self.b = b

    def evaluate(self, x: int) -> int:
        """
        指定した x における y = m*x + b の値を返す。
        """
        return self.m * x + self.b

    def __repr__(self):
        return f"LineCHT(m={self.m}, b={self.b})"


class ConvexHullTrick:
    """
    LiChao Tree を用いた Convex Hull Trick の実装（整数版）。

    このデータ構造は、直線（LineCHT 型）の動的追加と、
    任意の x における最適（最大または最小）な y の値のクエリに O(log(domain))
    で応答します。

    コンストラクタの引数:
      - x_left, x_right: クエリを行う x の定義域（両端含む、整数）。
      - is_min: True の場合は「最小値クエリ」、False の場合は「最大値クエリ」になります。

    ※ ここでは、すべての計算を整数演算で行い、結果は整数となる前提です。
    """

    class Node:
        """
        LiChao Tree の各ノードを表す内部クラス。
        各ノードは [lo, hi] の区間と、その区間上で現状最適と考えられる直線を保持します。
        """
        __slots__ = ('lo', 'hi', 'mid', 'line', 'left', 'right', 'is_min')

        def __init__(self, lo: int, hi: int, is_min: bool):
            self.lo = lo
            self.hi = hi
            # ここでは整数ドメインなので mid は整数の切り捨て値
            self.mid = (lo + hi) // 2
            self.line: LineCHT = None
            self.left: 'ConvexHullTrick.Node' = None
            self.right: 'ConvexHullTrick.Node' = None
            self.is_min = is_min

        def __repr__(self):
            return f"Node([{self.lo}, {self.hi}], line={self.line})"

    def __init__(self, x_left: int, x_right: int, is_min: bool = False):
        self.x_left = x_left
        self.x_right = x_right
        self.is_min = is_min
        self.root = self.Node(x_left, x_right, is_min)

    def _better(self, line1: LineCHT, line2: LineCHT, x: int, is_min: bool) -> bool:
        """
        x において、line1 の評価値が line2 の評価値より「良い」
        （最小クエリなら小さい、最大クエリなら大きい）かどうかを返す。
        """
        val1 = line1.evaluate(x)
        val2 = line2.evaluate(x)
        return val1 < val2 if is_min else val1 > val2

    def _better_val(self, val1: int, val2: int) -> bool:
        """
        クエリタイプに応じた値の比較。
        """
        return val1 < val2 if self.is_min else val1 > val2

    def _default_value(self) -> int:
        """
        クエリ対象に直線が登録されていない場合の初期値を返す。
        最小クエリの場合は +INF、最大クエリの場合は -INF とします。
        """
        INF = 1 << 62
        return INF if self.is_min else -INF

    def _add_line(self, node: 'ConvexHullTrick.Node', new_line: LineCHT):
        """
        再帰的に LiChao Tree を更新し、new_line を追加する。
        """
        lo, hi, mid = node.lo, node.hi, node.mid
        if node.line is None:
            node.line = new_line
            return

        # 中央点 mid で new_line の方が良ければ入れ替える
        if self._better(new_line, node.line, mid, node.is_min):
            node.line, new_line = new_line, node.line

        if lo == hi:
            return  # 範囲が 1 点の場合

        # 左端または右端で new_line がより良ければ、子ノードに再帰する
        if self._better(new_line, node.line, lo, node.is_min):
            if node.left is None:
                node.left = self.Node(lo, mid, node.is_min)
            self._add_line(node.left, new_line)
        elif self._better(new_line, node.line, hi, node.is_min):
            if node.right is None:
                # 右子ノードの定義域は [mid+1, hi] とします
                node.right = self.Node(mid + 1, hi, node.is_min)
            self._add_line(node.right, new_line)

    def add_line(self, m: int, b: int):
        """
        直線 y = m*x + b を追加する。
        """
        new_line = LineCHT(m, b)
        self._add_line(self.root, new_line)

    def _query(self, node: 'ConvexHullTrick.Node', x: int) -> int:
        if node is None:
            return self._default_value()
        res = node.line.evaluate(x) if node.line is not None else self._default_value()
        if x <= node.mid:
            candidate = self._query(node.left, x)
            if self._better_val(candidate, res):
                res = candidate
        else:
            candidate = self._query(node.right, x)
            if self._better_val(candidate, res):
                res = candidate
        return res

    def query(self, x: int) -> int:
        """
        指定した x において、追加された直線群の中から最適（最小または最大）の y の値を返す。
        """
        return self._query(self.root, x)

    def __repr__(self) -> str:
        return f"ConvexHullTrick(domain=[{self.x_left}, {self.x_right}], is_min={self.is_min})"


# =============================================================================
# Example Usage & Test Cases
# =============================================================================

if __name__ == '__main__':
    # # === 最大値クエリの例 ===
    # print("=== Maximum Query Example ===")
    # # 定義域 [0, 100] で、最大値を求める場合
    # cht_max = ConvexHullTrick(0, 100, is_min=False)
    # # 以下の直線を追加する（すべて y = m*x + b の形）
    # cht_max.add_line(2, 3)  # y = 2x + 3
    # cht_max.add_line(1, 5)  # y = x + 5
    # cht_max.add_line(3, 1)  # y = 3x + 1
    # for x in [0, 10, 50, 100]:
    #     print(f"Query x = {x}: {cht_max.query(x)}")
    #
    # # === 最小値クエリの例 ===
    # print("=== Minimum Query Example ===")
    # # 定義域 [0, 100] で、最小値を求める場合
    # cht_min = ConvexHullTrick(0, 100, is_min=True)
    # cht_min.add_line(2, 3)  # y = 2x + 3
    # cht_min.add_line(1, 5)  # y = x + 5
    # cht_min.add_line(3, 1)  # y = 3x + 1
    # for x in [0, 10, 50, 100]:
    #     print(f"Query x = {x}: {cht_min.query(x)}")

    # ABC289G
    N, M = NMI()
    B = sorted(NLI(), reverse=True)
    C = NLI()
    C = [(c, i) for i, c in enumerate(C)]

    # i人が商品jを購入するときの値段は i(Bi + Cj)
    # 求める答えは各x(∈ C)で iを動かしたときの i(Bi + x) の最大値
    CHT = ConvexHullTrick(-10**10, 10**10, is_min=False)
    for i, b in enumerate(B, start=1):
        CHT.add_line(i, i * b)

    ans = [0] * M
    for c, i in C:
        m = CHT.query(c)
        ans[i] = m

    print(*ans)

