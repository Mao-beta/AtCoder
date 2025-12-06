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
    N, X, Y = NMI()
    CAB = [SLI() for _ in range(N)]
    P = [(0, X, 0, Y)]
    for c, a, b in CAB:
        a, b = int(a), int(b)
        P2 = []
        if c == "X":
            for l, r, d, u in P:
                if l < a < r:
                    P2.append((l, a, d-b, u-b))
                    P2.append((a, r, d+b, u+b))
                elif a <= l:
                    P2.append((l, r, d+b, u+b))
                else:
                    P2.append((l, r, d-b, u-b))
        else:
            for l, r, d, u in P:
                if d < a < u:
                    P2.append((l-b, r-b, d, a))
                    P2.append((l+b, r+b, a, u))
                elif a <= d:
                    P2.append((l+b, r+b, d, u))
                else:
                    P2.append((l-b, r-b, d, u))
        P = P2

    uf = UnionFind(len(P))
    PN = len(P)
    idx = {p: i for i, p in enumerate(P)}
    for i in range(PN):
        for j in range(i+1, PN):
            l, r, d, u = P[i]
            l2, r2, d2, u2 = P[j]
            if not(r <= l2 or r2 <= l) and (u == d2 or u2 == d):
                uf.unite(i, j)
            if not(u <= d2 or u2 <= d) and (r == l2 or r2 == l):
                uf.unite(i, j)

    print(uf.group_count())
    ans = []
    for r in uf.roots:
        mems = uf.members[r]
        # print(mems)
        tmp = 0
        for m in mems:
            l, r, d, u = P[m]
            tmp += (r-l) * (u-d)
        ans.append(tmp)
    ans.sort()
    print(*ans)


if __name__ == "__main__":
    main()
