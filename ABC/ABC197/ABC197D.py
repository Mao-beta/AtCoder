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


def make_grid(h, w, num): return [[int(num)] * w for _ in range(h)]


def main():
    N = NI()
    x0, y0 = NMI()
    xk, yk = NMI()

    xm = (x0+xk) / 2
    ym = (y0+yk) / 2
    cos = math.cos(2 * math.pi / N)
    sin = math.sin(2 * math.pi / N)
    dx = x0 - xm
    dy = y0 - ym
    rx = cos * dx - sin * dy
    ry = sin * dx + cos * dy
    print(xm + rx, ym + ry)


if __name__ == "__main__":
    main()
