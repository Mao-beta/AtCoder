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


def dist2(x1, y1, x2, y2):
    return (x1-x2)**2 + (y1-y2)**2


def ConvexHull(xy):
    def NG(x, y):
        x0, y0 = res[-2]
        x1, y1 = res[-1]
        return (x-x0)*(y1-y0)-(x1-x0)*(y-y0) >= 0

    res = []
    xy.sort()
    for x, y in xy:
        while len(res) > 1 and NG(x, y): res.pop()
        res.append((x, y))
    under_n = len(res)
    for x, y in xy[-2::-1]:
        while len(res) > under_n and NG(x, y): res.pop()
        res.append((x, y))
    return res[:-1]

def RotatingCalipers(xy):
    def dist(i, j):
        ix, iy = xy[i]
        jx, jy = xy[j]
        return (ix-jx)**2+(iy-jy)**2

    def vec(i):
        x0, y0 = xy[i]
        x1, y1 = xy[(i+1)%n]
        return x1-x0, y1-y0

    def outer(i, j):
        vix, viy = vec(i)
        vjx, vjy = vec(j)
        return vix*vjy-viy*vjx

    n = len(xy)
    if n < 2: return 0
    if n == 2: return dist(0, 1)**0.5
    res = 0
    i = xy.index(min(xy))
    j = xy.index(max(xy))
    si, sj = i, j
    while i != sj or j != si:
        res = max(res, dist(i, j))
        if outer(i, j) > 0: j = (j+1)%n
        else: i = (i+1)%n
    return res**0.5


def main():
    N = NI()
    XY = EI(N)
    XY = [[x+10000, y+10000] for x, y in XY]

    if N == 0:
        print(1)
        return
    if N == 1:
        print(2)
        return

    # B[x][y]: Xi//10 = x, Yi//10 = y となる点のリスト
    B = [[[] for _ in range(2001)] for _ in range(2001)]
    for i, (x, y) in enumerate(XY):
        B[x//10][y//10].append([x, y, i])

    # Bの8近傍+自身のみ通信可能か探索
    DX = [0, 1, 1, 1]
    DY = [1, 0, 1, -1]

    uf = UnionFind(N)

    for bx in range(2001):
        for by in range(2001):
            Bxy = B[bx][by]
            if len(Bxy) == 0:
                continue
            # 自身
            for x1, y1, i1 in Bxy:
                for x2, y2, i2 in Bxy:
                    if dist2(x1, y1, x2, y2) <= 100:
                        uf.unite(i1, i2)
            # 8近傍
            for dx, dy in zip(DX, DY):
                nbx = bx + dx
                nby = by + dy
                if 0 <= nbx < 2001 and 0 <= nby < 2001:
                    for x1, y1, i1 in Bxy:
                        for x2, y2, i2 in B[nbx][nby]:
                            if dist2(x1, y1, x2, y2) <= 100:
                                uf.unite(i1, i2)

    # 凸包
    groups = [uf.find(i) for i in range(N)]
    members = [[] for _ in range(N)]
    for i, g in enumerate(groups):
        members[g].append(i)

    ans = 0
    for r, M in enumerate(members):
        if len(M) <= 1:
            continue
        Vs = [XY[i] for i in M]
        Vs = ConvexHull(Vs)
        d = RotatingCalipers(Vs)
        ans = max(ans, d)

    print(ans+2)


if __name__ == "__main__":
    main()
