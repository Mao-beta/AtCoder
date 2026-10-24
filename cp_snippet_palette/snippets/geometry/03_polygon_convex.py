"""競技プログラミング用 自己完結スニペット: 03_polygon_convex.py

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

    points = [Point(0, 0), Point(2, 0), Point(2, 2), Point(0, 2)]
    polygon = Polygon(points)
    polygon.area(), polygon.locate(Point(1, 1)), polygon.locate(Point(0, 1))  # => (Fraction(4, 1), 1, 0)
    hull = Polygon.convex_hull(points + [Point(1, 1)])
    hull.contains_convex(Point(1, 1)), convex_diameter_sq(points)  # => (True, 8)
    cut = polygon.convex_cut(Line(Point(1, 0), Point(1, 2)))  # 上向き直線の左を残す
    cut.area()  # => Fraction(2, 1)
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


class Polygon:
    """Pointの列verticesを周上順に渡す多角形。通常は単純多角形を想定する。
    時計回り・反時計回りの両方可。末尾が先頭と同じなら重複を取り除く。
    順不同の点群からはPolygon.convex_hull(points)で凸包を作る。
    locate(p)は内部1・境界0・外部-1。contains(p)は境界込みのbool。
    library/geometry/convex.pyのConvexPolygon.contains（0/1/2）と戻り値が異なる。
    入力: verticesは周上順のPointの列（先頭を末尾に重ねない）。Nは頂点数。構築O(N)時間・空間。
    pointはPoint、lineはLine、include_boundary/include_collinear/keep_leftはbool。
    """

    __slots__ = ('vertices',)

    def __init__(self, vertices):
        """入力: verticesは周上順のPointの列（先頭を末尾に重ねない）。Nは頂点数。構築O(N)時間・空間。
        pointはPoint、lineはLine、include_boundary/include_collinear/keep_leftはbool。
        """
        vs = list(vertices)
        if len(vs) >= 2 and vs[-1] == vs[0]:
            vs.pop()
        self.vertices = vs

    def __repr__(self):
        return f'Polygon({self.vertices})'

    def __len__(self):
        return len(self.vertices)

    def area2(self):
        """符号付き面積の2倍。反時計回り正、時計回り負。厳密。O(N)。
        計算量のNはself.verticesの長さ。点はPoint、切断線はLineを渡す。
        """
        vs = self.vertices
        n = len(vs)
        return sum(vs[i].cross(vs[(i + 1) % n]) for i in range(n)) if n else 0

    def signed_area(self):
        """符号付き面積。int/Fraction 入力なら Fraction。O(N)。
        計算量のNはself.verticesの長さ。点はPoint、切断線はLineを渡す。
        """
        return _divide(self.area2(), 2)

    def area(self):
        """絶対面積。int/Fraction 入力なら Fraction（浮動小数点化しない）。O(N)。
        計算量のNはself.verticesの長さ。点はPoint、切断線はLineを渡す。
        """
        return abs(self.signed_area())

    def is_ccw(self):
        """面積が正（反時計回り）なら True。退化多角形は False。O(N)。
        計算量のNはself.verticesの長さ。点はPoint、切断線はLineを渡す。
        """
        return self.area2() > 0

    def perimeter(self):
        """辺長の総和。float。O(N)。
        計算量のNはself.verticesの長さ。点はPoint、切断線はLineを渡す。
        """
        vs = self.vertices
        n = len(vs)
        if n <= 1:
            return 0.0
        return sum(distance(vs[i], vs[(i + 1) % n]) for i in range(n))

    def centroid(self):
        """単純で面積>0の多角形の面積重心。厳密な Point。O(N)。

        自己交差や面積0の多角形では幾何的な面積重心は定義しない。
        計算量のNはself.verticesの長さ。点はPoint、切断線はLineを渡す。
        """
        vs = self.vertices
        n = len(vs)
        a2 = sx = sy = 0
        for i in range(n):
            p, q = vs[i], vs[(i + 1) % n]
            c = p.cross(q)
            a2 += c
            sx += (p.x + q.x) * c
            sy += (p.y + q.y) * c
        if a2 == 0:
            raise ValueError('面積が0の多角形には面積重心がありません')
        return Point(_divide(sx, 3 * a2), _divide(sy, 3 * a2))

    def locate(self, point):
        """点の位置を返す。内部 1、境界 0、外部 -1。O(N)。

        偶奇規則（ray casting）。int/Fraction は乗除算なしの厳密判定。
        通常は単純多角形を想定する。凹多角形、CW/CCW の両方に対応。
        計算量のNはself.verticesの長さ。点はPoint、切断線はLineを渡す。
        """
        vs = self.vertices
        n = len(vs)
        if n == 0:
            return -1
        inside = False
        y = point.y
        for i in range(n):
            a, b = vs[i], vs[(i + 1) % n]
            if on_segment(a, point, b):
                return 0
            if a.y <= y < b.y:
                if cross3(a, b, point) > 0:
                    inside = not inside
            elif b.y <= y < a.y:
                if cross3(a, b, point) < 0:
                    inside = not inside
        return 1 if inside else -1

    def contains(self, point, include_boundary=True):
        """点が内部（デフォルトは境界を含む）か。O(N)。
        計算量のNはself.verticesの長さ。点はPoint、切断線はLineを渡す。
        """
        z = self.locate(point)
        return z == 1 or (include_boundary and z == 0)

    def contains_strict(self, point):
        """点が境界ではない厳密な内部か。O(N)。
        計算量のNはself.verticesの長さ。点はPoint、切断線はLineを渡す。
        """
        return self.locate(point) == 1

    def is_convex(self, strict=False):
        """頂点列が凸多角形か。strict=True では180度の角も不可。O(N)。
        計算量のNはself.verticesの長さ。点はPoint、切断線はLineを渡す。
        """
        vs = self.vertices
        n = len(vs)
        if n < 3:
            return False
        sign = 0
        for i in range(n):
            c = cross3(vs[i], vs[(i + 1) % n], vs[(i + 2) % n])
            if c == 0:
                if strict:
                    return False
                continue
            s = 1 if c > 0 else -1
            if sign and sign != s:
                return False
            sign = s
        return sign != 0

    def contains_convex(self, point, include_boundary=True):
        """凸多角形内の点を O(log N) で判定する。

        頂点は凸包の順に循環配置され、隣接頂点が重複せず、
        面積が正であること。時計回り・反時計回りのどちらも対応。
        1本の辺上に3頂点以上がある場合も使用できるが、
        頂点0からの両境界辺に途中の頂点がある退化配置では
        判定誤りを避けるため O(N) 判定に切り替える。
        事前に is_convex() で検証する場合、その検証コストは O(N)。
        計算量のNはself.verticesの長さ。点はPoint、切断線はLineを渡す。
        """
        vs = self.vertices
        n = len(vs)
        if n < 3:
            return self.contains(point, include_boundary)
        a, b, z = vs[0], vs[1], vs[-1]
        turn = cross3(a, b, z)
        if (turn == 0 or cross3(vs[0], vs[1], vs[2]) == 0
                or cross3(vs[-2], vs[-1], vs[0]) == 0):
            # p0->p1 や p0->p[-1] の先にも辺上の点があり得る。
            return self.contains(point, include_boundary)
        s = 1 if turn > 0 else -1
        left = s * cross3(a, b, point)
        right = s * cross3(a, z, point)
        if left < 0 or right > 0:
            return False
        if left == 0:
            return include_boundary and on_segment(a, point, b)
        if right == 0:
            return include_boundary and on_segment(a, point, z)
        lo, hi = 1, n - 1
        while hi - lo > 1:
            mid = (lo + hi) >> 1
            if s * cross3(a, vs[mid], point) >= 0:
                lo = mid
            else:
                hi = mid
        c = s * cross3(vs[lo], vs[lo + 1], point)
        if c < 0:
            return False
        if c == 0:
            return include_boundary and on_segment(vs[lo], point, vs[lo + 1])
        return True

    @staticmethod
    def convex_hull(points, include_collinear=False):
        """Monotone Chain 法で凸包を Polygon で返す。O(N log N)。

        重複点を除外、出力は反時計回り（点数が2以下の場合を除く）。
        デフォルトでは辺の途中の共線点は除外する。
        include_collinear=True なら辺上の点もすべて採用する。
        全点が一直線上のときは、Falseなら両端、Trueなら全点を返す。
        pointsはPointの列、N=len(points)。include_collinearは辺上の中間点を残すかのbool。出力・作業空間O(N)。
        """
        ps = sorted(set(points))
        n = len(ps)
        if n <= 2:
            return Polygon(ps)
        if all(cross3(ps[0], ps[-1], p) == 0 for p in ps):
            return Polygon(ps if include_collinear else [ps[0], ps[-1]])
        lower, upper = [], []
        for p in ps:
            while len(lower) >= 2:
                c = cross3(lower[-2], lower[-1], p)
                if c < 0 or (c == 0 and not include_collinear):
                    lower.pop()
                else:
                    break
            lower.append(p)
        for p in reversed(ps):
            while len(upper) >= 2:
                c = cross3(upper[-2], upper[-1], p)
                if c < 0 or (c == 0 and not include_collinear):
                    upper.pop()
                else:
                    break
            upper.append(p)
        return Polygon(lower[:-1] + upper[:-1])

    def diameter_sq(self):
        """頂点集合の最遠点対距離の二乗。凸包+回転キャリパー、O(N log N)。
        計算量のNはself.verticesの長さ。点はPoint、切断線はLineを渡す。
        """
        return convex_diameter_sq(self.vertices)

    def diameter(self):
        """頂点集合の最遠点対距離。float。O(N log N)。
        計算量のNはself.verticesの長さ。点はPoint、切断線はLineを渡す。
        """
        return sqrt(self.diameter_sq())

    def convex_cut(self, line, keep_left=True):
        """凸多角形を有向直線で切り、左側（既定）または右側を Polygon で返す。

        線上は残す。交点座標は int/Fraction 入力なら厳密。
        O(N)。入力が非凸の場合は結果を保証しない。
        計算量のNはself.verticesの長さ。点はPoint、切断線はLineを渡す。
        """
        vs = self.vertices
        n = len(vs)
        if n == 0:
            return Polygon([])
        out = []
        s = 1 if keep_left else -1
        for i in range(n):
            a, b = vs[i], vs[(i + 1) % n]
            ca = s * cross3(line.p, line.q, a)
            cb = s * cross3(line.p, line.q, b)
            if ca >= 0:
                if not out or out[-1] != a:
                    out.append(a)
            if (ca < 0 < cb) or (cb < 0 < ca):
                t = _divide(ca, ca - cb)
                x = a + (b - a) * t
                if not out or out[-1] != x:
                    out.append(x)
        return Polygon(out)


def convex_diameter_sq(points):
    """与えられた点集合の最遠点対の距離の二乗。厳密、O(N log N)。

    N=0,1 の場合は0。内部で凸包を構築し、回転キャリパー法を使う。
    pointsはPointの列、N=len(points)。時間O(N log(N+1))、追加空間O(N)。
    """
    vs = Polygon.convex_hull(points).vertices
    n = len(vs)
    if n <= 1:
        return 0
    if n == 2:
        return distance_sq(vs[0], vs[1])
    ans = 0
    j = 1
    for i in range(n):
        ni = (i + 1) % n
        edge = vs[ni] - vs[i]
        while (edge.cross(vs[(j + 1) % n] - vs[i])
               > edge.cross(vs[j] - vs[i])):
            j = (j + 1) % n
        ans = max(ans, distance_sq(vs[i], vs[j]),
                  distance_sq(vs[ni], vs[j]))
    return ans


