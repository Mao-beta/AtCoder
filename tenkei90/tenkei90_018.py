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
    T = NI()
    L, X, Y = NMI()
    Q = NI()
    for _ in range(Q):
        E = NI()
        ex = 0
        omega = -2*math.pi / T
        theta = E * omega - math.pi / 2
        ey = L/2 * math.cos(theta)
        ez = L/2 * math.sin(theta) + L/2

        xy = math.sqrt((X-ex)**2 + (Y-ey)**2)
        ans = math.atan2(ez, xy) * 180 / math.pi
        print(ans)


if __name__ == "__main__":
    main()
