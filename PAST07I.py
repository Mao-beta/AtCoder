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
    eyes = []
    for _ in range(2):
        eyes.append(NLI())
    H = [NLI() for _ in range(N)]

    x1, y1 = eyes[0]
    x2, y2 = eyes[1]
    dx = (x1 + x2) / 2
    dy = (y1 + y2) / 2

    E = math.sqrt((x2 - x1)**2 + (y2 - y1)**2) / 2
    cos = (x2 - x1) / 2 / E
    sin = (y2 - y1) / 2 / E

    for a, b in H:
        a -= dx
        b -= dy
        A = a * cos + b * sin
        B = -a * sin + b * cos
        print(A, B)


if __name__ == "__main__":
    main()
