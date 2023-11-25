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
EI = lambda m: [NLI() for _ in range(m)]


def main():
    H, W, N = NMI()
    AB = EI(N)
    INF = 5000
    D = [[INF]*(W+1) for _ in range(H+1)]
    for a, b in AB:
        a, b = a-1, b-1
        D[a][b] = 0
    for h in range(H+1):
        D[h][W] = 0
    for w in range(W+1):
        D[H][w] = 0
    
    DH = [0, 1, 1]
    DW = [1, 0, 1]
    for h in range(H-1, -1, -1):
        for w in range(W-1, -1, -1):
            for dh, dw in zip(DH, DW):
                D[h][w] = min(D[h][w], D[h+dh][w+dw]+1)

    ans = 0
    for h in range(H):
        for w in range(W):
            ans += D[h][w]

    print(ans)


if __name__ == "__main__":
    main()
