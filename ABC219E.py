import sys
import math
from collections import deque
from itertools import combinations

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


class UnionFind:
    def __init__(self, n):
        # 親要素のノード番号を格納　xが根のとき-(サイズ)を格納
        self.par = [-1 for i in range(n)]
        self.gnum = n
        self.n = n

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

        self.par[x] += self.par[y]
        self.par[y] = x
        self.gnum -= 1

    def size(self, x):
        return -self.par[self.find(x)]

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.par) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __repr__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())


def main():
    G = [NLI() for _ in range(4)]
    points = set()

    all_points = set()
    for h in range(4):
        for w in range(4):
            all_points.add((h, w))
            if G[h][w]:
                points.add((h, w))

    ans = 0
    for case in range(1<<16):
        uf = UnionFind(16)
        ok = set()
        for i in range(16):
            if (case>>i) & 1:
                ok.add((i//4, i%4))

        if points & ok != points:
            continue

        ng = all_points - ok

        for X, Y in combinations(ok, 2):
            Xi = X[0]*4 + X[1]
            Yi = Y[0]*4 + Y[1]
            if X[0] == Y[0] and abs(X[1] - Y[1]) == 1:
                uf.unite(Xi, Yi)
            elif X[1] == Y[1] and abs(X[0] - Y[0]) == 1:
                uf.unite(Xi, Yi)

        for X, Y in combinations(ng, 2):
            Xi = X[0]*4 + X[1]
            Yi = Y[0]*4 + Y[1]
            if X[0] == Y[0] and abs(X[1] - Y[1]) == 1:
                uf.unite(Xi, Yi)
            elif X[1] == Y[1] and abs(X[0] - Y[0]) == 1:
                uf.unite(Xi, Yi)

        is_bad = False
        for h, w in [(1, 1), (1, 2), (2, 1), (2, 2)]:
            if (h, w) in ok:
                continue
            t = False
            for dh, dw in [(1, 0), (2, 0), (1, 3), (2, 3), (0, 1), (0, 2), (3, 1), (3, 2)]:
                t |= uf.is_same(h*4+w, dh*4+dw)
            if not t:
                is_bad = True

        if is_bad:
            continue

        h, w = ok.pop()
        ok.add((h, w))

        if uf.size(h * 4 + w) == len(ok):
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
