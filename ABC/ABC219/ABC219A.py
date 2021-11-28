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
    X = NI()
    if X < 40:
        print(40-X)
    elif X < 70:
        print(70-X)
    elif X < 90:
        print(90-X)
    else:
        print("expert")


if __name__ == "__main__":
    main()
