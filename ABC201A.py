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
    A = NLI()
    A.sort()
    a, b, c = A
    if a - b == b - c:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
