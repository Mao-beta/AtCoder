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
    N, P = NMI()
    if N == 1:
        print(P-1)
        exit()

    if P == 2:
        print(0)
        exit()

    print((P-1) * pow(P-2, N-1, MOD) % MOD)


if __name__ == "__main__":
    main()
