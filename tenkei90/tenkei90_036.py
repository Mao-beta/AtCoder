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
    P = [NLI() for _ in range(N)]
    P = [[x+y, x-y] for x, y in P]
    querys = [NI() for _ in range(Q)]

    INF = 10**10
    xmax, xmin = -INF, INF
    ymax, ymin = -INF, INF
    for x, y in P:
        xmax = max(xmax, x)
        xmin = min(xmin, x)
        ymax = max(ymax, y)
        ymin = min(ymin, y)

    for q in querys:
        q -= 1
        x, y = P[q]
        print(max(abs(xmax-x), abs(xmin-x), abs(ymax-y), abs(ymin-y)))


if __name__ == "__main__":
    main()
