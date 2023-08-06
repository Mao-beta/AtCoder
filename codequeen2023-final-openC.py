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
EI = lambda m: [NLI() for _ in range(m)]


def adjlist(n, edges, directed=False, in_origin=1):
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
    N, S, T = NMI()
    UV = EI(N-1)
    G = adjlist(N, UV)
    S -= 1
    T -= 1

    def bfs(start):
        steps = [-1] * N
        que = deque()
        que.append(start)
        steps[start] = 0
        while que:
            now = que.popleft()
            step = steps[now]
            for goto in G[now]:
                if steps[goto] != -1:
                    continue
                que.append(goto)
                steps[goto] = step + 1
        return steps

    Ssteps = bfs(S)
    Tsteps = bfs(T)
    ST = Ssteps[T]
    for i in range(N):
        ans = (Ssteps[i] + Tsteps[i] - ST) // 2 + 1
        print(ans)


if __name__ == "__main__":
    main()
