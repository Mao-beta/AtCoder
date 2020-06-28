import sys
import math
from collections import deque
import bisect

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def make_grid(h, w, num): return [[int(num)] * w for _ in range(h)]


def main():
    N, M = NMI()
    A = NLI()
    C = [-1] * N
    for a in A:
        idx = bisect.bisect_left(C, a)
        if idx == 0:
            print(-1)
            continue

        C[idx - 1] = a
        print(N+1 - idx)


if __name__ == "__main__":
    main()