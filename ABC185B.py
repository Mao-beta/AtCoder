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
    N, M, T = NMI()
    cafes = [NLI() for _ in range(M)]
    now = 0
    cap = N
    for a, b in cafes:
        N -= a - now
        now = a
        if N <= 0:
            print("No")
            exit()
        N += b - a
        N = min(cap, N)
        now = b
    N -= T - now
    if N <= 0:
        print("No")
        exit()
    print("Yes")


if __name__ == "__main__":
    main()
