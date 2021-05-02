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
    for i, s in enumerate(S):
        if i%2 == 0:
            if s.isupper():
                print("No")
                exit()
        else:
            if s.islower():
                print("No")
                exit()
    print("Yes")


if __name__ == "__main__":
    main()
