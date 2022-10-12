import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
MOD99 = 998244353

input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()
SMI = lambda: input().split()
SLI = lambda: list(SMI())


def main():
    H, W, K = NMI()
    S = [SI() for _ in range(H)]
    A = [[0]*W for _ in range(H)]

    x = 1
    Hs = []
    for h in range(H):
        Hs.append(h)
        cnt = S[h].count("#")
        if cnt == 0:
            continue

        Ws = []
        for w in range(W):
            Ws.append(w)

            if S[h][w] == ".":
                continue

            for ah in Hs:
                for aw in Ws:
                    A[ah][aw] = x

            x += 1
            Ws = []

        Hs = []

    for h in range(H):
        if A[h][0] == 0:
            for w in range(W):
                A[h][w] = A[h-1][w]

        else:
            for w in range(W):
                if A[h][w] == 0:
                    A[h][w] = A[h][w-1]


    for row in A:
        print(*row)


if __name__ == "__main__":
    main()
