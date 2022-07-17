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
    S, T, M = NMI()
    UV = [NLI() for _ in range(M)]

    E = [[] for _ in range(S+1)]
    for u, v in UV:
        E[u].append(v-1-S)

    M = [[-1]*T for _ in range(T)]

    for z in range(1, S+1):
        for x in E[z]:
            for y in E[z]:
                if x == y: continue
                if M[x][y] == -1:
                    M[x][y] = z
                else:
                    print(x+1+S, y+1+S, z, M[x][y])
                    exit()

    print(-1)


if __name__ == "__main__":
    main()
