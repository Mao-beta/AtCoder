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
    N, K = NMI()
    A = NLI()
    B = NLI()
    C = [abs(a-b) for a, b in zip(A, B)]
    s = sum(C)
    if K >= s and (K-s) % 2 == 0:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
