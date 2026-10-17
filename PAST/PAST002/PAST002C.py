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
    T = [SI() for _ in range(N)]
    for i in range(N-2, -1, -1):
        for j in range(0, N*2-1):
            if T[i][j] == ".":
                continue
            if T[i+1][j-1] == "X" or T[i+1][j] == "X" or T[i+1][j+1] == "X":
                T[i] = T[i][:j] + "X" + T[i][j+1:]
    for i in range(N):
        print(T[i])


if __name__ == "__main__":
    main()