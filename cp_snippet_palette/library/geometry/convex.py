"""整数幾何。出典: yuki_0096.py, ABC022D, ABC296G。点は(x,y)タプル。
PyPy向け。Codonでは外積・距離二乗の中間値も64bit以内に収める。

使い方（このファイルを解答の先頭に貼り付けてから実行）
    points = [(0, 0), (2, 0), (2, 2), (0, 2), (1, 1)]
    hull = convex_hull_points(points)
    convex_diameter_sq(hull)  # => 8
    polygon = ConvexPolygon(points)
    polygon.locate((1, 1)), polygon.locate((0, 1)), polygon.locate((3, 1))  # => (1, 0, -1)
    polygon.contains((0, 1)), polygon.contains_strict((0, 1))  # => (True, False)
"""


def _cross2(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def convex_hull_points(points):
    """(x,y)の列から反時計回りの凸包をタプルのlistで返す。O(n log n)。
    始点の重複なし。重複点・辺上の中間点を除く。共線なら両端、空なら[]。
    座標は整数などの数値tuple。nは入力の点数。凸包構築はO(n)空間、直径計算は入力以外O(1)空間。
    pointsは点の(x,y) tupleの列。
    """
    points = sorted(set(points))
    if len(points) <= 1:
        return points
    lower, upper = [], []
    for p in points:
        while len(lower) >= 2 and _cross2(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    for p in reversed(points):
        while len(upper) >= 2 and _cross2(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]


def convex_diameter_sq(hull):
    """convex_hull_pointsのような反時計回り凸包から最遠2点の距離の二乗を返す。
    始点を末尾に重複させない。0/1点なら0。回転キャリパーO(n)。
    座標は整数などの数値tuple。nは入力の点数。凸包構築はO(n)空間、直径計算は入力以外O(1)空間。
    hullは反時計回りに並んだ凸包頂点の(x,y) tupleの列。
    """
    n = len(hull)
    if n <= 1:
        return 0

    def distance(a, b):
        return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

    if n == 2:
        return distance(hull[0], hull[1])
    best, j = 0, 1
    for i in range(n):
        nxt = (i + 1) % n
        while _cross2(hull[i], hull[nxt], hull[(j + 1) % n]) > _cross2(
            hull[i], hull[nxt], hull[j]
        ):
            j = (j + 1) % n
        best = max(best, distance(hull[i], hull[j]), distance(hull[nxt], hull[j]))
    return best


class ConvexPolygon:
    """points=[(x,y),...]の凸包を構築し、点の内外判定を繰り返す。
    構築O(n log n)、locate(p)はO(log n)。頂点の事前整列は不要。
    入力: pointsは数値座標(x,y)の列。n=len(points)、構築O(n log(n+1))時間・O(n)空間。locate/contains/contains_strictのpも(x,y)のtuple。
    """
    def __init__(self, points):
        """入力: pointsは数値座標(x,y)の列。n=len(points)、構築O(n log(n+1))時間・O(n)空間。locate/contains/contains_strictのpも(x,y)のtuple。
        """
        self.vertices = convex_hull_points(points)

    def locate(self, p):
        """O(log n)。外-1、境界0、内部1。空・点・線分にも対応。"""
        q = self.vertices
        n = len(q)
        if n == 0:
            return -1
        if n == 1:
            return 0 if p == q[0] else -1

        def on_segment(a, b):
            return (
                _cross2(a, b, p) == 0
                and min(a[0], b[0]) <= p[0] <= max(a[0], b[0])
                and min(a[1], b[1]) <= p[1] <= max(a[1], b[1])
            )

        if n == 2:
            return 0 if on_segment(q[0], q[1]) else -1
        first = _cross2(q[0], q[1], p)
        last = _cross2(q[0], q[-1], p)
        if first < 0 or last > 0:
            return -1
        if first == 0:
            return 0 if on_segment(q[0], q[1]) else -1
        if last == 0:
            return 0 if on_segment(q[0], q[-1]) else -1
        left, right = 1, n - 1
        while right - left > 1:
            mid = (left + right) // 2
            if _cross2(q[0], q[mid], p) >= 0:
                left = mid
            else:
                right = mid
        cross = _cross2(q[left], q[right], p)
        return 1 if cross > 0 else (0 if cross == 0 else -1)

    def contains(self, p, include_boundary=True):
        """点p=(x,y)が内部ならTrue。include_boundary=Trueでは境界も含む。
        O(log(N+1))時間、追加空間O(1)。Nは凸包頂点数。
        """
        location = self.locate(p)
        return location == 1 or (include_boundary and location == 0)

    def contains_strict(self, p):
        """点p=(x,y)が内部ならTrue。境界はFalse。O(log(N+1))時間、追加空間O(1)。"""
        return self.locate(p) > 0
