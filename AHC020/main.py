import random
import sys
import math
import bisect
import time
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


from collections import defaultdict

class UnionFind:
    def __init__(self, n):
        # 親要素のノード番号を格納　xが根のとき-(サイズ)を格納
        self.par = [-1 for i in range(n)]
        self.n = n
        self.roots = set(range(n))
        self.group_num = n

    def find(self, x):
        # 根ならその番号を返す
        if self.par[x] < 0:
            return x
        else:
            # 親の親は親
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def is_same(self, x, y):
        # 根が同じならTrue
        return self.find(x) == self.find(y)

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y: return

        # 木のサイズを比較し、小さいほうから大きいほうへつなぐ
        if self.par[x] > self.par[y]:
            x, y = y, x

        self.group_num -= 1
        self.roots.discard(y)
        assert self.group_num == len(self.roots)

        self.par[x] += self.par[y]
        self.par[y] = x

    def size(self, x):
        return -self.par[self.find(x)]

    def get_roots(self):
        return self.roots

    def group_count(self):
        return len(self.roots)


def MST(N, _edges, notuse):
    """
    要UnionFind
    N頂点の最小全域木の長さ
    edges = [[u, v, cost], ....] (0-index)
    """
    uf = UnionFind(N)
    edges = [[u, v, w, i] for i, (u, v, w) in enumerate(_edges)]
    edges.sort(key=lambda x: x[2])
    res = 0
    S = set()
    for a, b, c, i in edges:
        if i in notuse:
            continue

        if uf.is_same(a, b):
            continue
        else:
            res += c
            uf.unite(a, b)
            S.add(i)
    return res, uf, S


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
        for i, (u, v, c) in enumerate(edges):
            res[u].append([v, c, i])
            if not directed:
                res[v].append([u, c, i])

    else:
        for u, v in edges:
            res[u].append(v)
            if not directed:
                res[v].append(u)

    return res


def main():
    N, M, K = NMI()
    XY = EI(N)
    UVW = EI(M)
    AB = EI(K)

    START = time.time()


    def calc_cost(P, B):
        res = 0
        for p in P:
            res += p**2
        for b, (u, v, w) in zip(B, UVW):
            res += b * w
        return res

    def calc_score(cost):
        return round(10**6 * (1 + 10**8 / (cost + 10**7)))


    UVW = [[x-1, y-1, w] for x, y, w in UVW]
    G = adjlist(N, UVW, in_origin=0)

    l, uf, edge_S = MST(N, UVW, set())

    B = [0] * M
    for idx in edge_S:
        B[idx] = 1

    Dkn = [[0]*N for _ in range(K)]
    kton_kouho = [set() for _ in range(K)]
    ntok_kouho = [set() for _ in range(N)]
    for n in range(N):
        for k in range(K):
            x, y = XY[n]
            a, b = AB[k]
            d2 = (x-a)**2 + (y-b)**2
            d = int(d2 ** 0.5)
            while d**2 < d2:
                d += 1
            Dkn[k][n] = d
            if d <= 5000:
                kton_kouho[k].add(n)
                ntok_kouho[n].add(k)

    P = [0] * N
    seen = set()
    points = [set() for _ in range(N)]
    casters = [set() for _ in range(K)]
    for k in range(K):
        if k in seen:
            continue
        p = min(Dkn[k])
        n = Dkn[k].index(p)

        if p > P[n]:
            P[n] = p
            x, y = XY[n]
            for kk in ntok_kouho[n]:
                a, b = AB[kk]
                if (x-a)**2 + (y-b)**2 <= p**2:
                    seen.add(kk)
                    points[n].add(kk)
                    casters[kk].add(n)

    cost = calc_cost(P, B)
    score = calc_score(cost)

    print(*P)
    print(*B)

    best_P = P[:]
    best_B = B[:]

    def pgap(p, newp):
        return newp**2 - p**2


    def vanish(tn):

        # tn番目のPを0にして再構成
        rem = points[tn].copy()

        points[tn] = set()
        P[tn] = 0

        needs = set()
        for k in rem:
            casters[k].discard(tn)
            if len(casters[k]) == 0:
                needs.add(k)

        # print(f"vanish {tn} {needs}")
        # print([casters[x] for x in needs])

        for k in needs:
            n = -1
            g = 5001**2
            for tmpn in kton_kouho[k]:
                tmpg = pgap(P[tmpn], Dkn[k][tmpn])
                if tmpg < g and Dkn[k][tmpn] <= 5000:
                    n = tmpn
                    g = tmpg

            # print(k, n, g)

            if n != -1:
                P[n] = max(P[n], Dkn[k][n])
                x, y = XY[n]
                for kk in needs:
                    a, b = AB[kk]
                    if (x - a) ** 2 + (y - b) ** 2 <= P[n] ** 2:
                        points[n].add(kk)
                        casters[kk].add(n)

        # print(needs)
        # print([casters[x] for x in needs])


    while time.time() - START < 1.75:
        vanish(random.randint(0, N-1))
        # target = P.index(max(P))
        # vanish(target)
        tmp_cost = calc_cost(P, B)
        tmp_score = calc_score(tmp_cost)

        if tmp_score > score:
            best_P = P[:]
            best_B = B[:]
            score = tmp_score

        print(*P)
        print(*B)
        # print(tmp_score, score)

    B = best_B[:]
    P = best_P[:]

    # 枝刈り
    stack = deque()
    stack.append(~0)
    stack.append(0)
    order = []
    pars = [N] * N
    targets = [N] * N
    while stack:
        now = stack.pop()
        if now >= 0:
            for g, w, i in G[now]:
                if B[i] == 0:
                    continue
                if g == pars[now]:
                    continue
                stack.append(~g)
                stack.append(g)
                pars[g] = now
                targets[g] = i

        else:
            now = ~now
            order.append(now)

    dims = [0] * N
    for b, (u, v, w) in zip(B, UVW):
        if b:
            dims[u] += 1
            dims[v] += 1

    for x in order:
        if x != 0 and dims[x] == 1 and P[x] == 0:
            B[targets[x]] = 0
            dims[pars[x]] -= 1


    for n in range(N):
        minsize = K
        for x in points[n]:
            minsize = min(minsize, len(casters[x]))
        if minsize > 1:
            P[n] = 0

    tmp_cost = calc_cost(P, B)
    tmp_score = calc_score(tmp_cost)

    best_P = P[:]
    best_B = B[:]
    score = tmp_score

    print(*P)
    print(*B)

    notuse = set()
    for i, (u, v, w) in enumerate(UVW):
        if u == 0 or v == 0:
            continue
        if P[u] == 0 or P[v] == 0:
            notuse.add(i)
    l, uf, edge_S = MST(N, UVW, notuse)
    B = [0] * M
    for idx in edge_S:
        B[idx] = 1

    print(*P)
    print(*B)

    tmp_cost = calc_cost(P, B)
    tmp_score = calc_score(tmp_cost)

    if tmp_score > score:
        best_P = P[:]
        best_B = B[:]
        score = tmp_score

    print(*best_P)
    print(*best_B)


if __name__ == "__main__":
    main()
