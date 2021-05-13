import sys
import math
from collections import defaultdict
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    H, W = NMI()
    A = [NLI() for _ in range(H)]

    rowsum = [0] * H
    colsum = [0] * W
    for h in range(H):
        for w in range(W):
            a = A[h][w]
            rowsum[h] += a
            colsum[w] += a

    B = [[0]*W for _ in range(H)]
    for h in range(H):
        for w in range(W):
            B[h][w] = rowsum[h] + colsum[w] - A[h][w]

    for h in range(H):
        print(*B[h])


if __name__ == "__main__":
    main()
