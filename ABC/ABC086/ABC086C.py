import sys
import math
from collections import defaultdict
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
    TXY = [NLI() for _ in range(N)]
    T, X, Y = 0, 0, 0
    for t, x, y in TXY:
        gx, gy = abs(X-x), abs(Y-y)
        gt = t - T
        l = gx + gy
        if l > gt:
            print("No")
            exit()
        if (gt - l) % 2:
            print("No")
            exit()

        T, X, Y = t, x, y

    print("Yes")


if __name__ == "__main__":
    main()
