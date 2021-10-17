import sys
import math
from collections import deque

sys.setrecursionlimit(100000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    X = NI()
    if X % 100 == 0 and X > 0:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
