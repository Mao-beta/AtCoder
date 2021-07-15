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
    N, X = NMI()
    A = NLI()
    S = sum(A) - (N//2)
    print("Yes" if X >= S else "No")


if __name__ == "__main__":
    main()
