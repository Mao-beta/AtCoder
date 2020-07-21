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
    A = sorted(NLI())
    if N % 2:
        for i in range(N):
            if i % 2 == 0 and A[i] == i:
                continue
            elif i % 2 == 1 and A[i] == i + 1:
                continue
            else:
                print(0)
                exit()
        print(pow(2, (N//2), MOD))

    else:
        for i in range(N):
            if i % 2 == 0 and A[i] == i + 1:
                continue
            elif i % 2 == 1 and A[i] == i:
                continue
            else:
                print(0)
                exit()
        print(pow(2, (N//2), MOD))


if __name__ == "__main__":
    main()