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
        return {r: self.members(r) for r in self.roots()}

    def __repr__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())


def main():
    N, Q = NMI()
    wuf = WeightedUnionFind(N)
    for _ in range(Q):
        query = NLI()
        if query[0] == 0:
            _, x, y, z = query
            wuf.unite(x, y, z)
        else:
            _, x, y = query
            if wuf.is_same(x, y):
                print(wuf.diff(x, y))
            else:
                print("?")


if __name__ == "__main__":
    main()
