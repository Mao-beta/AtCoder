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
    N, Q = NMI()
    querys = EI(Q)
    uf = UnionFind(N)
    P = [N] * (N+1)
    x = 0
    for a, b, c in querys:
        A = 1 + (a * (1 + x) % MOD99) % 2
        B = 1 + (b * (1 + x) % MOD99) % N
        C = 1 + (c * (1 + x) % MOD99) % N
        # print(A, B, C)
        u, v = B-1, C-1

        if A == 1:
            szu = uf.size(u)
            szv = uf.size(v)
            if szu > szv:
                u, v = v, u
            now = u
            D = [v, u]
            while now < N:
                # print(now)
                D.append(P[now])
                now = P[now]
            # print("unite", u, v)
            # szu = uf.size(u)
            # szv = uf.size(v)
            # print(f"{u}size:{szu}, {v}size:{szv}")
            for i in range(1, len(D)-1):
                # print(f"{D[i-1]}<-{D[i]}")
                P[D[i]] = D[i-1]
            uf.unite(u, v)
            # print(P)
        else:
            if not uf.is_same(u, v):
                res = 0
            elif P[u] == P[v] and P[u] < N:
                res = P[u]+1
            elif P[P[u]] == v:
                res = P[u]+1
            elif P[P[v]] == u:
                res = P[v]+1
            else:
                res = 0
            # print("ans")
            print(res)
            x = res


if __name__ == "__main__":
    main()
