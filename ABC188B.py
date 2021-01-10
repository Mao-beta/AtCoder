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
    N = NI()
    A = NLI()
    B = NLI()
    nai = 0
    for a, b in zip(A, B):
        nai += a * b
    if nai:
        print("No")
    else:
        print("Yes")


if __name__ == "__main__":
    main()
