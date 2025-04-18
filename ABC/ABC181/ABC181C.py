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
    P = [NLI() for _ in range(N)]
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                ax, ay = P[i]
                bx, by = P[j]
                cx, cy = P[k]
                if ax == bx == cx:
                    print("Yes")
                    exit()
                if (bx-ax) * (cy-by) == (cx-bx) * (by-ay):
                    print("Yes")
                    exit()
    print("No")



if __name__ == "__main__":
    main()
