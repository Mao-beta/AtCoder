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
    __slots__ = ("n", "root", "LOG", "adj", "parent", "depth", "sz")

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
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        self.adj = adj

        parent = [[-1] * n for _ in range(self.LOG)]
        depth = [-1] * n
        sz = [1] * n
        self.parent = parent
        self.depth = depth
        self.sz = sz

        # DFS iterative（list stack）: depth=-1 を visited として使う
        stack = [~root, root]
        depth[root] = 0
        while stack:
            v = stack.pop()
            if v >= 0:
                for to in adj[v]:
                    if depth[to] != -1:
                        continue
                    parent[0][to] = v
                    depth[to] = depth[v] + 1
                    stack.append(~to)
                    stack.append(to)

            else:
                v = ~v
                p = parent[0][v]
                if v > 0:
                    sz[p] += sz[v]

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



def main():
    N = NI()
    UV = EI(N-1)
    tree = LCATree(N, UV)
    x, y = 0, 0
    ans = 0
    xc = 0
    for m in range(1, N+1):
        if x == y == 0:
            # mex1以上の個数は、0を含むパスの個数
            ans += N * (N-1) // 2 + N
            for c in tree.adj[0]:
                ans -= tree.sz[c] * (tree.sz[c]-1) // 2 + tree.sz[c]
                if tree.lca(1, c) == c:
                    xc = c
            x = m

        elif y == 0:
            # x～0のパスを含むパス
            ans += tree.sz[x] * (N - tree.sz[xc])
            if m >= N:
                break

            if tree.lca(m, x) == x:
                x = m
            elif tree.lca(m, x) == m:
                pass
            elif tree.lca(m, x) == 0:
                y = m
            else:
                break

        else:
            ans += tree.sz[x] * tree.sz[y]
            if m >= N:
                break

            if tree.lca(m, x) == x:
                x = m
            elif tree.lca(m, x) == m:
                pass
            elif tree.lca(m, y) == y:
                y = m
            elif tree.lca(m, y) == m:
                pass
            else:
                break

        # print(m, ans)

    print(ans)


if __name__ == "__main__":
    main()
