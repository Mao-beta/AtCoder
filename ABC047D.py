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
    N, T = NMI()
    A = NLI()

    if N == 1:
        print(1)
        exit()

    A_min = []
    A_min.append(A[0])
    A_min.append(min(A[0], A[1]))
    for i, a in enumerate(A):
        if i < 2:
            continue
        A_min.append(min(A_min[-1], a))

    diff = [0] * N
    for i, am in enumerate(A_min):
        if i == 0:
            diff[0] = 0
            continue
        diff[i] = max(A[i] - A_min[i-1], 0)
    diff_max = max(diff)
    print(diff.count(diff_max))


if __name__ == "__main__":
    main()