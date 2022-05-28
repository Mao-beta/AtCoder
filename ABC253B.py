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
    H, W = NMI()
    S = [SI() for _ in range(H)]
    K = []
    for h in range(H):
        for w in range(W):
            if S[h][w] == "o":
                K.append([h, w])

    print(abs(K[0][0] - K[1][0]) + abs(K[0][1] - K[1][1]))


if __name__ == "__main__":
    main()
