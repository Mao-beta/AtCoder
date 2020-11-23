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
    a, b = NMI()
    c, d = NMI()

    x = a-c
    y = b-d

    if x==0 and y==0:
        print(0)
        exit()

    if abs(x) + abs(y) <= 3 or a+b == c+d or a-b == c-d:
        print(1)
        exit()

    if abs(x) + abs(y) <= 6 or abs(x-y) <= 3 or abs(x+y) <= 3:
        print(2)
        exit()


    if (x-y) % 2:
        print(3)
    else:
        print(2)


if __name__ == "__main__":
    main()
