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
    N, M = NMI()
    A = set(NMI())
    B = set(NMI())
    C = A & B
    C = sorted(list(C))
    print(*C)


if __name__ == "__main__":
    main()
