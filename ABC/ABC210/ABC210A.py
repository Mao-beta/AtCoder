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
    N, A, X, Y = NMI()
    if N > A:
        print(X*A + Y*(N-A))
    else:
        print(N*X)


if __name__ == "__main__":
    main()
