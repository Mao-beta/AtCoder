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


def make_grid(h, w, num): return [[int(num)] * w for _ in range(h)]


def main():
    R, X, Y = NMI()

    d2 = X**2 + Y**2

    if d2 < R**2:
        print(2)
        exit()

    if d2 % (R**2):
        k2 = d2 // (R**2)
        print(math.isqrt(k2) + 1)

    else:
        k2 = d2 // (R**2)
        if math.isqrt(k2) ** 2 == k2:
            print(math.isqrt(k2))
        else:
            print(math.isqrt(k2)+1)


if __name__ == "__main__":
    main()
