"""競技プログラミング用 自己完結スニペット: 02_line_segment.py

必要なクラス・関数だけを収録。int/Fractionは厳密計算。

使い方（このファイルを解答の先頭に貼り付けてから実行）
    p, q = Point(0, 0), Point(3, 4)
    q.norm_sq(), distance_sq(p, q), distance(p, q), manhattan_distance(p, q)  # => (25, 25, 5.0, 7)
    cross3(p, Point(1, 0), Point(0, 1)), orientation(p, Point(1, 0), Point(0, 1))  # => (1, 1)
    on_segment(p, Point(1, 1), Point(2, 2))  # 第2引数が判定する点
    # => True

    line = Line(Point(0, 0), Point(2, 0))
    project_point(line, Point(1, 3)), reflect_point(line, Point(1, 3))  # => (Point(1, 0), Point(1, -3))
    vertical = Line(Point(1, -1), Point(1, 1))
    line.intersection(vertical)  # => Point(1, 0)
    segment = Segment(Point(0, 0), Point(2, 0))
    segment.contains(Point(1, 0)), segment.distance_sq_to_point(Point(3, 0))  # => (True, 1)
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


def project_point(line, p):
    """無限直線 line への垂線の足。int/Fraction 入力なら厳密な Point。
    入力: pはPoint。lineはLine。時間・追加空間O(1)回の数値演算。
    """
    v = line.q - line.p
    t = _divide((p - line.p).dot(v), v.norm_sq())
    return line.p + v * t


def reflect_point(line, p):
    """無限直線 line に関する点 p の鏡映。int/Fraction 入力なら厳密。
    入力: pはPoint。lineはLine。時間・追加空間O(1)回の数値演算。
    """
    return 2 * project_point(line, p) - p


def _line_intersection_point(a, b, c, d):
    """非平行な無限直線 ab, cd の交点。呼び出し側で非平行を確認。"""
    u, v = b - a, d - c
    t = _divide((c - a).cross(v), u.cross(v))
    return a + u * t


class Line:
    """異なるPoint p,qから定義する無限直線。Line(p,q)。同じ2点はValueError。
    p→qの向きを持ち、side(point)は左+1・右-1・線上0。
    intersection(other)は唯一の交点をPointで返す。平行・一致ならNone。座標tupleが必要なら交点のas_tuple()を使う。
    入力: p/qは異なる二つのPoint。構築O(1)時間・空間。pointは調べるPoint、otherは別のLine。normalizeは係数を正規化するかのbool。
    """

    __slots__ = ('p', 'q')

    def __init__(self, p, q):
        """入力: p/qは異なる二つのPoint。構築O(1)時間・空間。pointは調べるPoint、otherは別のLine。normalizeは係数を正規化するかのbool。
        """
        if p == q:
            raise ValueError('直線は異なる2点から定義してください')
        self.p, self.q = p, q

    def __repr__(self):
        return f'Line({self.p}, {self.q})'

    def direction(self):
        """方向ベクトル q - p。
        時間・追加空間O(1)回の数値演算。引数の型はクラスの入力規約に従う。
        """
        return self.q - self.p

    def abc(self, normalize=False):
        """ax + by + c = 0 の係数 (a,b,c)。整数座標なら整数。O(1)。

        normalize=True は整数座標専用。係数を最大公約数で割り、
        最初の非零係数が正になるよう符号も統一する。
        同じ無限直線の識別・重複除去に使える。
        normalize=FalseはO(1)回の数値演算。Trueは整数係数のgcd正規化が加わり、係数の最大絶対値Cに対してO(log(C+1))回程度の整数演算。
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
        """点が無限直線上にあるか。int/Fraction なら厳密。
        時間・追加空間O(1)回の数値演算。引数の型はクラスの入力規約に従う。
        """
        return cross3(self.p, self.q, point) == 0

    def side(self, point):
        """直線の p→q から見た左右。左 +1、右 -1、直線上 0。
        時間・追加空間O(1)回の数値演算。引数の型はクラスの入力規約に従う。
        """
        return orientation(self.p, self.q, point)

    def parallel(self, other):
        """2本の直線が平行か。重なっている場合も True。
        時間・追加空間O(1)回の数値演算。引数の型はクラスの入力規約に従う。
        """
        return self.direction().cross(other.direction()) == 0

    def coincident(self, other):
        """2本の直線が同一か。
        時間・追加空間O(1)回の数値演算。引数の型はクラスの入力規約に従う。
        """
        return self.parallel(other) and self.contains(other.p)

    def intersection(self, other):
        """一意の交点を Point で返す。平行・一致なら None。

        int/Fraction 入力なら座標も厳密。O(1)。
        時間・追加空間O(1)回の数値演算。引数の型はクラスの入力規約に従う。
        """
        if self.parallel(other):
            return None
        return _line_intersection_point(self.p, self.q, other.p, other.q)


    def projection(self, point):
        """点から無限直線に下ろした垂線の足。Point（厳密）。
        時間・追加空間O(1)回の数値演算。引数の型はクラスの入力規約に従う。
        """
        return project_point(self, point)

    def reflection(self, point):
        """点を直線で反射した位置。Point（厳密）。
        時間・追加空間O(1)回の数値演算。引数の型はクラスの入力規約に従う。
        """
        return reflect_point(self, point)

    def distance_sq_to_point(self, point):
        """直線と点との最短距離の二乗。厳密（有理数）。
        時間・追加空間O(1)回の数値演算。引数の型はクラスの入力規約に従う。
        """
        v = self.direction()
        c = v.cross(point - self.p)
        return _divide(c * c, v.norm_sq())

    def distance_to_point(self, point):
        """直線と点との最短距離。float。
        時間・追加空間O(1)回の数値演算。引数の型はクラスの入力規約に従う。
        """
        return sqrt(self.distance_sq_to_point(point))


class Segment:
    """Point p,qを両端とする閉線分Segment(p,q)。p==qの退化線分も許す。
    intersection(other)は交差なしNone、1点ならPoint、重なりならSegment。
    入力: p/qは端点のPoint（同じ点も可）。構築O(1)時間・空間。pointは調べるPoint、otherは別のSegment。
    """

    __slots__ = ('p', 'q')

    def __init__(self, p, q):
        """入力: p/qは端点のPoint（同じ点も可）。構築O(1)時間・空間。pointは調べるPoint、otherは別のSegment。
        """
        self.p, self.q = p, q

    def __repr__(self):
        return f'Segment({self.p}, {self.q})'

    def as_line(self):
        """延長した無限直線を返す。長さ0の場合は ValueError。
        時間・追加空間O(1)回の数値演算。引数の型はクラスの入力規約に従う。
        """
        return Line(self.p, self.q)

    def direction(self):
        """方向ベクトル q - p。
        時間・追加空間O(1)回の数値演算。引数の型はクラスの入力規約に従う。
        """
        return self.q - self.p

    def midpoint(self):
        """線分の中点。int/Fraction は厳密な Point。
        時間・追加空間O(1)回の数値演算。引数の型はクラスの入力規約に従う。
        """
        return (self.p + self.q) / 2

    def bbox(self):
        """軸平行の外接矩形 (min_x, min_y, max_x, max_y)。
        時間・追加空間O(1)回の数値演算。引数の型はクラスの入力規約に従う。
        """
        return (min(self.p.x, self.q.x), min(self.p.y, self.q.y),
                max(self.p.x, self.q.x), max(self.p.y, self.q.y))

    def length_sq(self):
        """線分の長さの二乗。厳密。
        時間・追加空間O(1)回の数値演算。引数の型はクラスの入力規約に従う。
        """
        return distance_sq(self.p, self.q)

    def length(self):
        """線分の長さ。float。
        時間・追加空間O(1)回の数値演算。引数の型はクラスの入力規約に従う。
        """
        return distance(self.p, self.q)

    def contains(self, point):
        """点が閉線分上にあるか（端点・退化線分に対応）。
        時間・追加空間O(1)回の数値演算。引数の型はクラスの入力規約に従う。
        """
        return on_segment(self.p, point, self.q)

    def intersects(self, other):
        """2線分の共通部分が空でないか。端点接触・重なりも True。O(1)。
        時間・追加空間O(1)回の数値演算。引数の型はクラスの入力規約に従う。
        """
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
        時間・追加空間O(1)回の数値演算。引数の型はクラスの入力規約に従う。
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
        """線分上で point に最も近い点を返す。int/Fraction なら厳密。
        時間・追加空間O(1)回の数値演算。引数の型はクラスの入力規約に従う。
        """
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
        """点から線分までの最短距離の二乗。厳密（有理数）。O(1)。
        時間・追加空間O(1)回の数値演算。引数の型はクラスの入力規約に従う。
        """
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
        """点から線分までの最短距離。float。
        時間・追加空間O(1)回の数値演算。引数の型はクラスの入力規約に従う。
        """
        return sqrt(self.distance_sq_to_point(point))

    def distance_sq_to_segment(self, other):
        """2線分間の最短距離の二乗。交差していれば0。厳密。O(1)。
        時間・追加空間O(1)回の数値演算。引数の型はクラスの入力規約に従う。
        """
        if self.intersects(other):
            return 0
        return min(self.distance_sq_to_point(other.p),
                   self.distance_sq_to_point(other.q),
                   other.distance_sq_to_point(self.p),
                   other.distance_sq_to_point(self.q))

    def distance_to_segment(self, other):
        """2線分間の最短距離。float。
        時間・追加空間O(1)回の数値演算。引数の型はクラスの入力規約に従う。
        """
        return sqrt(self.distance_sq_to_segment(other))


