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
    A = NLI()
    a, b, c = A
    x = b - a
    y = c - b
    if x >= y:
        print(x - y)
    else:
        if (y-x) % 2:
            q = (y-x) // 2 + 1
        else:
            q = (y-x) // 2
        print(x-y + 3*q)


if __name__ == "__main__":
    main()
