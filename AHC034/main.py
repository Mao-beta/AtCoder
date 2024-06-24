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


def zigzag():
    N = NI()
    H = EI(N)
    ans = []
    # ジグザグ2往復
    now = 0
    for h in range(N):
        if h % 2 == 0:
            for w in range(N):
                if H[h][w] > 0:
                    ans.append(f"+{H[h][w]}")
                    now += H[h][w]
                    H[h][w] = 0
                elif now > 0:
                    d = min(abs(H[h][w]), now)
                    if d > 0:
                        ans.append(f"-{d}")
                        now -= d
                        H[h][w] += d
                if w < N-1:
                    ans.append("R")
                elif h < N-1:
                    ans.append("D")
        else:
            for w in range(N-1, -1, -1):
                if H[h][w] > 0:
                    ans.append(f"+{H[h][w]}")
                    now += H[h][w]
                    H[h][w] = 0
                elif now > 0:
                    d = min(abs(H[h][w]), now)
                    if d > 0:
                        ans.append(f"-{d}")
                        now -= d
                        H[h][w] += d
                if w > 0:
                    ans.append("L")
                elif h < N-1:
                    ans.append("D")

    for h in range(N-1, -1, -1):
        if h % 2 == 1:
            for w in range(N):
                if H[h][w] > 0:
                    ans.append(f"+{H[h][w]}")
                    now += H[h][w]
                    H[h][w] = 0
                elif now > 0:
                    d = min(abs(H[h][w]), now)
                    if d > 0:
                        ans.append(f"-{d}")
                        now -= d
                        H[h][w] += d
                if w < N-1:
                    ans.append("R")
                elif 0 < h:
                    ans.append("U")
        else:
            for w in range(N-1, -1, -1):
                if H[h][w] > 0:
                    ans.append(f"+{H[h][w]}")
                    now += H[h][w]
                    H[h][w] = 0
                elif now > 0:
                    d = min(abs(H[h][w]), now)
                    if d > 0:
                        ans.append(f"-{d}")
                        now -= d
                        H[h][w] += d
                if w > 0:
                    ans.append("L")
                elif 0 < h:
                    ans.append("U")

    print(*ans, sep="\n")


import heapq
from typing import NamedTuple, Optional, List, Tuple, cast


class MCFGraph:
    class Edge(NamedTuple):
        src: int
        dst: int
        cap: int
        flow: int
        cost: int

    class _Edge:
        def __init__(self, dst: int, cap: int, cost: int) -> None:
            self.dst = dst
            self.cap = cap
            self.cost = cost
            self.rev: Optional[MCFGraph._Edge] = None

    def __init__(self, n: int) -> None:
        self._n = n
        self._g: List[List[MCFGraph._Edge]] = [[] for _ in range(n)]
        self._edges: List[MCFGraph._Edge] = []

    def add_edge(self, src: int, dst: int, cap: int, cost: int) -> int:
        assert 0 <= src < self._n
        assert 0 <= dst < self._n
        assert 0 <= cap
        m = len(self._edges)
        e = MCFGraph._Edge(dst, cap, cost)
        re = MCFGraph._Edge(src, 0, -cost)
        e.rev = re
        re.rev = e
        self._g[src].append(e)
        self._g[dst].append(re)
        self._edges.append(e)
        return m

    def get_edge(self, i: int) -> Edge:
        assert 0 <= i < len(self._edges)
        e = self._edges[i]
        re = cast(MCFGraph._Edge, e.rev)
        return MCFGraph.Edge(
            re.dst,
            e.dst,
            e.cap + re.cap,
            re.cap,
            e.cost
        )

    def edges(self) -> List[Edge]:
        return [self.get_edge(i) for i in range(len(self._edges))]

    def flow(self, s: int, t: int,
             flow_limit: Optional[int] = None) -> Tuple[int, int]:
        return self.slope(s, t, flow_limit)[-1]

    def slope(self, s: int, t: int,
              flow_limit: Optional[int] = None) -> List[Tuple[int, int]]:
        assert 0 <= s < self._n
        assert 0 <= t < self._n
        assert s != t
        if flow_limit is None:
            flow_limit = cast(int, sum(e.cap for e in self._g[s]))

        dual = [0] * self._n
        prev: List[Optional[Tuple[int, MCFGraph._Edge]]] = [None] * self._n

        def refine_dual() -> bool:
            pq = [(0, s)]
            visited = [False] * self._n
            dist: List[Optional[int]] = [None] * self._n
            dist[s] = 0
            while pq:
                dist_v, v = heapq.heappop(pq)
                if visited[v]:
                    continue
                visited[v] = True
                if v == t:
                    break
                dual_v = dual[v]
                for e in self._g[v]:
                    w = e.dst
                    if visited[w] or e.cap == 0:
                        continue
                    reduced_cost = e.cost - dual[w] + dual_v
                    new_dist = dist_v + reduced_cost
                    dist_w = dist[w]
                    if dist_w is None or new_dist < dist_w:
                        dist[w] = new_dist
                        prev[w] = v, e
                        heapq.heappush(pq, (new_dist, w))
            else:
                return False
            dist_t = dist[t]
            for v in range(self._n):
                if visited[v]:
                    dual[v] -= cast(int, dist_t) - cast(int, dist[v])
            return True

        flow = 0
        cost = 0
        prev_cost_per_flow: Optional[int] = None
        result = [(flow, cost)]
        while flow < flow_limit:
            if not refine_dual():
                break
            f = flow_limit - flow
            v = t
            while prev[v] is not None:
                u, e = cast(Tuple[int, MCFGraph._Edge], prev[v])
                f = min(f, e.cap)
                v = u
            v = t
            while prev[v] is not None:
                u, e = cast(Tuple[int, MCFGraph._Edge], prev[v])
                e.cap -= f
                assert e.rev is not None
                e.rev.cap += f
                v = u
            c = -dual[s]
            flow += f
            cost += f * c
            if c == prev_cost_per_flow:
                result.pop()
            result.append((flow, cost))
            prev_cost_per_flow = c
        return result


def MCF():
    N = NI()
    H = EI(N)
    ans = []

    # 負をみつけたらちょうど取りに行って帰ってきて埋める
    # 最小費用流？
    # (i, j): i*N+j (+400)
    G = MCFGraph(802)
    S = 800
    T = S+1
    for x in range(400):
        xi, xj = divmod(x, N)
        hx = H[xi][xj]
        if hx > 0:
            G.add_edge(S, x, hx, 0)
        else:
            G.add_edge(x+400, T, abs(hx), 0)

        for y in range(400):
            yi, yj = divmod(y, N)
            hy = H[yi][yj]
            d = abs(xi-yi) + abs(xj-yj)
            if hx > 0 and hy < 0:
                G.add_edge(x, y+400, hx, d)


    def move(s, t):
        si, sj = divmod(s, N)
        ti, tj = divmod(t, N)
        while si < ti:
            ans.append("D")
            si += 1
        while si > ti:
            ans.append("U")
            si -= 1
        while sj < tj:
            ans.append("R")
            sj += 1
        while sj > tj:
            ans.append("L")
            sj -= 1

    def load(x):
        ans.append(f"+{x}")

    def put(x):
        ans.append(f"-{x}")


    f = G.flow(S, T)
    E = [e for e in G.edges() if e.flow and e.src != S and e.dst != T]
    idx2df = [[] for _ in range(400)]
    for e in E:
        idx2df[e.src].append([e.dst-400, e.flow])

    now = 0
    for src in range(400):
        if len(idx2df[src]) == 0:
            continue
        srci, srcj = divmod(src, N)
        move(now, src)
        now = src
        load(H[srci][srcj])
        H[srci][srcj] = 0
        for dst, flow in idx2df[src]:
            dsti, dstj = divmod(dst, N)
            move(now, dst)
            now = dst
            put(flow)
            H[dsti][dstj] += flow

    # print(f)
    # num = 0
    # now = 0
    # for e in G.edges():
    #     if e.flow and e.src != S and e.dst != T:
    #         srci, srcj = divmod(e.src, N)
    #         dsti, dstj = divmod(e.dst-400, N)
    #         move(now, e.src)
    #         load(e.flow)
    #         H[srci][srcj] -= e.flow
    #         move(e.src, e.dst-400)
    #         put(e.flow)
    #         H[dsti][dstj] += e.flow
    #         now = e.dst-400
    #         num += 1

    print(*ans, sep="\n")


def main():
    N = NI()
    H = EI(N)
    ans = []

    def move(si, sj, ti, tj):
        while si < ti:
            ans.append("D")
            si += 1
        while si > ti:
            ans.append("U")
            si -= 1
        while sj < tj:
            ans.append("R")
            sj += 1
        while sj > tj:
            ans.append("L")
            sj -= 1

    def load(x):
        ans.append(f"+{x}")

    def put(x):
        ans.append(f"-{x}")

    finished = [0] * N

    def decide_row(v):
        gap = 10**10
        res = N
        for i in range(N):
            s = sum(H[i]) + v
            if finished[i]:
                continue
            if s < 0:
                continue
            if s < gap:
                gap = s
                res = i
        return res

    def play(i, v):
        for j in range(N):
            if H[i][j] > 0:
                load(H[i][j])
                v += H[i][j]
                H[i][j] = 0
            elif v > 0:
                d = min(abs(H[i][j]), v)
                if d > 0:
                    put(d)
                    v -= d
                    H[i][j] += d
            if j < N-1:
                ans.append("R")

        for j in range(N-1, -1, -1):
            if H[i][j] > 0:
                load(H[i][j])
                v += H[i][j]
                H[i][j] = 0
            elif v > 0:
                d = min(abs(H[i][j]), v)
                if d > 0:
                    put(d)
                    v -= d
                    H[i][j] += d
            if j > 0:
                ans.append("L")
        return v

    def play_ij(i, sj, v):
        j = sj
        while j < N:
            if H[i][j] > 0:
                load(H[i][j])
                v += H[i][j]
                H[i][j] = 0
            elif v > 0:
                d = min(abs(H[i][j]), v)
                if d > 0:
                    put(d)
                    v -= d
                    H[i][j] += d
            if j < N-1:
                ans.append("R")
                j += 1
            else:
                break

        while j >= 0:
            if H[i][j] > 0:
                load(H[i][j])
                v += H[i][j]
                H[i][j] = 0
            elif v > 0:
                d = min(abs(H[i][j]), v)
                if d > 0:
                    put(d)
                    v -= d
                    H[i][j] += d
            if j > 0:
                ans.append("L")
                j -= 1
            else:
                break

        while j < N:
            if H[i][j] > 0:
                load(H[i][j])
                v += H[i][j]
                H[i][j] = 0
            elif v > 0:
                d = min(abs(H[i][j]), v)
                if d > 0:
                    put(d)
                    v -= d
                    H[i][j] += d
            if j < N - 1:
                ans.append("R")
                j += 1
            else:
                break

        while ans and (ans[-1] in "LR"):
            x = ans.pop()
            if x == "L":
                j += 1
            elif x == "R":
                j -= 1

        return i, j, v


    ni, nj = 0, 0
    v = 0
    for idx in range(N):
        i = decide_row(v)
        move(ni, nj, i, nj)
        ni, nj, v = play_ij(i, nj, v)
        finished[i] = 1

    print(*ans, sep="\n")


if __name__ == "__main__":
    main()
