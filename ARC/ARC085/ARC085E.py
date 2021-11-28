import sys
import math
from collections import defaultdict
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


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
    N = NI()
    A = NLI()
    V = N + 2
    tree = Dinic(V)
    S = 0
    T = V-1
    ans = 0

    INF = 10**12

    for x, a in enumerate(A, start=1):
        # 割る→R、割らない→B
        # a > 0:
        # 割られないとaもらえる
        # aもらって、割られるとaコスト
        # a < 0:
        # 割られないと|a|コスト
        if a >= 0:
            ans += a
            tree.add_edge(x, T, a)
            #print(f"{x} -> T: cost {a}")
        else:
            tree.add_edge(S, x, abs(a))
            #print(f"S -> {x}: cost {abs(a)}")

        # xを割ったらkxも必ず割る
        # xR ^ kxBのときinfコスト
        for y in range(x*2, N+1, x):
            #print(f"{x} -> {y}: cost inf")
            tree.add_edge(x, y, INF)

    cost = tree.flow(S, T)
    print(ans - cost)


if __name__ == "__main__":
    main()
