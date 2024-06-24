import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.set_int_max_str_digits(10 ** 6)
MOD = 10 ** 9 + 7
MOD99 = 998244353

input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: tuple(NMI())
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
    AB = EI(N-1)
    G = adjlist(N, AB)

    # 重心分解を進めながら問題をとく。d(<=logN)ステップ行う
    # depth[v]: vが重心になるときの重心木の深さ（最初の重心の深さが0）
    depth = [N] * N

    # TODO: 高速化
    # ある重心木についてsubtree-size dpしながら次の重心を求める

    subtree = [0] * N
    parents = [N] * N
    starts = deque()
    totals = deque()
    steps = deque()
    starts.append(0)
    totals.append(N)
    steps.append(0)

    prevd = 0

    while starts:
        d = steps.popleft()
        s = starts.popleft()
        total = totals.popleft()

        if d != prevd:
            for i in range(N):
                parents[i] = N
            prevd = d

        stack = deque()
        stack.append(~s)
        stack.append(s)
        # centroid = s
        while stack:
            now = stack.pop()
            # print(now if now >= 0 else ~now)
            if now >= 0:
                for g in G[now]:
                    if g == parents[now]:
                        continue
                    if depth[g] < d:
                        continue
                    parents[g] = now
                    stack.append(~g)
                    stack.append(g)
            else:
                now = ~now
                is_centroid = True
                sub = 1
                for g in G[now]:
                    if g == parents[now]:
                        continue
                    if depth[g] < d:
                        continue
                    if subtree[g] > total // 2:
                        is_centroid = False
                    sub += subtree[g]
                subtree[now] = sub
                subpar = total - sub
                if subpar > total // 2:
                    is_centroid = False

                # 重心を見つけたので次の始点とサイズを保存
                if is_centroid:
                    centroid = now
                    depth[centroid] = d
                    for g in G[centroid]:
                        if depth[g] < d:
                            continue
                        if g == parents[centroid]:
                            if subpar == 1:
                                depth[g] = d+1
                            else:
                                starts.append(g)
                                totals.append(subpar)
                                steps.append(d+1)
                            continue
                        if subtree[g] == 1:
                            depth[g] = d+1
                        else:
                            starts.append(g)
                            totals.append(subtree[g])
                            steps.append(d+1)
                    break

            # print("#", d, s, total)
            # print(parents)
            # print(subtree)
            # print(depth)
            # print(centroid, starts[d+1])
    print(" ".join([chr(ord("A")+x) for x in depth]))



if __name__ == "__main__":
    main()

