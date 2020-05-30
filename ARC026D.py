import sys
import math
import copy
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def make_grid(h, w, num): return [[int(num)] * w for _ in range(h)]


#隣接リスト 1-order
def make_adjlist_nond(n, edges):
    res = [[] for _ in range(n + 1)]
    for edge in edges:
        res[edge[0]].append(edge[1])
        res[edge[1]].append(edge[0])
    return res


def make_adjlist_d(n, edges):
    res = [[] for _ in range(n + 1)]
    for edge in edges:
        res[edge[0]].append(edge[1])
    return res


#nCr
def cmb(n, r):
    return math.factorial(n) // math.factorial(r) // math.factorial(n - r)


def main():
    N, M = NMI()
    roads = [NLI() + [0] for _ in range(M)]

    ng = 0
    ok = 10**12

    for _ in range(100):
        mid = (ng+ok) / 2
        for i, road in enumerate(roads):
            roads[i][4] = mid*road[3] - road[2]

        tmp_roads = sorted(roads, key=lambda x: x[4], reverse=True)
        union = UnionFind(N)
        ans = 0
        for edge in tmp_roads:
            x, y, t, c, budget = edge
            if not union.is_same(x, y) or budget > 0:
                union.unite(x, y)
                ans += budget

        if ans >= 0:
            ok = mid
        else:
            ng = mid

    print(ok)



class UnionFind():
    def __init__(self, n):
        #親要素のノード番号を格納　xが根のとき-(サイズ)を格納
        self.par = [-1 for i in range(n)]
        self.n = n

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
        if x == y: return

        #木のサイズを比較し、小さいほうから大きいほうへつなぐ
        if self.par[x] > self.par[y]:
            x, y = y, x

        self.par[x] += self.par[y]
        self.par[y] = x

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

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())


if __name__ == "__main__":
    main()