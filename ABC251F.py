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


def adjlist_nond_1to0(n, edges):
    res = [[] for _ in range(n)]
    for a, b in edges:
        a, b = a - 1, b - 1
        res[a].append(b)
        res[b].append(a)
    return res



def main():
    N, M = NMI()
    edges = [NLI() for _ in range(M)]
    graph = adjlist_nond_1to0(N, edges)

    T = []
    seen = [0] * N

    def rec(now, par):
        if now != 0:
            T.append([now+1, par+1])
        seen[now] = 1

        for goto in graph[now]:
            if goto == par:
                continue
            if seen[goto]:
                continue

            rec(goto, now)

    rec(0, N)
    for x, y in T:
        print(x, y)


    T = []
    seen = [0] * N
    D = deque()
    D.append(0)
    seen[0] = 1
    P = [N] * N

    while D:
        now = D.popleft()
        for goto in graph[now]:
            if seen[goto]:
                continue
            D.append(goto)
            P[goto] = now
            seen[goto] = 1
            T.append([now + 1, goto + 1])

    for x, y in T:
        print(x, y)


if __name__ == "__main__":
    main()
