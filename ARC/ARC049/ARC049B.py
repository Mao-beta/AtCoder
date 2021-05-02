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
    N = NI()
    T = [NLI() for _ in range(N)]

    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            xi, yi, ci = T[i]
            xj, yj, cj = T[j]
            x_gap = abs(xi - xj)
            y_gap = abs(yi - yj)
            gap = max(x_gap, y_gap)
            t = gap * ci * cj / (ci + cj)
            ans = max(ans, t)

    print(ans)


if __name__ == "__main__":
    main()
