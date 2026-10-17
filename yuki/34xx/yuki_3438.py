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


"""
Geometry Library for Competitive Programming (Exact Arithmetic Version)
------------------------------------------------------------------------

このモジュールは、2D 平面上の幾何計算を行うための多機能ライブラリです。
できる限り整数演算および Fraction を用いて正確な計算を行います。
結果は四捨五入せず、可能な限り正確な値（整数または Fraction）を返します。

提供機能:
  - Point クラス: 点・ベクトルの基本演算（加算、減算、内積、外積、スカラー倍、回転など）
  - Segment クラス: 線分を表現し、交差判定などの機能を提供
  - Line クラス: 無限直線を表現し、直線同士の交点計算を Fraction で正確に実施
  - Polygon クラス: 多角形の面積、内部判定、凸包の計算（Monotone Chain 法）など
  - その他、距離計算、反射、点の投影などのユーティリティ関数

すべての座標は整数または Fraction を用いて表現され、四捨五入は行いません。
"""

from fractions import Fraction
from typing import List, Tuple, Union, Optional

# 型エイリアス: 座標は整数または Fraction
Coordinate = Union[int, Fraction]
PointType = Tuple[Coordinate, Coordinate]
SegmentType = Tuple[PointType, PointType]
PolygonType = List[PointType]


# =============================================================================
# Point クラス
# =============================================================================

class Point:
    """2次元の点・ベクトルを表すクラス（座標は整数または Fraction）。"""
    __slots__ = ('x', 'y')

    def __init__(self, x: Coordinate, y: Coordinate):
        self.x = x
        self.y = y

    def __add__(self, other: 'Point') -> 'Point':
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other: 'Point') -> 'Point':
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, k: Union[int, Fraction]) -> 'Point':
        """スカラー倍"""
        return Point(self.x * k, self.y * k)

    def __rmul__(self, k: Union[int, Fraction]) -> 'Point':
        return self.__mul__(k)

    def dot(self, other: 'Point') -> Coordinate:
        """内積を返す"""
        return self.x * other.x + self.y * other.y

    def cross(self, other: 'Point') -> Coordinate:
        """
        外積（スカラー値）を返す。
        計算式: self.x * other.y - self.y * other.x
        """
        return self.x * other.y - self.y * other.x

    def norm_sq(self) -> Coordinate:
        """2乗ノルム（長さの2乗）を返す"""
        return self.dot(self)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False

    def __lt__(self, other: 'Point') -> bool:
        # ソート用（x, y の順）
        return (self.x, self.y) < (other.x, other.y)

    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def __repr__(self) -> str:
        return f"Point({self.x}, {self.y})"

    def rotate(self, theta: float) -> 'Point':
        """
        原点を中心に角度 theta（ラジアン）だけ回転させた点を返す。
        この関数は内部で浮動小数点演算を用いるため、結果は近似値となります。
        四捨五入は行いません。
        """
        from math import cos, sin
        return Point(self.x * cos(theta) - self.y * sin(theta),
                     self.x * sin(theta) + self.y * cos(theta))

    def as_fraction(self) -> Tuple[Fraction, Fraction]:
        """座標を Fraction 型で返す"""
        return (Fraction(self.x), Fraction(self.y))


# =============================================================================
# 幾何学的補助関数
# =============================================================================

def orientation(p: Point, q: Point, r: Point) -> int:
    """
    3点 p, q, r の向きを返す。

    戻り値:
      >0: 反時計回り (ccw)
      <0: 時計回り
       0: p, q, r が同一直線上
    """
    diff = (q - p).cross(r - p)
    if diff > 0:
        return 1
    elif diff < 0:
        return -1
    else:
        return 0


def on_segment(p: Point, q: Point, r: Point) -> bool:
    """
    点 q が線分 pr 上にあるかを判定する（p, q, r が同一直線上であることを前提）。
    """
    return (min(p.x, r.x) <= q.x <= max(p.x, r.x) and
            min(p.y, r.y) <= q.y <= max(p.y, r.y))


def distance_sq(p: Point, q: Point) -> Coordinate:
    """点 p と q の間のユークリッド距離の2乗を返す"""
    return (p - q).norm_sq()


def distance(p: Point, q: Point) -> float:
    """点 p と q の間のユークリッド距離を返す"""
    from math import sqrt
    return sqrt(distance_sq(p, q))


# =============================================================================
# Segment クラス
# =============================================================================

class Segment:
    """2点で定義される線分を表すクラス"""
    __slots__ = ('p', 'q')

    def __init__(self, p: Point, q: Point):
        self.p = p
        self.q = q

    def __repr__(self) -> str:
        return f"Segment({self.p}, {self.q})"

    def as_line(self) -> 'Line':
        """この線分が含まれる無限直線を返す"""
        return Line(self.p, self.q)

    def contains(self, r: Point) -> bool:
        """
        点 r が線分上にあるか（端点を含む）を判定する。
        """
        if orientation(self.p, self.q, r) != 0:
            return False
        return on_segment(self.p, r, self.q)

    def intersects(self, other: 'Segment') -> bool:
        """
        自身と他の線分が交わるかを判定する。
        「交わる」とは、端点を含めた共通部分が 1 点以上存在することを意味する。
        """
        p, q = self.p, self.q
        r, s = other.p, other.q
        o1 = orientation(p, q, r)
        o2 = orientation(p, q, s)
        o3 = orientation(r, s, p)
        o4 = orientation(r, s, q)
        # 一般ケース
        if o1 * o2 < 0 and o3 * o4 < 0:
            return True
        # 特殊ケース（3点が同一直線上の場合）
        if o1 == 0 and on_segment(p, r, q):
            return True
        if o2 == 0 and on_segment(p, s, q):
            return True
        if o3 == 0 and on_segment(r, p, s):
            return True
        if o4 == 0 and on_segment(r, q, s):
            return True
        return False


# =============================================================================
# Line クラス
# =============================================================================

class Line:
    """2点で定義される無限直線を表すクラス"""
    __slots__ = ('p', 'q')

    def __init__(self, p: Point, q: Point):
        if p == q:
            raise ValueError("直線は同一の2点からは定義できません")
        self.p = p
        self.q = q

    def __repr__(self) -> str:
        return f"Line({self.p}, {self.q})"

    def intersection(self, other: 'Line') -> Optional[Tuple[Fraction, Fraction]]:
        """
        他の直線との交点を Fraction 型の (x, y) で返す。
        交点が一意に存在しない（平行または重なる）場合は None を返す。
        """
        A1 = self.q.y - self.p.y
        B1 = self.p.x - self.q.x
        C1 = A1 * self.p.x + B1 * self.p.y

        A2 = other.q.y - other.p.y
        B2 = other.p.x - other.q.x
        C2 = A2 * other.p.x + B2 * other.p.y

        det = A1 * B2 - A2 * B1
        if det == 0:
            return None
        x = Fraction(B2 * C1 - B1 * C2, det)
        y = Fraction(A1 * C2 - A2 * C1, det)
        return (x, y)


# =============================================================================
# Polygon クラス
# =============================================================================

class Polygon:
    """多角形を表すクラス。頂点は順序付けられた Point のリスト。"""

    def __init__(self, vertices: List[Point]):
        self.vertices = vertices  # 順序は時計回り or 反時計回りのどちらか

    def __repr__(self) -> str:
        return f"Polygon({self.vertices})"

    def area2(self) -> int:
        """
        符号付き面積の2倍を計算する。
        頂点が反時計回りなら正、時計回りなら負。
        """
        n = len(self.vertices)
        area = 0
        for i in range(n):
            area += self.vertices[i].cross(self.vertices[(i + 1) % n])
        return area

    def area(self) -> Fraction:
        """
        多角形の絶対面積を Fraction 型で返す。
        """
        return abs(self.area2()) / 2

    def contains(self, point: Point) -> bool:
        """
        点が多角形内部または境界上にあるかを判定する（ray-casting 法）。
        """
        n = len(self.vertices)
        inside = False
        x, y = point.x, point.y
        for i in range(n):
            p1 = self.vertices[i]
            p2 = self.vertices[(i + 1) % n]
            # 点が辺上にあるかチェック
            if orientation(p1, p2, point) == 0 and on_segment(p1, point, p2):
                return True
            if (p1.y > y) != (p2.y > y):
                # 交点の x 座標を Fraction で正確に計算
                intersect_x = p1.x + (p2.x - p1.x) * Fraction(y - p1.y, p2.y - p1.y)
                if x < intersect_x:
                    inside = not inside
        return inside

    @staticmethod
    def convex_hull(points: List[Point]) -> 'Polygon':
        """
        点集合の凸包を Monotone Chain アルゴリズムで求める。
        返り値は反時計回りに並んだ凸包の頂点からなる Polygon。
        全ての点が同一直線上の場合、両端の点のみが返る。
        """
        points = sorted(set(points))
        if len(points) <= 1:
            return Polygon(points)
        lower = []
        for p in points:
            while len(lower) >= 2 and orientation(lower[-2], lower[-1], p) <= 0:
                lower.pop()
            lower.append(p)
        upper = []
        for p in reversed(points):
            while len(upper) >= 2 and orientation(upper[-2], upper[-1], p) <= 0:
                upper.pop()
            upper.append(p)
        convex = lower[:-1] + upper[:-1]
        return Polygon(convex)


def main():
    T = NI()
    for _ in range(T):
        N = NI()
        XY = EI(N)
        D = defaultdict(int)
        for i, (x, y) in enumerate(XY):
            D[(x, y)] = i
        ch = Polygon.convex_hull([Point(x, y) for x, y in XY])
        ans = ["No"] * N
        CN = len(ch.vertices)

        if CN > 2:
            for i in range(CN):
                P = ch.vertices[i]
                idx = D[(P.x, P.y)]
                Q, R = ch.vertices[(i-1)%CN], ch.vertices[(i+1)%CN]
                x, y = R.x - Q.x, R.y - Q.y
                ans[idx] = f"{y} {-x}"
            print(*ans, sep="\n")

        else:
            for i in range(CN):
                P = ch.vertices[i]
                idx = D[(P.x, P.y)]
                Q = ch.vertices[(i+1)%CN]
                x, y = P.x - Q.x, P.y - Q.y
                ans[idx] = f"{x} {y}"
            print(*ans, sep="\n")


if __name__ == "__main__":
    main()
