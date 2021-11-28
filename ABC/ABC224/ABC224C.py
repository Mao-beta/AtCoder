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


def area(x1, y1, x2, y2, x3, y3):
    dx1 = x2 - x1
    dx2 = x3 - x1
    dy1 = y2 - y1
    dy2 = y3 - y1
    return dx1 * dy2 - dx2 * dy1


def main():
    N = NI()
    XY = [NLI() for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                a = area(XY[i][0], XY[i][1], XY[j][0], XY[j][1], XY[k][0], XY[k][1])
                if a:
                    ans += 1
    print(ans)


if __name__ == "__main__":
    main()
