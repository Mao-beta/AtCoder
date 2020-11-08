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
    C = [0]
    for a in A:
        C.append(C[-1] + a)
    points = [0]
    for c in C[1:]:
        points.append(points[-1]+c)
    maxes = [0]
    for c in C[1:]:
        maxes.append(max(maxes[-1], c))
    tops = [0]
    for p, m in zip(points, maxes[1:]):
        tops.append(p+m)
    print(max(points+tops))


if __name__ == "__main__":
    main()
