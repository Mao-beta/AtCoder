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

from collections import defaultdict


class UnionFind:
    def __init__(self, n, D):
        # 親要素のノード番号を格納　xが根のとき-(サイズ)を格納
        self.par = [-1 for i in range(n)]
        self.n = n
        self.roots = set(range(n))
        self.group_num = n
        self.members = defaultdict(set)
        # 連結成分ごとの残り本数
        self.D = D.copy()
        # 点ごとの残り本数
        self.C = D.copy()
        # Dが1個以上ある点の集合
        self.V = defaultdict(set)

        for i in range(n):
            self.members[i].add(i)
            self.V[i].add(i)

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

    def unite(self, ax, ay):
        x = self.find(ax)
        y = self.find(ay)
        if x == y: return

        # 木のサイズを比較し、小さいほうから大きいほうへつなぐ
        if self.par[x] > self.par[y]:
            x, y = y, x

        self.group_num -= 1
        self.roots.discard(y)
        assert self.group_num == len(self.roots)

        self.members[x] |= self.members[y]
        self.members[y] = set()

        ans_x = self.V[x].pop()
        ans_y = self.V[y].pop()

        self.C[ans_x] -= 1
        self.C[ans_y] -= 1
        if self.C[ans_x] > 0:
            self.V[x].add(ans_x)
        if self.C[ans_y] > 0:
            self.V[y].add(ans_y)

        self.V[x] |= self.V[y]
        self.V[y] = set()

        self.par[x] += self.par[y]
        self.par[y] = x

        self.D[x] += self.D[y] - 2
        self.D[y] = 0

        return ans_x, ans_y


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
    N, M = NMI()
    D = NLI()
    AB = [NLI() for _ in range(M)]

    if sum(D) != 2*N - 2:
        print(-1)
        exit()

    uf = UnionFind(N, D)

    for a, b in AB:
        a, b = a-1, b-1
        if not uf.is_same(a, b):
            uf.unite(a, b)
        else:
            print(-1)
            exit()

    ones = set()
    over = set()
    print(uf.D)
    for r in uf.get_roots():
        if uf.D[r] == 1:
            ones.add(r)
        elif uf.D[r] >= 2:
            over.add(r)
        else:
            print(-1)
            exit()

    ans = []
    for i in range(M+1, N):
        print(uf.V)
        print(ones, over)
        if ones and over:
            x = ones.pop()
            y = over.pop()
            x, y = uf.unite(x, y)
            if uf.D[x]: pass
            ans.append([x+1, y+1])




        elif not over and len(ones) == 2:
            x = ones.pop()
            y = ones.pop()
            x, y = uf.unite(x, y)
            ans.append([x+1, y+1])

    print(*ans)




if __name__ == "__main__":
    main()
