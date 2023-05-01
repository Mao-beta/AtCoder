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
    N, M = NMI()
    AB = EI(M)
    G = adjlist(N, AB)
    AB = [[x-1, y-1] for x, y in AB]
    D = [[0]*N for _ in range(N)]
    for a, b in AB:
        D[a][b] = 1
        D[b][a] = 1


    def is_case_valid(case):
        for a, b in AB:
            if ((case >> a) & 1) & ((case >> b) & 1):
                return False
        return True

    ans = 0

    for case in range(1<<N):
        if not is_case_valid(case):
            continue

        ans_case = 1
        colors = [-1] * N

        for s in range(N):
            if colors[s] >= 0:
                continue
            if (case >> s) & 1:
                continue

            # dfs
            stack = deque([s])
            colors[s] = 0
            tmp = 2
            while stack:
                now = stack.pop()
                for goto in G[now]:
                    if (case >> goto) & 1:
                        continue
                    if colors[goto] == colors[now]:
                        tmp = 0
                        continue
                    if colors[goto] == 1 - colors[now]:
                        continue
                    colors[goto] = 1 - colors[now]
                    stack.append(goto)

            ans_case *= tmp

        ans += ans_case

    print(ans)


if __name__ == "__main__":
    main()
