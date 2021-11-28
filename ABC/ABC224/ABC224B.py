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
    H, W = NMI()
    A = [NLI() for _ in range(H)]
    for i1 in range(H):
        for i2 in range(i1+1, H):
            for j1 in range(W):
                for j2 in range(j1+1, W):
                    if A[i1][j1] + A[i2][j2] > A[i2][j1] + A[i1][j2]:
                        print("No")
                        exit()
    print("Yes")


if __name__ == "__main__":
    main()
