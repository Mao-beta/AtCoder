import sys
import math
from collections import deque
import heapq as hq

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
    P = NLI()
    flags = [0] * 200002
    x = 0
    for p in P:
        flags[p] = 1
        while flags[x] == 1:
            x += 1
        print(x)


if __name__ == "__main__":
    main()
