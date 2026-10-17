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


def make_grid(h, w, num): return [[int(num)] * w for _ in range(h)]


def main():
    N = NI()
    A = [0] + NLI()
    for x in range(1, N+1):
        j = 1
        i = x
        while A[i] != x:
            i = A[i]
            j += 1
        print(j, end=" ")


if __name__ == "__main__":
    main()