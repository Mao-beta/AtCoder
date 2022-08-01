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
    N, M = NMI()
    UV = [NLI() for _ in range(M)]
    G = [[0]*N for _ in range(N)]
    for u, v in UV:
        G[u - 1][v - 1] = 1
        G[v - 1][u - 1] = 1

    ans = 0
    for a in range(N):
        for b in range(a+1, N):
            for c in range(b+1, N):
                if G[a][b] and G[b][c] and G[c][a]:
                    ans += 1

    print(ans)


if __name__ == "__main__":
    main()
