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
    S, P = NMI()
    for n in range(1, 10**6+1):
        if P % n:
            continue
        m = P // n
        if m + n == S:
            print("Yes")
            exit()
    print("No")


if __name__ == "__main__":
    main()
