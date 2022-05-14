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


def main():
    N, Q = NMI()
    XRH = [NLI() for _ in range(N)]
    AB = [NLI() for _ in range(Q)]

    def v(rad, height):
        return rad**2 * math.pi * height / 3

    def calc(x, h, a, b, r):
        l = x
        res = 0
        if l < a:
            ra = r * (l + h - a) / h
            rb = r * (l + h - b) / h

            if l+h >= b:
                res = v(ra, l+h-a) - v(rb, l+h-b)

            elif l+h >= a:
                res = v(ra, l+h-a)

        elif l < b:
            rb = r * (l + h - b) / h

            if l+h >= b:
                res = v(r, h) - v(rb, l+h-b)
            else:
                res = v(r, h)

        return res


    for a, b in AB:
        ans = 0
        for x, r, h in XRH:
            ans += calc(x, h, a, b, r)
        print(ans)


if __name__ == "__main__":
    main()
