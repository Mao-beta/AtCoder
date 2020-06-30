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


def combinations_mod(n, r, mod=1000000007):
    """Returns nCr in mod."""
    r = min(r, n - r)
    combs = 1
    for i, j in zip(range(n - r + 1, n + 1), range(1, r + 1)):
        combs *= (i % mod) * pow(j, mod - 2, mod)
        combs %= mod
    return combs


def main():
    X, Y = NMI()
    if (2*Y - X)%3 or (2*X - Y)%3:
        print(0)
        exit()

    A = (2*Y - X) // 3
    B = (2*X - Y) // 3
    if A < 0 or B < 0:
        print(0)
        exit()
    print(combinations_mod(A+B, A))


if __name__ == "__main__":
    main()