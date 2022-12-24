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
    G = adjlist(N, AB, directed=True)


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

    INF = 10**10
    min_l = INF
    min_ab = [-1, -1]

    steps = []

    for s in range(N):
        steps.append(bfs(s))

    for a, b in AB:
        a, b = a-1, b-1

        l = steps[b][a]
        if l == -1:
            continue

        if l < min_l:
            min_l = l
            min_ab = [a, b]

    # print(min_l, min_ab)

    if min_l == INF:
        print(-1)
        exit()

    print(min_l+1)
    a, b = min_ab

    rev_AB = [[b, a] for a, b in AB]
    R = adjlist(N, rev_AB, directed=True)

    steps_b = steps[b]
    # print(steps_b)
    now = a
    ans = [now+1]
    while steps_b[now] > 0:
        for goto in R[now]:
            if steps_b[goto] == steps_b[now] - 1:
                now = goto
                ans.append(goto+1)
                break

    ans.sort()
    print(*ans, sep="\n")


def _main():
    N, M = NMI()
    AB = EI(M)
    G = adjlist(N, AB, directed=True)
    # print(G)

    P = []
    seen = [-1] * N
    used = [0] * N
    ans_len = [10**10]
    ans = [[]]

    def dfs(now):
        P.append(now+1)
        seen[now] = len(P) - 1
        used[now] = 1
        # print(now+1, P)

        for goto in G[now]:
            # print("goto", goto+1)
            if seen[goto] >= 0:
                idx = seen[goto]
                if len(P)-idx < ans_len[0]:
                    # print(idx, goto+1, P[idx:])
                    ans_len[0] = len(P) - idx
                    ans[0] = P[idx:]
                continue

            dfs(goto)

        seen[now] = -1
        P.pop()
        # print("out", now+1)

    for s in range(N):
        if used[s]:
            continue
        # print(s)
        dfs(s)

    if ans_len[0] == 10**10:
        print(-1)
        exit()

    print(ans_len[0])
    print(*ans[0], sep="\n")


if __name__ == "__main__":
    main()
