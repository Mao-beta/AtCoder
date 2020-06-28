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
    S = SI()
    h = 0
    is_dict = False
    for s in S:
        if s == "{":
            h += 1
        elif s == "}":
            h -= 1
        elif s == ":" and h == 1:
            is_dict = True
            break

    print("dict" if is_dict or S == "{}" else "set")


if __name__ == "__main__":
    main()