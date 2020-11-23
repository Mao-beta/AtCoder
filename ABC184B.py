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
    S = SI()
    for s in S:
        X += 1 if s == "o" else -1
        if X <= 0:
            X = 0
    print(X)


if __name__ == "__main__":
    main()
