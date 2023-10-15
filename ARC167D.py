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


from sortedcontainers import SortedSet

def solve(N, P):
    P = [x-1 for x in P]
    R = [0] * N

    uf = UnionFind(N)

    for x in range(N):
        uf.unite(x, P[x])
        R[P[x]] = x

    if uf.group_num == 1:
        return [p+1 for p in P]

    # 各連結成分のなかでもう見た個数
    C = Counter()

    # 各連結成分における最小値の集合
    MM = SortedSet()
    # 各連結成分における最小値の辞書とその逆
    M = defaultdict(lambda: N+1)
    RM = defaultdict(lambda: N + 1)

    for r in uf.roots:
        m = min(uf.members[r])
        MM.add(m)
        M[r] = m
        RM[m] = r

    # print("mins", MM, "M", M)

    for i in range(N):
        p = P[i]
        r = uf.find(i)
        m = M[r]
        C[r] += 1
        c = C[r]

        # 他の連結成分のうち最小のもの
        if not uf.is_same(MM[0], i):
            target = MM[0]
        else:
            target = MM[1]

        if C[r] < uf.size(r) and target > p:
            continue

        tr = RM[target]
        tidx = R[target]
        tc = C[tr]

        # print("swap", i+1, P[i]+1, tidx+1, P[tidx]+1)
        P[i], P[tidx] = P[tidx], P[i]
        R[p], R[target] = R[target], R[p]
        uf.unite(p, target)
        nr = uf.find(p)

        MM.discard(m)
        MM.discard(target)
        MM.add(min(m, target))

        # print(M, P, uf, r, tr, target)
        del M[r]
        del M[tr]
        M[nr] = min(m, target)

        del RM[m]
        del RM[target]
        RM[min(m, target)] = nr

        del C[r]
        del C[tr]
        C[nr] = c + tc

        if len(MM) <= 1:
            break

    return [p+1 for p in P]


def main():
    T = NI()
    for _ in range(T):
        N = NI()
        P = NLI()
        ans = solve(N, P)
        print(*ans)


if __name__ == "__main__":
    main()
