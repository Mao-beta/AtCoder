import sys
import math
from collections import deque

sys.setrecursionlimit(100000)
MOD = 998244353
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    H, W, K = NMI()
    sx, sy, tx, ty = NMI()

    ans = [0, 0, 0, 0]
    if sx != tx and sy != ty:
        ans[0] = 1
    elif sx == tx and sy != ty:
        ans[1] = 1
    elif sx != tx and sy == ty:
        ans[2] = 1
    else:
        ans[3] = 1

    for k in range(K):
        f, x, y, t = ans
        ans[0] = (H+W-4) * f + (H-1) * x + (W-1) * y +     0 * t
        ans[1] =       1 * f + (W-2) * x +     0 * y + (W-1) * t
        ans[2] =       1 * f +     0 * x + (H-2) * y + (H-1) * t
        ans[3] =       0 * f +     1 * x +     1 * y +     0 * t
        for i in range(4):
            ans[i] %= MOD

    print(ans[3])


if __name__ == "__main__":
    main()
