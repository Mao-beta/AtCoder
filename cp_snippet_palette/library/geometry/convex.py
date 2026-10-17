"""整数幾何。出典: yuki_0096.py, ABC022D, ABC296G。点は(x,y)タプル。
PyPy向け。Codonでは外積・距離二乗の中間値も64bit以内に収める。
"""


def _cross2(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def convex_hull_points(points):
    """O(n log n)。反時計回り。重複と辺上の中間点を除く。共線なら両端。"""
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
    """反時計回り凸包の直径の二乗。回転キャリパーO(n)。"""
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
    def __init__(self, points):
        """点群の凸包を作る。O(n log n)。"""
        self.vertices = convex_hull_points(points)

    def contains(self, p):
        """O(log n)。外0、境界1、内部2。空・点・線分にも対応。"""
        q = self.vertices
        n = len(q)
        if n == 0:
            return 0
        if n == 1:
            return int(p == q[0])

        def on_segment(a, b):
            return (
                _cross2(a, b, p) == 0
                and min(a[0], b[0]) <= p[0] <= max(a[0], b[0])
                and min(a[1], b[1]) <= p[1] <= max(a[1], b[1])
            )

        if n == 2:
            return int(on_segment(q[0], q[1]))
        first = _cross2(q[0], q[1], p)
        last = _cross2(q[0], q[-1], p)
        if first < 0 or last > 0:
            return 0
        if first == 0:
            return int(on_segment(q[0], q[1]))
        if last == 0:
            return int(on_segment(q[0], q[-1]))
        left, right = 1, n - 1
        while right - left > 1:
            mid = (left + right) // 2
            if _cross2(q[0], q[mid], p) >= 0:
                left = mid
            else:
                right = mid
        cross = _cross2(q[left], q[right], p)
        return 2 if cross > 0 else (1 if cross == 0 else 0)
