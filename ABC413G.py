import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.set_int_max_str_digits(10**6)
sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
MOD99 = 998244353

input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: tuple(NMI())
SI = lambda: input()
SMI = lambda: input().split()
SLI = lambda: tuple(SMI())
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


def compress(S):
    """ 座標圧縮 """

    S = set(S)
    zipped, unzipped = {}, {}
    for i, a in enumerate(S):
        zipped[a] = i
        unzipped[i] = a
    return zipped, unzipped


def main():
    H, W, K = NMI()

    def f(h, w):
        return h * (W+2) + w

    RC = [f(*NLI()) for _ in range(K)]
    #0   ..###
    #1   .   .
    #H+1 ###..
    for h in range(2, H+2):
        RC.append(f(h, 0))
    for h in range(H):
        RC.append(f(h, W+1))
    for w in range(2, W+2):
        RC.append(f(0, w))
    for w in range(W):
        RC.append(f(H+1, w))
    S = set(RC)
    Z, UZ = compress(S)
    uf = UnionFind(len(S))
    for rc in RC:
        r, c = divmod(rc, W+2)
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
            nr, nc = r+dr, c+dc
            if nr < 0 or nr >= H+2 or nc < 0 or nc >= W+2:
                continue
            if f(nr, nc) not in S:
                continue
            uf.unite(Z[f(nr, nc)], Z[f(r, c)])
    x = Z[f(H+1, 0)]
    y = Z[f(0, W+1)]
    if not uf.is_same(x, y):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
