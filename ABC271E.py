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
    N, M, K = NMI()
    ABC = [NLI() for _ in range(M)]
    ABC = [[x-1, y-1, w] for x, y, w in ABC]
    E = NLI()
    E = [x-1 for x in E]
    INF = 10**20
    D = [INF] * N
    D[0] = 0

    for e in E:
        a, b, c = ABC[e]

        nb = min(D[b], D[a]+c)
        D[b] = nb

    print(D[-1] if D[-1] < INF else -1)


if __name__ == "__main__":
    main()
