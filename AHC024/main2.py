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

from collections import defaultdict


class UnionFind:
    def __init__(self, n):
        # 親要素のノード番号を格納　xが根のとき-(サイズ)を格納
        self.par = [-1 for i in range(n)]
        self.n = n
        self.roots = set(range(n))
        self.group_num = n
        self.members = defaultdict(set)

        for i in range(n):
            self.members[i].add(i)

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

        self.members[x] |= self.members[y]
        self.members[y] = set()

        self.par[x] += self.par[y]
        self.par[y] = x

    def size(self, x):
        return -self.par[self.find(x)]

    def get_members(self, x):
        root = self.find(x)
        return self.members[root]

    def get_roots(self):
        return self.roots

    def group_count(self):
        return len(self.roots)

    def all_group_members(self):
        return self.members

    def __repr__(self):
        return '\n'.join('{}: {}'.format(r, self.members[r]) for r in self.roots)


def main():
    N, M = NMI()
    C = EI(N)
    G = [set() for _ in range(M + 1)]

    DH = [0, 0, 1, -1]
    DW = [1, -1, 0, 0]

    DH8 = [0, 0, 1, -1, 1, 1, -1, -1]
    DW8 = [1, -1, 0, 0, 1, -1, 1, -1]

    cnts = [0] * (M + 1)

    def in_grid(h, w, n):
        return 0 <= h < n and 0 <= w < n

    def can_change(h, w):
        # 周囲8マスで自分と同じ色のマスが連結か？
        hws = [[0]*3 for _ in range(3)]
        S = 0
        for dh, dw in zip(DH8, DW8):
            nh, nw = h + dh, w + dw
            if in_grid(nh, nw, N) and C[nh][nw] == C[h][w]:
                hws[dh+1][dw+1] = 1
                S += 1

        # 適当にBFS
        seen = [[0]*3 for _ in range(3)]

        def bfs():
            T = 0
            for sh in range(3):
                for sw in range(3):
                    if hws[sh][sw] == 0:
                        continue
                    que = deque()
                    que.append([sh, sw])
                    seen[sh][sw] = 1
                    while que:
                        hh, ww = que.popleft()
                        T += 1
                        for dh, dw in zip(DH, DW):
                            if not in_grid(hh+dh, ww+dw, 3):
                                continue
                            if seen[hh+dh][ww+dw]:
                                continue
                            if hws[hh+dh][ww+dw] == 0:
                                continue
                            que.append([hh+dh, ww+dw])
                            seen[hh + dh][ww + dw] = 1
                    return T

        T = bfs()
        return S == T


    def tozero(h, w):
        # 隣接マスが0と自分しかなく、削除しても連結なら0にする
        Cs = []
        for dh, dw in zip(DH, DW):
            nh, nw = h + dh, w + dw
            if in_grid(nh, nw, N):
                Cs.append(C[nh][nw])
            else:
                Cs.append(0)

        SCs = set(Cs)
        if SCs | {0, C[h][w]} == {0, C[h][w]} and 0 in SCs:
            if can_change(h, w):
                C[h][w] = 0


    # 外側からtozero
    order = []
    for h in range(N):
        for w in range(N):
            order.append([h, w])

    order.sort(key=lambda x: -(abs(x[0]-N//2) + abs(x[1]-N//2)))

    for h, w in order:
        tozero(h, w)

    for row in C:
        print(*row)


if __name__ == "__main__":
    main()
