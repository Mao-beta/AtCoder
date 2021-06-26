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
    A, B, C, D = NMI()
    if C*D - B <= 0:
        print(-1)
    else:
        k = A / (C*D-B)
        print(int(math.ceil(k)))


if __name__ == "__main__":
    main()
