import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.set_int_max_str_digits(10 ** 6)
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


def adjlist(n, edges, directed=False, in_origin=1) -> list[list[int]]:
    if len(edges) == 0:
        return [[] for _ in range(n)]

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
    N = NI()
    XY = EI(N-1)
    XY = [[x-1, y-1] for x, y in XY]
    G = adjlist(N, XY, in_origin=0)
    D = [0] * N
    for x, y in XY:
        D[x] += 1
        D[y] += 1

    steps = [-1] * N
    que = deque()

    for i in range(N):
        if i == 0 or D[i] == 1:
            que.append(i)
            steps[i] = 0

    while que:
        now = que.popleft()
        step = steps[now]
        for goto in G[now]:
            if steps[goto] != -1:
                continue
            que.append(goto)
            steps[goto] = step + 1

    print(*steps, sep="\n")


if __name__ == "__main__":
    main()
