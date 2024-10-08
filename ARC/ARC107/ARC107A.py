import sys
import math
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 998244353
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def make_grid(h, w, num): return [[int(num)] * w for _ in range(h)]


def main():
    A, B, C = NMI()
    A = A * (1+A) // 2 % MOD
    B = B * (1 + B) // 2 % MOD
    C = C * (1 + C) // 2 % MOD
    print(A*B*C%MOD)


if __name__ == "__main__":
    main()
