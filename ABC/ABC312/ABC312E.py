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
    N = NI()
    C = EI(N)
    G = [[[-1]*105 for _ in range(105)] for _ in range(105)]

    for i, (x1, y1, z1, x2, y2, z2) in enumerate(C):
        for x in range(x1, x2):
            for y in range(y1, y2):
                for z in range(z1, z2):
                    G[x][y][z] = i

    D = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    S = [set() for _ in range(N)]
    for x in range(100):
        for y in range(100):
            for z in range(100):
                i = G[x][y][z]
                if i == -1:
                    continue
                for dx, dy, dz in D:
                    j = G[x+dx][y+dy][z+dz]
                    if j == -1:
                        continue
                    if i == j:
                        continue
                    S[i].add(j)
                    S[j].add(i)

    for s in S:
        print(len(s))


if __name__ == "__main__":
    main()
