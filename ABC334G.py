import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

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


from collections import deque
class LowLink:
    def __init__(self, N, G):
        self.N = N
        self.G = G
        self.order = [N] * N
        self.low = [N] * N
        self.pars = [N] * N
        self.finish = [0] * N
        self.roots = set()
        # self.dfs_tree = [[] for _ in range(N)]
        self.disjoints = [0] * N
        self.is_articular = [0] * N
        self.build()

    def dfs(self, root):
        self.roots.add(root)
        stack = deque()
        stack.append(~root)
        stack.append(root)
        t = 0

        while stack:
            now = stack.pop()
            if self.finish[max(now, ~now)]:
                continue

            if now >= 0:
                if self.order[now] < t:
                    continue

                self.order[now] = t
                self.low[now] = self.order[now]
                t += 1
                for v in self.G[now]:
                    if v == self.pars[now]:
                        continue
                    if self.order[v] < self.N:
                        self.low[now] = min(self.low[now], self.order[v])
                    else:
                        self.pars[v] = now
                        stack.append(~v)
                        stack.append(v)

            else:
                now = ~now

                if now == root and self.disjoints[now] >= 2:
                    self.is_articular[now] = 1
                elif now != root and self.disjoints[now] >= 1:
                    self.is_articular[now] = 1

                if now != root:
                    par = self.pars[now]
                    self.low[par] = min(self.low[par], self.low[now])

                    if self.order[par] <= self.low[now]:
                        self.disjoints[par] += 1

                self.finish[now] = 1

    def build(self):
        for i in range(self.N):
            if not self.finish[i]:
                self.dfs(i)

        # for i, p in enumerate(self.pars):
        #     if i >= self.N or p >= self.N:
        #         continue
        #     self.dfs_tree[i].append(p)
        #     self.dfs_tree[p].append(i)

    def articularion_points(self):
        return [i for i, v in enumerate(self.is_articular) if v]


def main():
    H, W = NMI()
    S = [SI() for _ in range(H)]
    # uf = UnionFind(H*W)
    DH = [0, 1]
    DW = [1, 0]

    def f(h, w):
        return h * W + w

    def rf(idx):
        return divmod(idx, W)

    red = 0
    G = [[] for _ in range(H*W)]

    for idx in range(H*W):
        h, w = rf(idx)
        s = S[h][w]
        if s == ".":
            red += 1
            continue
        for dh, dw in zip(DH, DW):
            nh, nw = h + dh, w + dw
            if 0 <= nh < H and 0 <= nw < W:
                nidx = f(nh, nw)
                t = S[nh][nw]
                if s == t == "#":
                    G[idx].append(nidx)
                    G[nidx].append(idx)

    lowlink = LowLink(H*W, G)

    base = len(lowlink.roots) - red
    ans = 0
    for idx in range(H*W):
        h, w = rf(idx)
        s = S[h][w]
        if s == ".":
            continue
        if idx in lowlink.roots:
            ans += base - 1 + lowlink.disjoints[idx]
        else:
            ans += base - 1 + lowlink.disjoints[idx] + 1

    green = H*W - red
    print(ans * pow(green, MOD99-2, MOD99) % MOD99)


if __name__ == "__main__":
    main()
