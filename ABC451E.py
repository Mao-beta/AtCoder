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


class LCATree:
    __slots__ = ("n", "root", "LOG", "adj", "parent", "depth")

    def __init__(self, n, edges, root=0):
        """
        :param n: 0-index
        :param edges: 0-index
        :param root: default 0
        """
        self.n = n
        self.root = root
        self.LOG = n.bit_length()

        adj = [[] for _ in range(n)]
        for u, v, a in edges:
            adj[u].append(v)
            adj[v].append(u)
        self.adj = adj

        parent = [[-1] * n for _ in range(self.LOG)]
        depth = [-1] * n
        self.parent = parent
        self.depth = depth

        # DFS iterative（list stack）: depth=-1 を visited として使う
        stack = [root]
        depth[root] = 0
        while stack:
            v = stack.pop()
            for to in adj[v]:
                if depth[to] != -1:
                    continue
                parent[0][to] = v
                depth[to] = depth[v] + 1
                stack.append(to)

        # doubling
        for k in range(1, self.LOG):
            pk = parent[k - 1]
            ck = parent[k]
            for v in range(n):
                p = pk[v]
                ck[v] = -1 if p == -1 else pk[p]

    def lca(self, a, b):
        parent = self.parent
        depth = self.depth
        if depth[a] < depth[b]:
            a, b = b, a

        # lift a to depth[b]
        diff = depth[a] - depth[b]
        k = 0
        while diff:
            if diff & 1:
                a = parent[k][a]
            diff >>= 1
            k += 1

        if a == b:
            return a

        for k in range(self.LOG - 1, -1, -1):
            pa = parent[k][a]
            pb = parent[k][b]
            if pa != pb:
                a, b = pa, pb
        return parent[0][a]

    def dist(self, a, b):
        c = self.lca(a, b)
        d = self.depth
        return d[a] + d[b] - 2 * d[c]


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

    def group_count(self):
        return len(self.roots)


def MST(N, edges):
    """
    要UnionFind
    N頂点の最小全域木の辺
    edges = [[u, v, cost], ....] (0-index)
    """
    uf = UnionFind(N)
    edges.sort(key=lambda x: x[-1])
    res = []
    for a, b, c in edges:
        if uf.is_same(a, b):
            continue
        else:
            res.append([a, b, c])
            uf.unite(a, b)
        if uf.group_num == 1:
            break
    return res


def adjlist(n, edges, directed=False, in_origin=1) -> list[list[int]]:
    if len(edges) == 0:
        return [[] for _ in range(n)]

    weighted = True if len(edges[0]) > 2 else False
    if in_origin == 1:
        if weighted:
            edges = [[x-1, y-1, w] for x, y, w in edges]
        else:
            edges = [[x-1, y-1] for x, y in edges]

    res = [[] for _ in range(n)]

    if weighted:
        for u, v, c in edges:
            res[u].append([v, c])
            if not directed:
                res[v].append([u, c])

    else:
        for u, v in edges:
            res[u].append(v)
            if not directed:
                res[v].append(u)

    return res

def main():
    N = NI()
    UVA = []
    for u in range(N-1):
        for v, a in enumerate(NLI(), start=u+1):
            UVA.append([u, v, a])
    edges = MST(N, UVA)
    LCA = LCATree(N, edges)
    G = adjlist(N, edges, in_origin=0)

    steps = [-1] * N
    que = deque()
    que.append(0)
    steps[0] = 0
    while que:
        now = que.popleft()
        step = steps[now]
        for goto, a in G[now]:
            if steps[goto] != -1:
                continue
            que.append(goto)
            steps[goto] = step + a

    for u, v, a in UVA:
        lca = LCA.lca(u, v)
        d = steps[u] + steps[v] - 2 * steps[lca]
        if d != a:
            print("No")
            return
    print("Yes")


if __name__ == "__main__":
    main()
