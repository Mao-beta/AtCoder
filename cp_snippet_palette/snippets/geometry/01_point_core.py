"""競技プログラミング用 自己完結スニペット: 01_point_core.py

必要なクラス・関数だけを収録。int/Fractionは厳密計算。

使い方（このファイルを解答の先頭に貼り付けてから実行）
    p, q = Point(0, 0), Point(3, 4)
    q.norm_sq(), distance_sq(p, q), distance(p, q), manhattan_distance(p, q)  # => (25, 25, 5.0, 7)
    cross3(p, Point(1, 0), Point(0, 1)), orientation(p, Point(1, 0), Point(0, 1))  # => (1, 1)
    on_segment(p, Point(1, 1), Point(2, 2))  # 第2引数が判定する点
    # => True

    q.rotate90(), q.dot(Point(1, 2)), q.cross(Point(1, 2))  # => (Point(-4, 3), 11, 2)
入力の共通規約: 点はPoint(x,y)で渡す（座標tupleを直接渡すAPIではない）。座標はint/Fraction/float。
計算量は一回の数値演算をO(1)とし、多倍長整数・Fractionのbit長によるコストは別。
"""

from fractions import Fraction
from math import atan2, cos, gcd, hypot, sin, sqrt

def _divide(a, b):
    """int/Fraction 同士は厳密な Fraction、float を含むなら通常の除算。"""
    if isinstance(a, float) or isinstance(b, float):
        return a / b
    return Fraction(a, b)


class Point:
    """2次元の点・ベクトル。Point(x,y)で作る。座標はint/Fraction/float。
    p.x,p.yまたはtuple(p)で座標を取得。p+q,p-q,k*p,p/kに対応し、*は内積ではない。
    内積はp.dot(q)、外積はp.cross(q)。int/Fractionは厳密、floatは近似。
    set/dictに登録した後に座標を変更しないこと。
    入力: x/yは数値の座標。構築O(1)時間・空間。otherは別のPoint、thetaは回転角の実数（ラジアン）。
    """

    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        """入力: x/yは数値の座標。構築O(1)時間・空間。otherは別のPoint、thetaは回転角の実数（ラジアン）。
        """
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point({self.x}, {self.y})'

    def __iter__(self):
        """x, y = point として取り出せる。"""
        yield self.x
        yield self.y

    def __eq__(self, other):
        return isinstance(other, Point) and self.x == other.x and self.y == other.y

    def __lt__(self, other):
        """(x, y) の辞書順。ソートや凸包で利用する。"""
        return (self.x, self.y) < (other.x, other.y)

    def __hash__(self):
        """hashable。ただし集合・辞書に登録した後は座標を変更しないこと。"""
        return hash((self.x, self.y))

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __neg__(self):
        return Point(-self.x, -self.y)

    def __mul__(self, k):
        """ベクトルのスカラー倍。内積は dot() を使う。"""
        return Point(self.x * k, self.y * k)

    def __rmul__(self, k):
        return self * k

    def __truediv__(self, k):
        """スカラーで割る。整数入力同士でも Fraction を保持する。"""
        return Point(_divide(self.x, k), _divide(self.y, k))

    def as_tuple(self):
        """(x, y) のタプルを返す。
        時間・追加空間O(1)回の数値演算。引数の型はクラスの入力規約に従う。
        """
        return self.x, self.y

    def as_fraction(self):
        """(Fraction(x), Fraction(y)) を返す。float は二進浮動小数点を有理数化。
        時間・追加空間O(1)回の数値演算。引数の型はクラスの入力規約に従う。
        """
        return Fraction(self.x), Fraction(self.y)

    def dot(self, other):
        """内積 x1*x2 + y1*y2。厳密。O(1)。
        時間・追加空間O(1)回の数値演算。引数の型はクラスの入力規約に従う。
        """
        return self.x * other.x + self.y * other.y

    def cross(self, other):
        """外積 x1*y2 - y1*x2。反時計回りで正。厳密。O(1)。
        時間・追加空間O(1)回の数値演算。引数の型はクラスの入力規約に従う。
        """
        return self.x * other.y - self.y * other.x

    def norm_sq(self):
        """原点からのユークリッド距離の二乗。平方根を取らず厳密。
        時間・追加空間O(1)回の数値演算。引数の型はクラスの入力規約に従う。
        """
        return self.x * self.x + self.y * self.y

    def norm(self):
        """原点からのユークリッド距離。float。
        時間・追加空間O(1)回の数値演算。引数の型はクラスの入力規約に従う。
        """
        return hypot(self.x, self.y)

    def dist_sq(self, other):
        """他の点との距離の二乗。厳密。
        時間・追加空間O(1)回の数値演算。引数の型はクラスの入力規約に従う。
        """
        return distance_sq(self, other)

    def dist(self, other):
        """他の点との距離。float。
        時間・追加空間O(1)回の数値演算。引数の型はクラスの入力規約に従う。
        """
        return distance(self, other)

    def manhattan(self, other):
        """他の点とのマンハッタン距離。厳密。
        時間・追加空間O(1)回の数値演算。引数の型はクラスの入力規約に従う。
        """
        return abs(self.x - other.x) + abs(self.y - other.y)

    def rotate90(self):
        """原点まわりに反時計回り90度。厳密。
        時間・追加空間O(1)回の数値演算。引数の型はクラスの入力規約に従う。
        """
        return Point(-self.y, self.x)

    def rotate180(self):
        """原点まわりに180度。厳密。
        時間・追加空間O(1)回の数値演算。引数の型はクラスの入力規約に従う。
        """
        return -self

    def rotate270(self):
        """原点まわりに反時計回り270度。厳密。
        時間・追加空間O(1)回の数値演算。引数の型はクラスの入力規約に従う。
        """
        return Point(self.y, -self.x)

    def rotate(self, theta):
        """原点まわりに theta [rad] 回転。三角関数を使うためfloat。
        時間・追加空間O(1)回の数値演算。引数の型はクラスの入力規約に従う。
        """
        c, s = cos(theta), sin(theta)
        return Point(self.x * c - self.y * s, self.x * s + self.y * c)

    def angle(self):
        """ベクトルの偏角 atan2(y, x) [rad]。float。
        時間・追加空間O(1)回の数値演算。引数の型はクラスの入力規約に従う。
        """
        return atan2(self.y, self.x)

    def angle_to(self, other):
        """self から other への符号付き角度 [-pi, pi] [rad]。float。
        時間・追加空間O(1)回の数値演算。引数の型はクラスの入力規約に従う。
        """
        return atan2(self.cross(other), self.dot(other))


def cross3(a, b, c):
    """ベクトル AB と AC の外積。反時計回りで正。厳密。
    入力: a / b / cはPoint。時間・追加空間O(1)回の数値演算。
    """
    return (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x)


def orientation(p, q, r, eps=0):
    """p->q->r の向き。反時計回り +1、時計回り -1、一直線 0。

    int/Fraction では eps=0（デフォルト）で完全に厳密。
    float の許容誤差が必要な場合だけ eps を正に指定する。
    eps は外積値に対する絶対誤差であり座標スケールに依存する。
    入力: p / q / rはPoint。epsは0以上の数値の許容誤差（0は厳密判定）。時間・追加空間O(1)回の数値演算。
    """
    c = cross3(p, q, r)
    return (c > eps) - (c < -eps)


def on_segment(p, q, r, eps=0):
    """点 q が閉線分 [p, r] 上か。共線性も確認する（退化線分も可）。

    元の実装と引数順序 p, q, r を維持。int/Fraction は厳密判定。
    入力: p / q / rはPoint。epsは0以上の数値の許容誤差（0は厳密判定）。時間・追加空間O(1)回の数値演算。
    """
    return (orientation(p, r, q, eps) == 0
            and min(p.x, r.x) - eps <= q.x <= max(p.x, r.x) + eps
            and min(p.y, r.y) - eps <= q.y <= max(p.y, r.y) + eps)


def distance_sq(p, q):
    """二点間のユークリッド距離の二乗。int/Fraction なら厳密。
    入力: p / qはPoint。時間・追加空間O(1)回の数値演算。
    """
    dx, dy = p.x - q.x, p.y - q.y
    return dx * dx + dy * dy


def distance(p, q):
    """二点間のユークリッド距離。float。
    入力: p / qはPoint。時間・追加空間O(1)回の数値演算。
    """
    return hypot(p.x - q.x, p.y - q.y)


def manhattan_distance(p, q):
    """二点間のマンハッタン距離。int/Fraction なら厳密。
    入力: p / qはPoint。時間・追加空間O(1)回の数値演算。
    """
    return abs(p.x - q.x) + abs(p.y - q.y)


