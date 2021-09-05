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


def main():
    A, B = NMI()
    C = A + B
    if C >= 15 and B >= 8:
        print(1)
    elif C >= 10 and B >= 3:
        print(2)
    elif C >= 3:
        print(3)
    else:
        print(4)


if __name__ == "__main__":
    main()
