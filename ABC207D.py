import sys
import math
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    N = NI()
    AB = [NLI() for _ in range(N)]
    CD = [NLI() for _ in range(N)]

    def center(points):
        """
        pointsの重心を返す
        points: 点(x,y)のリスト
        """
        X = 0
        Y = 0
        n = len(points)
        for x, y in points:
            X += x
            Y += y
        X /= n
        Y /= n
        return X, Y

    gab_x, gab_y = center(AB)
    gcd_x, gcd_y = center(CD)
    AB = [[a-gab_x, b-gab_y] for a, b in AB]
    CD = [[c-gcd_x, d-gcd_y] for c, d in CD]

    def rotate(point, angle):
        x, y = point
        c = math.cos(angle)
        s = math.sin(angle)
        return c*x - s*y, s*x + c*y

    def rotate_points(points, angle):
        return [rotate(p, angle) for p in points]

    def close_points(PA, PB, eps):
        rPA = []
        rPB = []
        e = 8
        for x, y in PA:
            rPA.append([round(x, e), round(y, e)])
        for x, y in PB:
            rPB.append([round(x, e), round(y, e)])
        rPA.sort()
        rPB.sort()

        for (ax, ay), (bx, by) in zip(rPA, rPB):
            if abs((ax-bx)**2 + (ay-by)**2) > eps:
                return False
        return True

    eps = 1e-6
    a, b = AB[0]
    # AB[0]が原点のときがコーナーケース
    if abs(a) < eps and abs(b) < eps:
        a, b = AB[-1]
    theta_a = math.atan2(b, a)
    for c, d in CD:
        if abs((a-c)**2 + (b-d)**2) > eps:
            pass
        theta_c = math.atan2(d, c)

        rAB = rotate_points(AB, theta_c - theta_a)

        if close_points(rAB, CD, eps):
            print("Yes")
            exit()
    print("No")




if __name__ == "__main__":
    main()
