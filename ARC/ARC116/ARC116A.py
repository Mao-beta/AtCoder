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
    for _ in range(T):
        N = NI()
        if N % 2:
            print("Odd")
        elif N % 4:
            print("Same")
        else:
            print("Even")


if __name__ == "__main__":
    main()
