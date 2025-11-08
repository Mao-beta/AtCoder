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
    N, M = NMI()
    UV = EI(M)
    G = adjlist(N, UV)
    S = SI()

    def f(start, now, step):
        return start * N * N + now * N + step

    def g(sns):
        start, ns = divmod(sns, N*N)
        now, step = divmod(ns, N)
        return start, now, step

    def fs(start, step):
        if start == -1:
            return -1
        else:
            return start * N + step

    def gs(ss):
        if ss == -1:
            return -1, -1
        else:
            return divmod(ss, N)

    steps = [fs(-1, -1) for _ in range(N)]
    steps2 = [fs(-1, -1) for _ in range(N)]
    que = deque()
    for i, s in enumerate(S):
        if s == "S":
            que.append(f(i, i, 0))
            steps[i] = fs(i, 0)
    while que:
        start, now, step = g(que.popleft())
        for goto in G[now]:
            if gs(steps2[goto])[1] != -1:
                continue
            if gs(steps[goto])[1] == -1:
                steps[goto] = fs(start, step+1)
                que.append(f(start, goto, step + 1))
            else:
                if gs(steps[goto])[0] == start:
                    continue
                steps2[goto] = fs(start, step+1)
                que.append(f(start, goto, step + 1))
    # print(steps)
    # print(steps2)
    ans = []
    for i, s in enumerate(S):
        if s == "D":
            ans.append(gs(steps[i])[1] + gs(steps2[i])[1])

    ans = "\n".join(map(str, ans))
    print(ans)


if __name__ == "__main__":
    main()
