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
    E = {}

    if weighted:
        for u, v, c in edges:
            res[u].append([v, c])
            if not directed:
                res[v].append([u, c])

    else:
        for i, (u, v) in enumerate(edges, start=1):
            if u > v:
                u, v = v, u
            E[(u, v)] = i
            res[u].append(v)
            if not directed:
                res[v].append(u)

    return res, E


def main():
    N, M, K = NMI()
    UV = EI(M)

    if K == 0:
        print("Yes")
        print(0)
        print()
        return

    if M == 0:
        print("No")
        return

    if K % 2:
        print("No")
        return

    G, E = adjlist(N, UV)

    # 全点見終わるまで連結成分ごとにDFS
    # 各成分においてサイズSとするとS//2*2個までは必ず光る

    seen = [0] * N
    total = [0]
    ans = []
    lamp = [0] * N
    pars = [N] * N

    def dfs(start):
        if seen[start]:
            return
        D = deque()
        D.append(~start)
        D.append(start)
        seen[start] = 1

        while D:
            now = D.pop()
            if now >= 0:
                for g in G[now]:
                    if seen[g]:
                        continue
                    D.append(~g)
                    D.append(g)
                    seen[g] = 1
                    pars[g] = now

            else:
                now = ~now
                par = pars[now]
                if par == N:
                    continue

                u, v = now, par
                if u > v:
                    u, v = v, u
                e = E[(u, v)]
                if lamp[now]:
                    continue

                if lamp[par] == 0:
                    total[0] += 2

                lamp[now] = 1
                lamp[par] ^= 1
                ans.append(e)

                if total[0] == K:
                    print("Yes")
                    print(len(ans))
                    print(*ans)
                    exit()

    for s in range(N):
        dfs(s)

    print("No")


if __name__ == "__main__":
    main()
