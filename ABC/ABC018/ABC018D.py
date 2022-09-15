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
    N, M, P, Q, R = NMI()
    XYZ = [NLI() for _ in range(R)]
    XYZ = [[x-1, y-1, w] for x, y, w in XYZ]
    G = [[] for _ in range(N)]
    for x, y, z in XYZ:
        G[x].append([y, z])

    ans = 0
    for X in combinations(range(N), P):
        tmp = [0] * M
        for x in X:
            for y, z in G[x]:
                tmp[y] += z
        tmp.sort()
        ans = max(ans, sum(tmp[-Q:]))
    print(ans)


if __name__ == "__main__":
    main()
