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
    N = NI()
    A = NLI()
    print(A)
    A = [(a, i+1) for i, a in enumerate(A)]
    print(A)
    A.sort()
    print(A)
    print(A[-2][1])


if __name__ == "__main__":
    main()
