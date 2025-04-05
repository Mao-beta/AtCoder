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
    UV = EI(N-1)
    G = adjlist(N, UV)

    steps = [-1] * N
    que = deque()
    que.append(0)
    steps[0] = 0
    while que:
        now = que.popleft()
        step = steps[now]
        for goto in G[now]:
            if steps[goto] != -1:
                continue
            que.append(goto)
            steps[goto] = step + 1

    colors = [steps[i] % 2 for i in range(N)]
    E = set()
    for u in range(N):
        for v in range(u+1, N):
            if colors[u] != colors[v]:
                E.add((u, v))
    for u, v in UV:
        u, v = u-1, v-1
        E.discard((u, v))
    # print(E)
    if len(E) % 2:
        print("First", flush=True)
        u, v = E.pop()
        print(u+1, v+1, flush=True)
    else:
        print("Second", flush=True)

    while True:
        u, v = NMI()
        if u == -1 and v == -1:
            return
        E.discard((u-1, v-1))
        u, v = E.pop()
        print(u + 1, v + 1, flush=True)


if __name__ == "__main__":
    main()
