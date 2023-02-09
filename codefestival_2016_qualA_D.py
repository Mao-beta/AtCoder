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


class WeightedUnionFind:
    def __init__(self, n):
        # 親要素のノード番号を格納　xが根のとき-(サイズ)を格納
        self.par = [-1 for i in range(n)]
        self.n = n
        # 根からノードへの重みを管理
        self.weight = [0] * n

    def find(self, x):
        # 根ならその番号を返す
        if self.par[x] < 0:
            return x
        else:
            # 再帰的に累積和を取る
            r = self.find(self.par[x])
            self.weight[x] += self.weight[self.par[x]]
            self.par[x] = r
            return self.par[x]

    def is_same(self, x, y):
        # 根が同じならTrue
        return self.find(x) == self.find(y)

    def get_weight(self, x):
        self.find(x)
        return self.weight[x]

    def diff(self, x, y):
        # xからyへの重み
        return self.get_weight(y) - self.get_weight(x)

    # xからyへの重みはw
    def unite(self, x, y, w=0):
        w = w + self.get_weight(x) - self.get_weight(y)
        x = self.find(x)
        y = self.find(y)

        if x == y: return

        # 木のサイズを比較し、小さいほうから大きいほうへつなぐ
        if -self.par[x] < -self.par[y]:
            x, y = y, x
            w = -w

        self.par[x] += self.par[y]
        self.par[y] = x
        self.weight[y] = w

    def size(self, x):
        return -self.par[self.find(x)]

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def weights(self):
        return self.weight

    def roots(self):
        return [i for i, x in enumerate(self.par) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        res = defaultdict(list)
        for i in range(self.n):
            res[self.find(i)].append(i)
        return res

    def __repr__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())


def main():
    H, W = NMI()
    N = NI()
    uf_h = WeightedUnionFind(H)
    uf_w = WeightedUnionFind(W)
    H2W = [[] for _ in range(H)]
    W2H = [[] for _ in range(W)]
    P = []

    for i in range(N):
        h, w, a = NMI()
        h, w = h-1, w-1
        P.append([h, w, a])
        H2W[h].append([w, a, i])
        W2H[w].append([h, a, i])

    for h in range(H):
        H2W[h].sort()
        for idx in range(len(H2W[h])-1):
            wx, ax, ix = H2W[h][idx]
            wy, ay, iy = H2W[h][idx+1]

            if uf_w.is_same(wx, wy):
                d = uf_w.diff(wx, wy)
                if d != ay-ax:
                    print("No")
                    exit()
            else:
                uf_w.unite(wx, wy, ay-ax)

    for w in range(W):
        W2H[w].sort()
        for idx in range(len(W2H[w]) - 1):
            hx, ax, ix = W2H[w][idx]
            hy, ay, iy = W2H[w][idx + 1]

            if uf_h.is_same(hx, hy):
                d = uf_h.diff(hx, hy)
                if d != ay - ax:
                    print("No")
                    exit()
            else:
                uf_h.unite(hx, hy, ay - ax)

    gm_h = uf_h.all_group_members()
    gm_w = uf_w.all_group_members()
    MH = [0] * H
    MW = [0] * W

    for r, members in gm_h.items():
        if len(members) == 0:
            continue

        weights_h = [uf_h.weight[m] for m in members]
        mh = min(weights_h)
        for m in members:
            MH[m] = mh

    for r, members in gm_w.items():
        if len(members) == 0:
            continue

        weights_w = [uf_w.weight[m] for m in members]
        mw = min(weights_w)
        for m in members:
            MW[m] = mw

    for i, (h, w, a) in enumerate(P):
        if a < uf_h.weight[h] - MH[h] + uf_w.weight[w] - MW[w]:
            print("No")
            exit()

    print("Yes")


if __name__ == "__main__":
    main()
