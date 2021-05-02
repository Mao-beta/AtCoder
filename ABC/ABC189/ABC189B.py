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
    N, X = NMI()
    a = 0
    for i in range(N):
        v, p = NMI()
        a += v * p
        if a > X * 100:
            print(i+1)
            exit()
    print(-1)


if __name__ == "__main__":
    main()
