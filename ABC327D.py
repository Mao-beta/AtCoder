import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

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


def is_bipartite(N, graph):
    colors = [-1] * N

    def dfs_paint_01_color(start):
        if colors[start] != -1:
            return True

        stack = deque()
        stack.append(start)

        colors[start] = 0

        while stack:
            now = stack.pop()
            c = colors[now]

            for goto in graph[now]:
                if colors[goto] == 1 - c:
                    continue
                elif colors[goto] == c:
                    return False
                stack.append(goto)
                colors[goto] = 1 - c

        return True

    res = True
    for s in range(N):
        res &= dfs_paint_01_color(s)

    return res


def main():
    N, M = NMI()
    A = NLI()
    B = NLI()
    G = [[] for _ in range(N)]

    for a, b in zip(A, B):
        a, b = a-1, b-1
        G[a].append(b)
        G[b].append(a)

    if is_bipartite(N, G):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
