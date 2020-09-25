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


INF = 10 ** 20
class Dinic:
    """
    最大流(Dinic)
    ※2部マッチングなどで行き先を再現するときはlinks[i][0]==0のものを探す
    """


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
    N = NI()
    A = [NI() for _ in range(N)]
    s, t = 2*N, 2*N+1
    din = Dinic(2*N+2)
    for i in range(N):
        din.add_link(s, i, 1)
        din.add_link(i+N, t, 1)
        hate = A[i]
        for j in range(N):
            if j == hate: continue
            din.add_link(i, j+N, 1)
    if din.max_flow(s, t) != N:
        print(-1)
        exit()

    for i in range(N):
        for cap, to, _ in din.links[i]:
            if cap == 0:
                print(to - N)


if __name__ == "__main__":
    main()