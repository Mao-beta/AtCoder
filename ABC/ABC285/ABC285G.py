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

# ACL_maxflow(Dinic)
from typing import NamedTuple, Optional, List, cast


class MFGraph:
    class Edge(NamedTuple):
        src: int
        dst: int
        cap: int
        flow: int

    class _Edge:
        def __init__(self, dst: int, cap: int) -> None:
            self.dst = dst
            self.cap = cap
            self.rev: Optional[MFGraph._Edge] = None

    def __init__(self, n: int) -> None:
        self._n = n
        self._g: List[List[MFGraph._Edge]] = [[] for _ in range(n)]
        self._edges: List[MFGraph._Edge] = []

    def add_edge(self, src: int, dst: int, cap: int) -> int:
        assert 0 <= src < self._n
        assert 0 <= dst < self._n
        assert 0 <= cap
        m = len(self._edges)
        e = MFGraph._Edge(dst, cap)
        re = MFGraph._Edge(src, 0)
        e.rev = re
        re.rev = e
        self._g[src].append(e)
        self._g[dst].append(re)
        self._edges.append(e)
        return m

    def get_edge(self, i: int) -> Edge:
        assert 0 <= i < len(self._edges)
        e = self._edges[i]
        re = cast(MFGraph._Edge, e.rev)
        return MFGraph.Edge(
            re.dst,
            e.dst,
            e.cap + re.cap,
            re.cap
        )

    def edges(self) -> List[Edge]:
        return [self.get_edge(i) for i in range(len(self._edges))]

    def change_edge(self, i: int, new_cap: int, new_flow: int) -> None:
        assert 0 <= i < len(self._edges)
        assert 0 <= new_flow <= new_cap
        e = self._edges[i]
        e.cap = new_cap - new_flow
        assert e.rev is not None
        e.rev.cap = new_flow

    def flow(self, s: int, t: int, flow_limit: Optional[int] = None) -> int:
        assert 0 <= s < self._n
        assert 0 <= t < self._n
        assert s != t
        if flow_limit is None:
            flow_limit = cast(int, sum(e.cap for e in self._g[s]))

        current_edge = [0] * self._n
        level = [0] * self._n

        def fill(arr: List[int], value: int) -> None:
            for i in range(len(arr)):
                arr[i] = value

        def bfs() -> bool:
            fill(level, self._n)
            queue = []
            q_front = 0
            queue.append(s)
            level[s] = 0
            while q_front < len(queue):
                v = queue[q_front]
                q_front += 1
                next_level = level[v] + 1
                for e in self._g[v]:
                    if e.cap == 0 or level[e.dst] <= next_level:
                        continue
                    level[e.dst] = next_level
                    if e.dst == t:
                        return True
                    queue.append(e.dst)
            return False

        def dfs(lim: int) -> int:
            stack = []
            edge_stack: List[MFGraph._Edge] = []
            stack.append(t)
            while stack:
                v = stack[-1]
                if v == s:
                    flow = min(lim, min(e.cap for e in edge_stack))
                    for e in edge_stack:
                        e.cap -= flow
                        assert e.rev is not None
                        e.rev.cap += flow
                    return flow
                next_level = level[v] - 1
                while current_edge[v] < len(self._g[v]):
                    e = self._g[v][current_edge[v]]
                    re = cast(MFGraph._Edge, e.rev)
                    if level[e.dst] != next_level or re.cap == 0:
                        current_edge[v] += 1
                        continue
                    stack.append(e.dst)
                    edge_stack.append(re)
                    break
                else:
                    stack.pop()
                    if edge_stack:
                        edge_stack.pop()
                    level[v] = self._n
            return 0

        flow = 0
        while flow < flow_limit:
            if not bfs():
                break
            fill(current_edge, 0)
            while flow < flow_limit:
                f = dfs(flow_limit - flow)
                flow += f
                if f == 0:
                    break
        return flow

    def min_cut(self, s: int) -> List[bool]:
        visited = [False] * self._n
        stack = [s]
        visited[s] = True
        while stack:
            v = stack.pop()
            for e in self._g[v]:
                if e.cap > 0 and not visited[e.dst]:
                    visited[e.dst] = True
                    stack.append(e.dst)
        return visited


def main():
    # 解説AC
    H, W = NMI()
    C = [SI() for _ in range(H)]

    def f(h, w):
        return h*W+w

    G = MFGraph(H*W+4)
    S = H*W
    T = S+1
    Sd = S+2
    Td = S+3

    DH = [0, 0, 1, -1]
    DW = [1, -1, 0, 0]

    for h in range(H):
        for w in range(W):
            ca = C[h][w]
            a = f(h, w)

            if ca == "1":
                continue

            # 左
            if (h+w) % 2:
                if ca == "2":
                    # 絶対使いたい辺
                    G.add_edge(Sd, a, 1)
                else:
                    G.add_edge(S, a, 1)

                for dh, dw in zip(DH, DW):
                    nh, nw = h+dh, w+dw
                    if not(0 <= nh < H and 0 <= nw < W):
                        continue
                    cb = C[nh][nw]
                    if cb == "1":
                        continue
                    b = f(nh, nw)
                    G.add_edge(a, b, 1)

            # 右
            else:
                if ca == "2":
                    # 絶対使いたい辺
                    G.add_edge(a, Td, 1)
                else:
                    G.add_edge(a, T, 1)


    # 絶対使いたいところから流す
    G.flow(Sd, Td)
    G.flow(Sd, T)
    G.flow(S, Td)
    G.flow(S, T)

    # 絶対使いたい辺を使っているか確認
    E = G.edges()
    for e in E:
        # print(Sd, Td, e)
        if e.src == Sd and e.flow != e.cap:
            print("No")
            exit()
        if e.dst == Td and e.flow != e.cap:
            print("No")
            exit()

    print("Yes")


if __name__ == "__main__":
    main()