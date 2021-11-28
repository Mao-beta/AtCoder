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
    X = SI()
    a, b = X.split(".")
    a = int(a)
    if int(b[0]) >= 5:
        a += 1
    print(a)


if __name__ == "__main__":
    main()
