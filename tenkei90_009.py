import sys
import math
import bisect

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Segment:
    def __init__(self, A, B):
        self.A = A
        self.B = B
        self.angle = self.get_angle()

    def get_angle(self):
        xa, ya = self.A.x, self.A.y
        xb, yb = self.B.x, self.B.y
        return math.atan2(yb-ya, xb-xa) * 180 / math.pi % 360


def main():
    N = NI()
    P = []
    for _ in range(N):
        x, y = NMI()
        P.append(Point(x, y))

    ans = -1
    for i in range(N):
        angles = []
        for j in range(N):
            if i == j: continue
            segment = Segment(P[i], P[j])
            angles.append(segment.get_angle())
        angles.sort()

        for j in range(N):
            if i == j:
                continue
            target = Segment(P[i], P[j]).get_angle() + 180
            target %= 360
            idx = bisect.bisect_left(angles, target) % len(angles)

            p, q = abs(angles[idx] - target), abs(angles[idx-1] - target)
            if p >= 180: p = 360 - p
            if q >= 180: q = 360 - q

            tmp = max(180-p, 180-q)
            ans = max(tmp, ans)
    print(ans)


if __name__ == "__main__":
    main()
