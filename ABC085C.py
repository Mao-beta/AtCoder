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
    N, Y = NMI()
    for i in range(N+1):
        for j in range(N+1-i):
            k = N - i - j
            if 10000*i + 5000*j + 1000*k == Y:
                print(i, j, k)
                exit()
    print(-1,-1,-1)


if __name__ == "__main__":
    main()