import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.set_int_max_str_digits(10**6)
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


def compress(S):
    """ 座標圧縮 """

    S = set(S)
    zipped, unzipped = {}, {}
    for i, a in enumerate(sorted(S)):
        zipped[a] = i
        unzipped[i] = a
    return zipped, unzipped


def is_bipartite(N, graph):
    colors = [-1] * N
    ans = [1]

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
                    ans[0] = 0
                    return False
                stack.append(goto)
                colors[goto] = 1 - c

        if len(graph[start]) == 0:
            ans[0] *= 2
            ans[0] %= MOD99
        return True

    res = True
    for s in range(N):
        res &= dfs_paint_01_color(s)

    return ans[0]


def main():
    N, Q = NMI()
    PV = EI(Q)
    S = [v for _, v in PV] + [0]
    Z, UZ = compress(S)
    PV = [[p-1, Z[v]] for p, v in PV]
    ZN = len(Z)
    G = [[] for _ in range(Q)]
    Max = [0] * N
    for i, (p, v) in enumerate(PV):
        if Max[p] > v:
            print(0)
            return
        Max[p] = max(Max[p], v)
        for j in range(i):
            pp, vv = PV[j]
            if vv > v:
                G[i].append(j)
                G[j].append(i)
    ans = is_bipartite(Q, G)

    print(ans)


if __name__ == "__main__":
    main()
