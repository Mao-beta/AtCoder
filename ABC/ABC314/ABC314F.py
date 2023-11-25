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
        # 今回のみ 集合が最後に行った試合を表すノードの番号をrootから返す
        self.nodes = list(range(n))

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

    def unite(self, x, y, m):
        # mは試合番号
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

        self.nodes[self.find(x)] = m

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
        return ' '.join('{}: {}'.format(r, self.members[r]) for r in self.roots)


def main():
    N = NI()
    PQ = EI(N-1)
    PQ = [[x-1, y-1] for x, y in PQ]
    uf = UnionFind(N)
    G = [[] for _ in range(2*N-1)]
    E = [0] * (2*N-1)

    for m, (p, q) in enumerate(PQ, start=N):
        rp = uf.find(p)
        rq = uf.find(q)
        G[m].append([uf.nodes[rp], uf.size(rp)])
        G[m].append([uf.nodes[rq], uf.size(rq)])
        uf.unite(p, q, m)
        # print(uf)

    ans = [0] * N
    que = deque()
    que.append([2*N-2, 0])
    # print(G)
    while que:
        now, e = que.popleft()
        # print(now, e, G[now])
        if len(G[now]) == 0:
            ans[now] = e
            continue

        SZ = []
        for goto, sz in G[now]:
            SZ.append(sz)
        a, b = SZ
        ea = a * pow(a+b, MOD99-2, MOD99)
        eb = b * pow(a+b, MOD99-2, MOD99)
        # print(G[now][0], G[now][1])
        que.append([G[now][0][0], (e+ea) % MOD99])
        que.append([G[now][1][0], (e+eb) % MOD99])

    print(*ans)


if __name__ == "__main__":
    main()
