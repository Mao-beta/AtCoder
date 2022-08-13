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


def adjlist(n, edges, directed=False, in_origin=1):
    weighted = True if len(edges[0]) > 2 else False
    if in_origin == 1:
        if weighted:
            edges = [[x-1, y-1, w] for x, y, w in edges]
        else:
            edges = [[x-1, y-1] for x, y in edges]

    res = [[] for _ in range(n)]

    if weighted:
        for u, v, c in edges:
            res[u].append([v, c])
            if not directed:
                res[v].append([u, c])

    else:
        for u, v in edges:
            res[u].append(v)
            if not directed:
                res[v].append(u)

    return res


def main():
    N, M, v = NMI()
    ABC = [NLI() for _ in range(M)]
    G = adjlist(N, ABC, directed=True)
    print(*G, sep="\n")
    print()
    BAC = [[b, a, c] for a, b, c in ABC]
    RG = adjlist(N, BAC, directed=True)
    print(*RG, sep="\n")

    # fin[i][v] i(先手0 後手1)が頂点vから始めたときに有限回で終了するか？(0:無限 / 1:有限)
    fin = [[0]*N for _ in range(2)]

    out_dims = [len(l) for l in G]

    que = deque()
    for v in range(N):
        if out_dims[v] == 0:
            que.append(v)
            fin[0][v] = 1
            fin[1][v] = 1

    seen = [0] * N
    while que:
        now = que.popleft()
        if seen[now]: continue
        seen[now] = 1

        print(now)
        for goto, c in RG[now]:
            if not seen[goto]:
                que.append(goto)

        if len(G[now]) == 0:
            fin[0][now] = 1
            fin[1][now] = 1
            continue

        # Taka: finが一個でもあれば1
        ones = [fin[1][goto] == 1 for goto, c in G[now]]
        fin[0][now] = int(any(ones))

        # Aoki: 全部finなら1
        ones = [fin[0][goto] == 1 for goto, c in G[now]]
        fin[1][now] = int(all(ones))

    print(*fin, sep="\n")



if __name__ == "__main__":
    main()
