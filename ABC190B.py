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
    N, S, D = NMI()
    spells = [NLI() for _ in range(N)]
    for x, y in spells:
        if x < S and y > D:
            print("Yes")
            exit()
    print("No")


if __name__ == "__main__":
    main()
