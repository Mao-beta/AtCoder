import sys
import math
from collections import defaultdict
from collections import deque

sys.setrecursionlimit(1000000)
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

    def __str__(self):
        return "{0}/{1}".format(self.numerator, self.denominator)


def main():
    N = NI()
    AB = defaultdict(int)
    Y, Z = 0, 0
    for i in range(N):
        a, b = NMI()
        if a == b == 0:
            Z += 1
            continue
        if b == 0:
            Y += 1
            continue

        if str(MyFraction(a, b)) in AB:
            AB[str(MyFraction(a, b))] += 1
        else:
            AB[str(MyFraction(a, b))] = 1

    C = defaultdict(lambda: ())
    ans = 1
    flag = True
    for ab, k in list(AB.items()):
        a, b = ab.split("/")
        a = int(a)
        b = int(b)
        if a > 0:
            if str(MyFraction(-b, a)) in AB:
                t = AB[str(MyFraction(-b, a))]
            else:
                t = 0
        elif a < 0:
            if str(MyFraction(b, -a)) in AB:
                continue
            t = 0
        else:
            flag = False
            t = Y
        C[(a, b)] = (k, t)

    for k, t in list(C.values()):
        tmp = pow(2, k, MOD) + pow(2, t, MOD) - 1
        ans = ans * tmp % MOD

    if flag:
        tmp = pow(2, Y, MOD)
        ans = ans * tmp % MOD
    print((ans + Z - 1)%MOD)


if __name__ == "__main__":
    main()