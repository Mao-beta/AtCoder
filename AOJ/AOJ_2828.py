import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.set_int_max_str_digits(10 ** 6)
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
import heapq

class MinCostFlow:
    """
    Successive Shortest Augmenting Path + Potentials (Johnson reweighting).
    - add_edge(u, v, cap, cost)
    - calc(s, t, flow): minimum cost to send 'flow' units (or INF if impossible)
    - get_edge(i): returns (from, to, cost, cap_fwd, cap_rev) for i-th forward edge
    """

    class _Edge:
        __slots__ = ("to", "rev", "cap", "cost")
        def __init__(self, to, rev, cap, cost):
            self.to = to
            self.rev = rev
            self.cap = cap
            self.cost = cost

    def __init__(self, N: int, inf: int = 10**30):
        self.N = N
        self.inf = inf
        self.g = [[] for _ in range(N)]
        self._fw_pos = []  # (from, index_in_g[from]) for each added forward edge
        self._has_negative_cost = False

    def add_edge(self, From: int, To: int, Cap: int, Cost: int):
        assert 0 <= From < self.N and 0 <= To < self.N
        assert Cap >= 0
        if Cost < 0:
            self._has_negative_cost = True

        fwd = MinCostFlow._Edge(To, len(self.g[To]), Cap, Cost)
        rev = MinCostFlow._Edge(From, len(self.g[From]), 0, -Cost)
        self.g[From].append(fwd)
        self.g[To].append(rev)
        self._fw_pos.append((From, len(self.g[From]) - 1))

    @property
    def M(self):
        return len(self._fw_pos)

    def get_edge(self, i: int):
        assert 0 <= i < self.M
        u, idx = self._fw_pos[i]
        e = self.g[u][idx]
        rev = self.g[e.to][e.rev]
        return u, e.to, e.cost, e.cap, rev.cap

    def _spfa_init_potential(self, s: int, pe: int):
        """
        Compute initial potentials h[] by shortest paths from s on residual graph,
        allowing negative edge costs. SPFA is fine here due to small constraints.
        """
        N = self.N
        h = [self.inf] * N
        inq = [False] * N
        q = deque([s])
        h[s] = 0
        inq[s] = True

        while q:
            u = q.popleft()
            inq[u] = False
            du = h[u]
            if du == self.inf:
                continue
            for e in self.g[u]:
                if e.cap <= pe:
                    continue
                v = e.to
                nd = du + e.cost
                if nd < h[v]:
                    h[v] = nd
                    if not inq[v]:
                        inq[v] = True
                        q.append(v)

        # unreachable nodes keep inf -> set to 0 to avoid inf arithmetic in reduced costs
        for i in range(N):
            if h[i] >= self.inf // 2:
                h[i] = 0
        return h

    def calc(self, start: int, goal: int, flow: int, permissible_error: int = 0) -> int:
        """
        Return minimum cost to send 'flow' units from start to goal.
        If impossible, return self.inf.
        permissible_error: treat edges with residual cap <= permissible_error as 0-cap.
        """
        assert 0 <= start < self.N and 0 <= goal < self.N and start != goal
        assert flow >= 0

        pe = max(0, permissible_error)
        N = self.N
        s, t = start, goal

        # potentials (h)
        if self._has_negative_cost:
            h = self._spfa_init_potential(s, pe)
        else:
            h = [0] * N

        res_cost = 0
        prev_v = [0] * N
        prev_e = [0] * N

        while flow > 0:
            dist = [self.inf] * N
            dist[s] = 0
            pq = [(0, s)]

            while pq:
                d, u = heapq.heappop(pq)
                if d != dist[u]:
                    continue
                for ei, e in enumerate(self.g[u]):
                    if e.cap <= pe:
                        continue
                    v = e.to
                    # reduced cost (must be >= 0 when h is feasible)
                    nd = d + e.cost + h[u] - h[v]
                    if nd < dist[v]:
                        dist[v] = nd
                        prev_v[v] = u
                        prev_e[v] = ei
                        heapq.heappush(pq, (nd, v))

            if dist[t] >= self.inf // 2:
                return self.inf  # cannot send remaining flow

            # update potentials
            for v in range(N):
                if dist[v] < self.inf // 2:
                    h[v] += dist[v]

            # push as much as possible along path (usually 1 in matching problems)
            addf = flow
            v = t
            while v != s:
                u = prev_v[v]
                e = self.g[u][prev_e[v]]
                addf = min(addf, e.cap)
                v = u

            v = t
            while v != s:
                u = prev_v[v]
                e = self.g[u][prev_e[v]]
                e.cap -= addf
                self.g[v][e.rev].cap += addf
                v = u

            # path cost in original costs equals h[t] - h[s]; h[s] stays 0 because dist[s]=0
            res_cost += addf * (h[t] - h[s])
            flow -= addf

        return res_cost


def main():
    for _ in range(51):
        """
        最小重み最大二部マッチングに帰着する
        S->iはCap=1, Cost=0
        iがjを収容するときにi->jの重みがCap=1, Cost=-Vjとする（最小化のため反転）
         収容できるかの判定は、各々回転できるのでXYZ[i]をそれぞれソート
        iが何も収容しない場合にダミー頂点Dについてi->D Cap=1, Cost=0
        D->TはCap=N, Cost=0
        totalから|res|を引くと答え
        """
        N = NI()
        if N == 0:
            return
        XYZ = EI(N)
        XYZ = [sorted(p) for p in XYZ]
        G = MinCostFlow(2*N+3)
        S = 2*N
        T = S+1
        D = T+1
        total = 0
        for i in range(N):
            xi, yi, zi = XYZ[i]
            total += xi*yi*zi
            G.add_edge(S, i, 1, 0)
            G.add_edge(i+N, T, 1, 0)
            G.add_edge(i, D, 1, 0)
            for j in range(N):
                xj, yj, zj = XYZ[j]
                if xi > xj and yi > yj and zi > zj:
                    G.add_edge(i, j+N, 1, -xj*yj*zj)
        G.add_edge(D, T, N, 0)
        res = G.calc(S, T, N)
        print(total - abs(res))


if __name__ == "__main__":
    main()
