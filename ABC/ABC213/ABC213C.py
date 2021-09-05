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


def compress(S):
    """ 座標圧縮 """

    S = set(S)
    zipped, unzipped = {}, {}
    for i, a in enumerate(sorted(S)):
        zipped[a] = i
        unzipped[i] = a
    return zipped, unzipped


def main():
    H, W, N = NMI()
    A = []
    B = []
    for _ in range(N):
        a, b = NMI()
        A.append(a)
        B.append(b)

    zipA, unzipA = compress(A)
    zipB, unzipB = compress(B)

    for a, b in zip(A, B):
        print(zipA[a]+1, zipB[b]+1)


if __name__ == "__main__":
    main()
