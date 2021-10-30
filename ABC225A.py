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
    N = len(set(SI()))
    if N == 1:
        print(1)
    elif N == 2:
        print(3)
    else:
        print(6)


if __name__ == "__main__":
    main()
