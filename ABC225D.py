import sys
import math
from collections import deque

sys.setrecursionlimit(100000)
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
    N, Q = NMI()
    querys = [NLI() for _ in range(Q)]

    parents = [N] * N
    gotos = [N] * N

    for query in querys:
        t, *p = query
        if t == 1:
            x, y = p
            x, y = x-1, y-1
            parents[y] = x
            gotos[x] = y

        elif t == 2:
            x, y = p
            x, y = x-1, y-1
            parents[y] = N
            gotos[x] = N

        else:
            x = p[0]
            x -= 1
            now = x
            while parents[now] != N:
                now = parents[now]
            ans = []
            while now != N:
                ans.append(now+1)
                now = gotos[now]
            print(len(ans), *ans)



if __name__ == "__main__":
    main()
