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
    R, B = NMI()
    x, y = NMI()

    ok = -1
    ng = 10**19
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if R < mid or B < mid:
            ng = mid
            continue

        blue = (B - mid) // (y - 1)
        red = (R - mid) // (x - 1)

        if red + blue >= mid:
            ok = mid
        else:
            ng = mid

    print(ok)


if __name__ == "__main__":
    main()