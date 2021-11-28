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


def main():
    N = NI()
    XY = [NLI() for _ in range(N)]

    M = set()

    for i in range(N):
        for j in range(i+1, N):
            xi, yi = XY[i]
            xj, yj = XY[j]

            if xi > xj:
                xi, xj = xj, xi
                yi, yj = yj, yi

            if xi == xj:
                M.add((0, 1))
                M.add((0, -1))
            else:
                dx = xj - xi
                dy = yj - yi
                g = math.gcd(dx, dy)
                dx //= g
                dy //= g
                M.add((dx, dy))
                M.add((-dx, -dy))

    print(len(M))


if __name__ == "__main__":
    main()
