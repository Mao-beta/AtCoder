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
    N, M = NMI()
    P = EI(N)
    C = EI(M)
    D = [[0]*(N+M) for _ in range(N+M)]
    E = []
    
    def euc(xi, yi, xj, yj):
        return math.sqrt((xi-xj)**2 + (yi-yj)**2)
    
    def euc2(xi, yi, xj, yj):
        return (xi-xj)**2 + (yi-yj)**2
    
    
    def calc_dist(i, j):
        if i < N and j < N:
            xi, yi = P[i]
            xj, yj = P[j]
            d = euc(xi, yi, xj, yj)
        elif i < N and j >= N:
            xi, yi = P[i]
            xj, yj, rj = C[j-N]
            d = abs(euc(xi, yi, xj, yj) - rj)
        else:
            xi, yi, ri = C[i-N]
            xj, yj, rj = C[j-N]
            e2 = euc2(xi, yi, xj, yj)
            if e2 > (ri+rj)**2:
                d = math.sqrt(e2) - (ri+rj)
            elif e2 < (ri-rj)**2:
                d = abs(ri-rj) - math.sqrt(e2)
            else:
                d = 0
        
        return d
    
    
    for i in range(N+M):
        for j in range(i+1, N+M):
            d = calc_dist(i, j)
            D[i][j] = d
            D[j][i] = d
            E.append((d, i, j))

    E.sort()
    INF = 10**20
    ans = INF
    for case in range(1<<M):
        tmp = 0
        S = set(range(N))
        for j in range(M):
            if (case >> j) & 1:
                S.add(j+N)

        uf = UnionFind(N+M)

        for d, i, j in E:
            if i not in S or j not in S:
                continue
            if uf.is_same(i, j):
                continue
            uf.unite(i, j)
            tmp += D[i][j]

        ans = min(ans, tmp)

    print(ans)


if __name__ == "__main__":
    main()
