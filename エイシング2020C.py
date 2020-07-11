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
    A = [0] * (N+1)
    for x in range(1, 102):
        for y in range(1, 102):
            for z in range(1, 102):
                t = x*x + y*y + z*z + x*y + y*z + z*x
                if t <= N:
                    A[t] += 1
    for i in range(1, N+1):
        print(A[i])


if __name__ == "__main__":
    main()