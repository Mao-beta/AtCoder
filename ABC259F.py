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
    N = NI()
    D = NLI()
    edges = [NLI() for _ in range(N-1)]
    graph = adjlist(N, edges)

    INF = 10**15

    P = [N] * N
    # dp1/dp2: 子のうち[d個以下で選ぶ/d個未満で選ぶ]ときの、i以下の部分木の重みの総和の最大値
    dp1 = [0] * N
    dp2 = [0] * N

    def rec(now):
        # print("now", now)
        # 子への辺を選ばない→選ぶに変更したときの重みの差
        gaps = []
        # 子への辺を1本も選ばないときの重みの総和
        base = 0

        for goto, w in graph[now]:
            if goto == P[now]: continue

            P[goto] = now
            rec(goto)

            base += dp1[goto]

            # 子への辺を選ぶとき dp2[goto] + w
            # 選ばないとき dp1[goto]
            gap = dp2[goto] + w - dp1[goto]
            gaps.append(gap)

        gaps.sort(reverse=True)

        dp1[now] = base
        dp2[now] = base

        # print(now, D[now], base, graph[now])

        cnt = 0
        for gap in gaps:
            if gap < 0:
                break
            base += gap
            cnt += 1
            if cnt < D[now]:
                dp2[now] = max(dp2[now], base)
            if cnt <= D[now]:
                dp1[now] = max(dp1[now], base)

        # print(base)

        if D[now] == 0:
            dp2[now] = -INF

        # print(dp1)
        # print(dp2)
        # print("end", now)

    rec(0)
    # print(dp1)
    # print(dp2)
    print(max(dp1[0], dp2[0]))


if __name__ == "__main__":
    main()
