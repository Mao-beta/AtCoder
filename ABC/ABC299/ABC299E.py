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
    UV = EI(M)
    G = adjlist(N, UV)
    K = NI()
    PD = EI(K)
    PD.sort(key=lambda x: (-x[1]))
    ans = [1] * N

    def bfs(start, d):
        steps = [-1] * N
        que = deque()
        que.append(start)
        steps[start] = 0
        while que:
            now = que.popleft()
            step = steps[now]
            if step >= d:
                return
            else:
                ans[now] = 0
            for goto in G[now]:
                if steps[goto] != -1:
                    continue
                que.append(goto)
                steps[goto] = step + 1


    def check(start, d):
        steps = [-1] * N
        que = deque()
        que.append(start)
        steps[start] = 0
        while que:
            now = que.popleft()
            step = steps[now]
            if step == d and ans[now] == 1:
                return True
            if step > d:
                return False

            for goto in G[now]:
                if steps[goto] != -1:
                    continue
                que.append(goto)
                steps[goto] = step + 1

        return False

    for p, d in PD:
        p -= 1
        bfs(p, d)

    if 1 not in ans:
        print("No")
    else:
        for p, d in PD:
            p -= 1
            res = check(p, d)
            if not res:
                print("No")
                exit()

        print("Yes")
        print(*ans, sep="")


if __name__ == "__main__":
    main()
