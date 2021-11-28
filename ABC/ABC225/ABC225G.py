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


INF = 10 ** 10


class Dinic:
    __slots__ = ["n", "graph", "level", "it"]

    class Edge:
        def __init__(self, to, cap, rev=None):
            self.to = to
            self.cap = cap
            self.rev = rev

    def __init__(self, n):
        self.n = n
        self.graph = [[] for i in range(n)]
        self.level = [self.n] * self.n
        self.it = [0] * self.n

    def add_edge(self, fr, to, cap=1):
        forward = self.Edge(to, cap, None)
        forward.rev = backward = self.Edge(fr, 0, forward)
        self.graph[fr].append(forward)
        self.graph[to].append(backward)

    def bfs(self, s, t):
        graph = self.graph

        for i in range(self.n):
            self.level[i] = self.n

        level = self.level
        q = deque([s])
        level[s] = 0
        while q:
            x = q.popleft()
            lx = level[x] + 1
            for e in graph[x]:
                y = e.to
                if e.cap and level[y] > lx:
                    level[y] = lx
                    if y == t:
                        return True
                    q.append(y)
        return False

    def dfs(self, s, t, f):
        graph = self.graph
        level = self.level
        it = self.it
        q = deque([t])
        while q:
            x = q[-1]
            if x == s:
                q.pop()
                for y in q:
                    cap = graph[y][it[y]].rev.cap
                    if cap < f:
                        f = cap
                for y in q:
                    e = graph[y][it[y]]
                    e.cap += f
                    e.rev.cap -= f
                return f
            lx = level[x] - 1
            while it[x] < len(graph[x]):
                e = graph[x][it[x]]
                y = e.to
                rev = e.rev
                if rev.cap == 0 or lx != level[y]:
                    it[x] += 1
                    continue
                q.append(y)
                break
            if it[x] == len(graph[x]):
                q.pop()
                level[x] = self.n
        return 0

    def flow(self, s, t):
        flow = 0
        while self.bfs(s, t):
            for i in range(self.n):
                self.it[i] = 0
            f = self.dfs(s, t, float("inf"))
            while f:
                flow += f
                f = self.dfs(s, t, float("inf"))
        return flow


def main():
    """愚直？解"""
    H, W, C = NMI()
    A = [NLI() for _ in range(H)]

    def hw2v(h, w):
        return h * W + w

    V = H * W * 3 + 2
    tree = Dinic(V)
    S = V - 1
    T = V - 2

    ans = 0
    Z = H * W

    for h in range(H):
        for w in range(W):
            v = hw2v(h, w)
            a = A[h][w]
            score = a - 2 * C

            if score >= 0:
                ans += abs(score)
                tree.add_edge(S, v, abs(score))
            else:
                tree.add_edge(v, T, abs(score))

            for dh, dw in [[1, 1], [-1, 1]]:
                nh, nw = h + dh, w + dw
                if nh < 0 or nh >= H or nw < 0 or nw >= W:
                    continue

                nv = hw2v(nh, nw)

                # S->Z: C, Z->X: inf, Z->Y: inf
                ans += C
                tree.add_edge(S, Z, C)
                tree.add_edge(Z, v, INF)
                tree.add_edge(Z, nv, INF)
                Z += 1

    ans -= tree.flow(S, T)
    print(ans)


def _main():
    """
    writer解
    """
    H, W, C = NMI()
    A = [NLI() for _ in range(H)]

    def hw2v(h, w):
        return h * W + w

    V = H*W + 2
    tree = Dinic(V)
    S = V-1
    T = V-2

    ans = 0

    for h in range(H):
        for w in range(W):
            v = hw2v(h, w)
            a = A[h][w]

            ans += a
            tree.add_edge(S, v, a)

            if h == H-1 or w == W-1:
                tree.add_edge(v, T, C)
            else:
                nv = hw2v(h + 1, w + 1)
                tree.add_edge(v, nv, C)

            if h == H-1 or w == 0:
                tree.add_edge(v, T, C)
            else:
                nv = hw2v(h + 1, w - 1)
                tree.add_edge(v, nv, C)

    ans -= tree.flow(S, T)
    print(ans)


if __name__ == "__main__":
    main()
