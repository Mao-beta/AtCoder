import sys
import math
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def make_grid(h, w, num): return [[int(num)] * w for _ in range(h)]


class UnionFind:
    def __init__(self, n):
        #親要素のノード番号を格納　xが根のとき-(サイズ)を格納
        self.par = [-1 for i in range(n)]
        self.n = n
        self.e = [0 for i in range(n)]

    def find(self, x):
        #根ならその番号を返す
        if self.par[x] < 0:
            return x
        else:
            #親の親は親
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def is_same(self, x, y):
        #根が同じならTrue
        return self.find(x) == self.find(y)

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            self.e[x] += 1
            return

        #木のサイズを比較し、小さいほうから大きいほうへつなぐ
        if self.par[x] > self.par[y]:
            x, y = y, x

        self.par[x] += self.par[y]
        self.par[y] = x
        self.e[x] += self.e[y] + 1

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


def compress(S):
    """ 座標圧縮 """

    zipped, unzipped = {}, {}
    for i, a in enumerate(S):
        zipped[a] = i
        unzipped[i] = a
    return zipped, unzipped


def main():
    N = NI()
    cards = [NLI() for _ in range(N)]
    cards = [[a-1, b-1] for a, b in cards]

    S = set()
    for a, b in cards:
        S.add(a)
        S.add(b)
    zipped, unzipped = compress(S)

    cards = [[zipped[a], zipped[b]] for a, b in cards]

    tree = UnionFind(len(zipped))
    for a, b in cards:
        tree.unite(a, b)

    gm = tree.roots()

    ans = 0
    for r in gm:
        s = tree.size(r)
        e = tree.e[r]
        ans += min(s, e)

    print(ans)

if __name__ == "__main__":
    main()
