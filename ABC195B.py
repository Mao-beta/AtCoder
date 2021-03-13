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
    A, B, W = NMI()
    W = W * 1000
    l = W // B
    r = W // A + 1
    m = 10**10
    M = -1
    for n in range(l, r+1):
        if A * n <= W <= B * n:
            m = min(m, n)
            M = max(M, n)
    if M == -1:
        print("UNSATISFIABLE")
    else:
        print(m, M)


if __name__ == "__main__":
    main()
