import sys
import math
from collections import deque
import bisect

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def make_grid(h, w, num): return [[int(num)] * w for _ in range(h)]


def main():
    N, T = NMI()
    A = NLI()
    AX = A[:N//2]
    AY = A[N//2:]

    lx = len(AX)
    ly = len(AY)

    sum_X = []
    sum_Y = []
    for case in range(2**lx):
        s = 0
        for i in range(lx):
            if (case >> i) & 1:
                s += AX[i]
        sum_X.append(s)

    for case in range(2**ly):
        s = 0
        for i in range(ly):
            if (case >> i) & 1:
                s += AY[i]
        sum_Y.append(s)

    sum_X.sort()
    sum_Y.sort()

    ans = 0
    for x in sum_X:
        rem = T - x
        if rem < 0:
            break
        idx = bisect.bisect_right(sum_Y, rem)
        y = sum_Y[idx - 1]

        ans = max(ans, x+y)
    print(ans)


if __name__ == "__main__":
    main()
