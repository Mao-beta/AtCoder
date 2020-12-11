import sys
import math
from collections import deque
from itertools import combinations

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def make_grid(h, w, num): return [[int(num)] * w for _ in range(h)]


def main():
    A, B, C, D = NMI()
    S = A+B+C+D
    if S%2:
        print("No")
        exit()
    for r in range(1, 4):
        for T in combinations([A,B,C,D], r):
            if sum(T) * 2 == S:
                print("Yes")
                exit()
    print("No")


if __name__ == "__main__":
    main()
