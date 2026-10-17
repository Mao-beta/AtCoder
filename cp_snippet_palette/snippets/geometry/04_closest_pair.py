"""単独提出用：Point と最近点対O(N log N)"""
from fractions import Fraction
from math import atan2, cos, gcd, hypot, sin, sqrt

def _divide(a, b):
    """int/Fraction 同士は厳密な Fraction、float を含むなら通常の除算。"""
    if isinstance(a, float) or isinstance(b, float):
        return a / b
    return Fraction(a, b)


class Point:
    """2次元の点・ベクトル。int/Fraction は厳密、float は近似演算。"""

    __slots__ = ('x', 'y')

    def __init__(self, x, y):
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
        """(x, y) のタプルを返す。"""
        return self.x, self.y

    def as_fraction(self):
        """(Fraction(x), Fraction(y)) を返す。float は二進浮動小数点を有理数化。"""
        return Fraction(self.x), Fraction(self.y)

    def dot(self, other):
        """内積 x1*x2 + y1*y2。厳密。O(1)。"""
        return self.x * other.x + self.y * other.y

    def cross(self, other):
        """外積 x1*y2 - y1*x2。反時計回りで正。厳密。O(1)。"""
        return self.x * other.y - self.y * other.x

    def norm_sq(self):
        """原点からのユークリッド距離の二乗。平方根を取らず厳密。"""
        return self.x * self.x + self.y * self.y

    def norm(self):
        """原点からのユークリッド距離。float。"""
        return hypot(self.x, self.y)

    def dist_sq(self, other):
        """他の点との距離の二乗。厳密。"""
        return distance_sq(self, other)

    def dist(self, other):
        """他の点との距離。float。"""
        return distance(self, other)

    def manhattan(self, other):
        """他の点とのマンハッタン距離。厳密。"""
        return abs(self.x - other.x) + abs(self.y - other.y)

    def rotate90(self):
        """原点まわりに反時計回り90度。厳密。"""
        return Point(-self.y, self.x)

    def rotate180(self):
        """原点まわりに180度。厳密。"""
        return -self

    def rotate270(self):
        """原点まわりに反時計回り270度。厳密。"""
        return Point(self.y, -self.x)

    def rotate(self, theta):
        """原点まわりに theta [rad] 回転。三角関数を使うためfloat。"""
        c, s = cos(theta), sin(theta)
        return Point(self.x * c - self.y * s, self.x * s + self.y * c)

    def angle(self):
        """ベクトルの偏角 atan2(y, x) [rad]。float。"""
        return atan2(self.y, self.x)

    def angle_to(self, other):
        """self から other への符号付き角度 [-pi, pi] [rad]。float。"""
        return atan2(self.cross(other), self.dot(other))


def cross3(a, b, c):
    """ベクトル AB と AC の外積。反時計回りで正。厳密。"""
    return (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x)


def orientation(p, q, r, eps=0):
    """p->q->r の向き。反時計回り +1、時計回り -1、一直線 0。

    int/Fraction では eps=0（デフォルト）で完全に厳密。
    float の許容誤差が必要な場合だけ eps を正に指定する。
    eps は外積値に対する絶対誤差であり座標スケールに依存する。
    """
    c = cross3(p, q, r)
    return (c > eps) - (c < -eps)


def on_segment(p, q, r, eps=0):
    """点 q が閉線分 [p, r] 上か。共線性も確認する（退化線分も可）。

    元の実装と引数順序 p, q, r を維持。int/Fraction は厳密判定。
    """
    return (orientation(p, r, q, eps) == 0
            and min(p.x, r.x) - eps <= q.x <= max(p.x, r.x) + eps
            and min(p.y, r.y) - eps <= q.y <= max(p.y, r.y) + eps)


def distance_sq(p, q):
    """二点間のユークリッド距離の二乗。int/Fraction なら厳密。"""
    dx, dy = p.x - q.x, p.y - q.y
    return dx * dx + dy * dy


def distance(p, q):
    """二点間のユークリッド距離。float。"""
    return hypot(p.x - q.x, p.y - q.y)


def manhattan_distance(p, q):
    """二点間のマンハッタン距離。int/Fraction なら厳密。"""
    return abs(p.x - q.x) + abs(p.y - q.y)


def closest_pair_sq(points):
    """点集合の最近点対の距離の二乗。厳密、分割統治 O(N log N)。

    N<2 の場合は None。重複点があれば0。浮動小数点の平方根を使わない。
    """
    ps = sorted(points)
    n = len(ps)
    if n < 2:
        return None
    for i in range(1, n):
        if ps[i] == ps[i - 1]:
            return 0

    def rec(arr):
        m = len(arr)
        if m <= 3:
            d = None
            for i in range(m):
                for j in range(i + 1, m):
                    z = distance_sq(arr[i], arr[j])
                    d = z if d is None or z < d else d
            return d, sorted(arr, key=lambda p: (p.y, p.x))

        mid = m >> 1
        split_x = arr[mid].x
        d1, left = rec(arr[:mid])
        d2, right = rec(arr[mid:])
        if d1 is None:
            best = d2
        elif d2 is None:
            best = d1
        else:
            best = min(d1, d2)

        # x分割した左右のy順配列をマージ（各層合計 O(N)）
        merged = []
        i = j = 0
        while i < len(left) and j < len(right):
            if (left[i].y, left[i].x) <= (right[j].y, right[j].x):
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        merged.extend(left[i:])
        merged.extend(right[j:])

        strip = []
        for p in merged:
            if (p.x - split_x) ** 2 >= best:
                continue
            # y方向の差も距離の下限。strip はy座標順。
            k = len(strip) - 1
            while k >= 0 and (p.y - strip[k].y) ** 2 < best:
                best = min(best, distance_sq(p, strip[k]))
                k -= 1
            strip.append(p)
        return best, merged

    return rec(ps)[0]


