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
    N, M = NMI()
    odd = 0
    even = 0
    for _ in range(N):
        S = input()
        if S.count("1") % 2:
            odd += 1
        else:
            even += 1
    print(odd * even)


if __name__ == "__main__":
    main()
