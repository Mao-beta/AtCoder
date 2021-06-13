import sys
import math
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()

INF = 10 ** 20
class Dinic:
    """ 最大流(Dinic) """


    def __init__(self, n):
        self.n = n
        self.links = [[] for _ in range(n)]
        self.depth = None
        self.progress = None

    def add_link(self, _from, to, cap):
        self.links[_from].append([cap, to, len(self.links[to])])
        self.links[to].append([0, _from, len(self.links[_from]) - 1])

    def bfs(self, s):
        from collections import deque

        depth = [-1] * self.n
        depth[s] = 0
        q = deque([s])
        while q:
            v = q.popleft()
            for cap, to, rev in self.links[v]:
                if cap > 0 and depth[to] < 0:
                    depth[to] = depth[v] + 1
                    q.append(to)
        self.depth = depth

    def dfs(self, v, t, flow):
        if v == t:
            return flow
        links_v = self.links[v]
        for i in range(self.progress[v], len(links_v)):
            self.progress[v] = i
            cap, to, rev = link = links_v[i]
            if cap == 0 or self.depth[v] >= self.depth[to]:
                continue
            d = self.dfs(to, t, min(flow, cap))
            if d == 0:
                continue
            link[0] -= d
            self.links[to][rev][0] += d
            return d
        return 0

    def max_flow(self, s, t):
        flow = 0
        while True:
            self.bfs(s)
            if self.depth[t] < 0:
                return flow
            self.progress = [0] * self.n
            current_flow = self.dfs(s, t, INF)
            while current_flow > 0:
                flow += current_flow
                current_flow = self.dfs(s, t, INF)


def main():
    H, W, N = NMI()
    P = [NLI() for _ in range(N)]

    tree = Dinic(H + W + 2*N + 2 + H + W)
    S = H+W+N+N
    T = S+1
    for i in range(H):
        tree.add_link(S, i, 1)
    for i in range(W):
        tree.add_link(H+i, T, 1)
    for i in range(N):
        tree.add_link(H+W+i, H+W+N+i, 1)

    for i, (a, b, c, d) in enumerate(P):
        a, b, c, d = a-1, b-1, c-1, d-1
        for h in range(a, c+1):
            tree.add_link(h, H+W+i, 1)
        for w in range(b, d+1):
            tree.add_link(H+W+N+i, H+w, 1)


    print(tree.max_flow(S, T))




if __name__ == "__main__":
    main()
