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
    N = int(input())
    A = list(map(int, input().split()))
    B = [abs(a) for a in A]
    t = min(B)
    fu = 0
    for a in A:
        if a < 0:
            fu += 1
    print(sum(B) - t*2 if fu % 2 else sum(B))


if __name__ == "__main__":
    main()