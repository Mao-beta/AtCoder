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
    T = NI()
    case = [NLI() for _ in range(T)]

    for N, A, B in case:
        if N < A + B:
            print(0)
        else:
            ans = 2 * (N-A+1) * (N-B+1) * (N-A-B+1)*(N-A-B+2) - (N-A-B+1)**2 * (N-A-B+2) ** 2
            print(ans % MOD)


if __name__ == "__main__":
    main()
