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


def cum_2D(_A):
    """
    2次元リストAの累積和
    """
    from copy import deepcopy

    A = deepcopy(_A)
    H = len(A)
    W = len(A[0])
    for h in range(H):
        for w in range(W-1):
            A[h][w+1] += A[h][w]
    for w in range(W):
        for h in range(H-1):
            A[h+1][w] += A[h][w]

    return A


def main():
    N = NI()
    gn = 1005
    grid = [[0] * gn for _ in range(gn)]

    for _ in range(N):
        lx, ly, rx, ry = NMI()
        grid[lx][ly] += 1
        grid[rx][ly] -= 1
        grid[lx][ry] -= 1
        grid[rx][ry] += 1

    imos = cum_2D(grid)
    C = [0] * (N+1)
    for h in range(gn):
        for w in range(gn):
            k = imos[h][w]
            C[k] += 1

    for k in range(1, N+1):
        print(C[k])


if __name__ == "__main__":
    main()
