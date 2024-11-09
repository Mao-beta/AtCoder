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
        self.members = defaultdict(set)

        for i in range(n):
            self.members[i].add(i)

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

        self.members[x] |= self.members[y]
        self.members[y] = set()

        self.par[x] += self.par[y]
        self.par[y] = x

    def size(self, x):
        return -self.par[self.find(x)]

    def get_members(self, x):
        root = self.find(x)
        return self.members[root]

    def get_roots(self):
        return self.roots

    def group_count(self):
        return len(self.roots)

    def all_group_members(self):
        return self.members

    def __repr__(self):
        return '\n'.join('{}: {}'.format(r, self.members[r]) for r in self.roots)


def main():
    H, W = NMI()
    S = [SI() for _ in range(H)]
    red = 0
    uf = UnionFind(H*W)
    for h in range(H):
        for w in range(W):
            i = h * W + w
            if S[h][w] == ".":
                red += 1
                continue
            for dh, dw in zip([1, 0], [0, 1]):
                nh, nw = h+dh, w+dw
                if 0 <= nh < H and 0 <= nw < W:
                    if S[h][w] == S[nh][nw] == "#":
                        ni = nh * W + nw
                        uf.unite(i, ni)
    green = uf.group_num - red
    ans = 0
    for h in range(H):
        for w in range(W):
            i = h * W + w
            if S[h][w] == "#":
                continue
            R = set()
            for dh, dw in zip([1, 0, -1, 0], [0, 1, 0, -1]):
                nh, nw = h+dh, w+dw
                if 0 <= nh < H and 0 <= nw < W:
                    ni = nh * W + nw
                    if S[nh][nw] == ".":
                        continue
                    R.add(uf.find(ni))
            if len(R) == 0:
                ans += green + 1
                continue
            # print(h, w, len(R))
            ans += green - (len(R) - 1)
    print(ans * pow(red, MOD99-2, MOD99) % MOD99)


if __name__ == "__main__":
    main()
