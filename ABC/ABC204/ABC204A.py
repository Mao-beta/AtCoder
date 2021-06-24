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
    x, y = NMI()
    if x == y:
        print(x)
    else:
        S = set([0, 1, 2])
        S.discard(x)
        S.discard(y)
        print(S.pop())


if __name__ == "__main__":
    main()
