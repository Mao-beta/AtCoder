import sys
import math
from collections import deque

sys.setrecursionlimit(100000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


# 有理数クラス
class MyFraction:
    def __init__(self, a, b):
        assert b != 0, "分母が0です"

        if b < 0:
            a, b = -a, -b
        if a == 0:
            b = 1

        g = math.gcd(a, b)
        self.numerator = a // g
        self.denominator = b // g

    def __add__(self, other):
        Fa_n, Fa_d = self.get_nd()
        Fb_n, Fb_d = other.get_nd()
        F_n = Fa_d * Fb_n + Fa_n * Fb_d
        F_d = Fa_d * Fb_d
        return MyFraction(F_n, F_d)

    def __sub__(self, other):
        Fa_n, Fa_d = self.get_nd()
        Fb_n, Fb_d = other.get_nd()
        F_n = - Fa_d * Fb_n + Fa_n * Fb_d
        F_d = Fa_d * Fb_d
        return MyFraction(F_n, F_d)

    def __mul__(self, other):
        Fa_n, Fa_d = self.get_nd()
        Fb_n, Fb_d = other.get_nd()
        F_n = Fa_n * Fb_n
        F_d = Fa_d * Fb_d
        return MyFraction(F_n, F_d)

    def __truediv__(self, other):
        Fa_n, Fa_d = self.get_nd()
        Fb_d, Fb_n = other.get_nd()
        F_n = Fa_n * Fb_n
        F_d = Fa_d * Fb_d
        return MyFraction(F_n, F_d)

    def __repr__(self):
        return "{0}/{1}".format(self.numerator, self.denominator)


    def __lt__(self, other):
        Fa_n, Fa_d = self.get_nd()
        Fb_n, Fb_d = other.get_nd()
        return Fa_n * Fb_d < Fb_n * Fa_d

    def __le__(self, other):
        Fa_n, Fa_d = self.get_nd()
        Fb_n, Fb_d = other.get_nd()
        return Fa_n * Fb_d <= Fb_n * Fa_d

    def get_nd(self):
        return (self.numerator, self.denominator)


def main():
    N = NI()
    XY = [NLI() for _ in range(N)]
    INF = 10**10
    T = []
    for x, y in XY:
        l = MyFraction(y-1, x)
        if x == 1:
            r = MyFraction(INF, 1)
        else:
            r = MyFraction(y, x-1)
        T.append([l, r])

    T.sort(key=lambda x: x[1])
    now = MyFraction(0, 1)
    ans = 0
    for l, r in T:
        if now <= l:
            ans += 1
            now = r

    print(ans)


if __name__ == "__main__":
    main()
