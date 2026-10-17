"""競技プログラミング用 自己完結スニペット: 05_circle.py
必要なクラス・関数だけを収録。int/Fractionは厳密計算。
"""

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


def project_point(line, p):
    """無限直線 line への垂線の足。int/Fraction 入力なら厳密な Point。"""
    v = line.q - line.p
    t = _divide((p - line.p).dot(v), v.norm_sq())
    return line.p + v * t


def reflect_point(line, p):
    """無限直線 line に関する点 p の鏡映。int/Fraction 入力なら厳密。"""
    return 2 * project_point(line, p) - p


def _line_intersection_point(a, b, c, d):
    """非平行な無限直線 ab, cd の交点。呼び出し側で非平行を確認。"""
    u, v = b - a, d - c
    t = _divide((c - a).cross(v), u.cross(v))
    return a + u * t


class Line:
    """異なる2点から定義する無限直線。"""

    __slots__ = ('p', 'q')

    def __init__(self, p, q):
        if p == q:
            raise ValueError('直線は異なる2点から定義してください')
        self.p, self.q = p, q

    def __repr__(self):
        return f'Line({self.p}, {self.q})'

    def direction(self):
        """方向ベクトル q - p。"""
        return self.q - self.p

    def abc(self, normalize=False):
        """ax + by + c = 0 の係数 (a,b,c)。整数座標なら整数。O(1)。

        normalize=True は整数座標専用。係数を最大公約数で割り、
        最初の非零係数が正になるよう符号も統一する。
        同じ無限直線の識別・重複除去に使える。
        """
        a, b = self.p.y - self.q.y, self.q.x - self.p.x
        c = -a * self.p.x - b * self.p.y
        if not normalize:
            return a, b, c
        if not all(isinstance(v, int) for v in (a, b, c)):
            raise TypeError('normalize=True は整数座標にのみ対応します')
        z = gcd(gcd(abs(a), abs(b)), abs(c))
        a, b, c = a // z, b // z, c // z
        if a < 0 or (a == 0 and b < 0):
            a, b, c = -a, -b, -c
        return a, b, c

    def contains(self, point):
        """点が無限直線上にあるか。int/Fraction なら厳密。"""
        return cross3(self.p, self.q, point) == 0

    def side(self, point):
        """直線の p→q から見た左右。左 +1、右 -1、直線上 0。"""
        return orientation(self.p, self.q, point)

    def parallel(self, other):
        """2本の直線が平行か。重なっている場合も True。"""
        return self.direction().cross(other.direction()) == 0

    def coincident(self, other):
        """2本の直線が同一か。"""
        return self.parallel(other) and self.contains(other.p)

    def intersection_point(self, other):
        """一意の交点を Point で返す。平行・一致なら None。

        int/Fraction 入力なら座標も厳密。O(1)。
        """
        if self.parallel(other):
            return None
        return _line_intersection_point(self.p, self.q, other.p, other.q)

    def intersection(self, other):
        """交点を (x,y) タプルで返す。平行・一致なら None（元API互換）。"""
        p = self.intersection_point(other)
        return None if p is None else p.as_tuple()

    def projection(self, point):
        """点から無限直線に下ろした垂線の足。Point（厳密）。"""
        return project_point(self, point)

    def reflection(self, point):
        """点を直線で反射した位置。Point（厳密）。"""
        return reflect_point(self, point)

    def distance_sq_to_point(self, point):
        """直線と点との最短距離の二乗。厳密（有理数）。"""
        v = self.direction()
        c = v.cross(point - self.p)
        return _divide(c * c, v.norm_sq())

    def distance_to_point(self, point):
        """直線と点との最短距離。float。"""
        return sqrt(self.distance_sq_to_point(point))


class Segment:
    """端点を含む閉線分。両端点が同じ退化線分も許す。"""

    __slots__ = ('p', 'q')

    def __init__(self, p, q):
        self.p, self.q = p, q

    def __repr__(self):
        return f'Segment({self.p}, {self.q})'

    def as_line(self):
        """延長した無限直線を返す。長さ0の場合は ValueError。"""
        return Line(self.p, self.q)

    def direction(self):
        """方向ベクトル q - p。"""
        return self.q - self.p

    def midpoint(self):
        """線分の中点。int/Fraction は厳密な Point。"""
        return (self.p + self.q) / 2

    def bbox(self):
        """軸平行の外接矩形 (min_x, min_y, max_x, max_y)。"""
        return (min(self.p.x, self.q.x), min(self.p.y, self.q.y),
                max(self.p.x, self.q.x), max(self.p.y, self.q.y))

    def length_sq(self):
        """線分の長さの二乗。厳密。"""
        return distance_sq(self.p, self.q)

    def length(self):
        """線分の長さ。float。"""
        return distance(self.p, self.q)

    def contains(self, point):
        """点が閉線分上にあるか（端点・退化線分に対応）。"""
        return on_segment(self.p, point, self.q)

    def intersects(self, other):
        """2線分の共通部分が空でないか。端点接触・重なりも True。O(1)。"""
        p, q, r, s = self.p, self.q, other.p, other.q
        a, b = orientation(p, q, r), orientation(p, q, s)
        c, d = orientation(r, s, p), orientation(r, s, q)
        if a * b < 0 and c * d < 0:
            return True
        return (a == 0 and on_segment(p, r, q)
                or b == 0 and on_segment(p, s, q)
                or c == 0 and on_segment(r, p, s)
                or d == 0 and on_segment(r, q, s))

    def intersection(self, other):
        """2線分の共通部分を返す。O(1)。

        交差なし: None
        1点で交わる: Point（整数・Fraction 入力なら厳密）
        同一直線上で区間が重なる: Segment（両端は元の点）
        """
        if not self.intersects(other):
            return None
        if self.p == self.q:
            return self.p
        if other.p == other.q:
            return other.p
        if self.direction().cross(other.direction()) == 0:
            # 共線の端点は辞書順で単調なので、共通区間も辞書順で求まる。
            lo = max(min(self.p, self.q), min(other.p, other.q))
            hi = min(max(self.p, self.q), max(other.p, other.q))
            return lo if lo == hi else Segment(lo, hi)
        return _line_intersection_point(self.p, self.q, other.p, other.q)

    def closest_point(self, point):
        """線分上で point に最も近い点を返す。int/Fraction なら厳密。"""
        v = self.direction()
        d = v.norm_sq()
        if d == 0:
            return self.p
        t = (point - self.p).dot(v)
        if t <= 0:
            return self.p
        if t >= d:
            return self.q
        return self.p + v * _divide(t, d)

    def distance_sq_to_point(self, point):
        """点から線分までの最短距離の二乗。厳密（有理数）。O(1)。"""
        v = self.direction()
        d = v.norm_sq()
        if d == 0:
            return distance_sq(point, self.p)
        t = (point - self.p).dot(v)
        if t <= 0:
            return distance_sq(point, self.p)
        if t >= d:
            return distance_sq(point, self.q)
        c = v.cross(point - self.p)
        return _divide(c * c, d)

    def distance_to_point(self, point):
        """点から線分までの最短距離。float。"""
        return sqrt(self.distance_sq_to_point(point))

    def distance_sq_to_segment(self, other):
        """2線分間の最短距離の二乗。交差していれば0。厳密。O(1)。"""
        if self.intersects(other):
            return 0
        return min(self.distance_sq_to_point(other.p),
                   self.distance_sq_to_point(other.q),
                   other.distance_sq_to_point(self.p),
                   other.distance_sq_to_point(self.q))

    def distance_to_segment(self, other):
        """2線分間の最短距離。float。"""
        return sqrt(self.distance_sq_to_segment(other))


class Circle:
    """中心 Point、半径 r>=0 の円。

    contains など半径の二乗だけで済む判定は int/Fraction で厳密。
    intersections は平方根を用いるため float の Point を返す。
    """

    __slots__ = ('center', 'r')

    def __init__(self, center, r):
        if r < 0:
            raise ValueError('半径は0以上にしてください')
        self.center, self.r = center, r

    def __repr__(self):
        return f'Circle({self.center}, {self.r})'

    def contains(self, point, include_boundary=True):
        """円盤内か（既定で円周を含む）。整数・有理数入力なら厳密。"""
        d2 = distance_sq(self.center, point)
        r2 = self.r * self.r
        return d2 <= r2 if include_boundary else d2 < r2

    def on_circle(self, point):
        """点が円周上か。int/Fraction 入力なら厳密。"""
        return distance_sq(self.center, point) == self.r * self.r

    def intersects_line(self, line):
        """円周と無限直線が接する・交わるか。厳密。"""
        return line.distance_sq_to_point(self.center) <= self.r * self.r

    def intersects_segment(self, segment):
        """線分が円周と共有点を持つか。円盤内に完全包含された線分は False。

        円盤（内部+円周）との交差なら intersects_disk_segment を使う。
        """
        if segment.distance_sq_to_point(self.center) > self.r * self.r:
            return False
        return max(distance_sq(self.center, segment.p),
                   distance_sq(self.center, segment.q)) >= self.r * self.r

    def intersects_disk_segment(self, segment):
        """円盤（内部を含む）と線分が交差するか。厳密。"""
        return segment.distance_sq_to_point(self.center) <= self.r * self.r

    def intersects_circle(self, other):
        """2つの円周が共有点を持つか（同一円も True）。厳密。"""
        d2 = distance_sq(self.center, other.center)
        if d2 == 0:
            return self.r == other.r
        return ((self.r - other.r) ** 2 <= d2 <= (self.r + other.r) ** 2)

    def line_intersections(self, line):
        """円周と無限直線の交点。Point(float, float) のリスト（0〜2点）。

        平方根が必要なため近似値。接線時は1点。
        """
        foot = line.projection(self.center)
        d2 = distance_sq(self.center, foot)
        r2 = self.r * self.r
        if d2 > r2:
            return []
        if d2 == r2:
            return [Point(float(foot.x), float(foot.y))]
        v = line.direction()
        scale = sqrt(float(r2 - d2) / float(v.norm_sq()))
        dx, dy = v.x * scale, v.y * scale
        return [Point(float(foot.x) - dx, float(foot.y) - dy),
                Point(float(foot.x) + dx, float(foot.y) + dy)]

    def circle_intersections(self, other):
        """2円周の交点。Point(float,float) のリスト、または None。

        []: 交点なし、1点: 接する、2点: 2交点。
        None: 同一円で交点が無限個。平方根計算の結果は近似値。
        """
        dx = other.center.x - self.center.x
        dy = other.center.y - self.center.y
        d2 = dx * dx + dy * dy
        if d2 == 0:
            return None if self.r == other.r else []
        r1, r2 = self.r, other.r
        if d2 > (r1 + r2) ** 2 or d2 < (r1 - r2) ** 2:
            return []
        # 中心間方向の射影パラメータ。無理数は最後の sqrt だけで導入。
        t = float(_divide(d2 + r1 * r1 - r2 * r2, 2 * d2))
        bx = float(self.center.x) + dx * t
        by = float(self.center.y) + dy * t
        # 判別式を整数・Fraction で先に計算することで、
        # 接線判定で浮動小数点の桁落ちを起こさない。
        disc = 4 * r1 * r1 * d2 - (d2 + r1 * r1 - r2 * r2) ** 2
        if disc <= 0:
            return [Point(bx, by)]
        h = sqrt(float(disc)) / (2 * float(d2))
        return [Point(bx - dy * h, by + dx * h),
                Point(bx + dy * h, by - dx * h)]


