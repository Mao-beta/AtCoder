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
    X, Y, A, B = NMI()
    ex = 0
    while X <= B//(A-1):
        if X*A >= Y:
            print(ex)
            exit()
        X *= A
        ex += 1
    print(ex + (Y-X-1)//B)


if __name__ == "__main__":
    main()
