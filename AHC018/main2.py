import sys
from enum import Enum
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations
from typing import Tuple, List, Union, Optional
from pathlib import Path

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


IS_LOCAL = False
try:
    import matplotlib.pyplot as plt
    IS_LOCAL = True
except:
    pass


# IS_LOCAL = False

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


# 座標
class Pos:
    def __init__(self, y: int, x: int, n: int = 200):
        self.y = y
        self.x = x
        self.idx = y * n + x

    def __str__(self):
        return f"y: {self.y}, x: {self.x}"

# 結果変数
class Response(Enum):
    NOT_BROKEN = 0
    BROKEN = 1
    FINISH = 2
    INVALID = -1

# オブジェクトの種類
class Object(Enum):
    VACANT = 0
    WATER = 1
    HOUSE = 2

# ローカル出力用解答
class Ans:
    def __init__(self):
        self.ans = []

    def append(self, ans_q: list):
        self.ans.append(ans_q)

    def output(self, dst_path: Optional[Path] = None):
        if dst_path is None:
            return

        with open(dst_path, mode="w") as f:
            for y, x, p in self.ans:
                f.write(f"{y} {x} {p}\n")


class Input:
    """
    N, W, K, C
    source_pos, house_pos
    S: Grid
    dst_path
    """
    def __init__(self, src_path: Optional[Path] = None):
        self.src_path = src_path
        self.source_pos: List[Pos] = []
        self.house_pos: List[Pos] = []

        if isinstance(src_path, Path):
            filename = src_path.name
            self.dst_path = Path(f"./out/{filename}")

            with open(src_path, mode="r") as f:
                f = f.readlines()
                self.N, self.W, self.K, self.C = map(int, f[0].split(" "))
                self.S = []
                for i in range(1, self.N + 1):
                    self.S.append(list(map(int, f[i].split())))

                for i in range(self.W):
                    y, x = (int(v) for v in f[self.N + 1 + i].split(" "))
                    self.source_pos.append(Pos(y, x))
                for i in range(self.K):
                    y, x = (int(v) for v in f[self.N + 1 + self.W + i].split(" "))
                    self.house_pos.append(Pos(y, x))

        else:
            self.N, self.W, self.K, self.C = [int(v) for v in input().split(" ")]
            self.S = None
            self.dst_path = None

            for _ in range(self.W):
                y, x = (int(v) for v in input().split(" "))
                self.source_pos.append(Pos(y, x))
            for _ in range(self.K):
                y, x = (int(v) for v in input().split(" "))
                self.house_pos.append(Pos(y, x))

    def __str__(self):
        if self.src_path is None:
            src = "Online"
        else:
            src = self.src_path

        res = [f"# Inputs from {src}",
               f"# N: {self.N}, W: {self.W}, K: {self.K}, C: {self.C}",]
        return "\n".join(res)


# 盤面
Grid = Union[List[List[int]], List[List[Object]]]
class Field:
    def __init__(self, inputs: Input):
        self.inputs = inputs
        self.is_broken: Grid = [[Response.NOT_BROKEN] * inputs.N for _ in range(inputs.N)]
        self.objects: Grid = [[Object.VACANT for _ in range(inputs.N)] for _ in range(inputs.N)]
        self.total_cost = 0

        self.status = Response.NOT_BROKEN

        self.SUPER_SRC = inputs.N**2
        self.uf = UnionFind(inputs.N**2 + 1)

        for pos in inputs.source_pos:
            self.objects[pos.y][pos.x] = Object.WATER
            self.uf.unite(self.SUPER_SRC, pos.idx)
        for pos in inputs.house_pos:
            self.objects[pos.y][pos.x] = Object.HOUSE


    def check_finish(self):
        for pos in self.inputs.house_pos:
            if not self.uf.is_same(pos.idx, self.SUPER_SRC):
                return False

        self.status = Response.FINISH
        return True


    def judge(self, y: int, x: int, power: int) -> Response:
        if self.inputs.S[y][x] > power:
            self.inputs.S[y][x] -= power
            return Response.NOT_BROKEN
        else:
            self.inputs.S[y][x] = 0
            return Response.BROKEN

    def query(self, y: int, x: int, power: int) -> Tuple[Response, List]:
        if self.is_broken[y][x] == Response.BROKEN:
            return Response.BROKEN, []

        self.total_cost += power + self.inputs.C
        if not IS_LOCAL:
            print(f"{y} {x} {power}", flush=True)
        q = [y, x, power]

        if IS_LOCAL:
            res = self.judge(y, x, power)
        else:
            res = Response(NI())

        if res in (Response.BROKEN, Response.FINISH):
            self.is_broken[y][x] = Response.BROKEN

            for dy, dx in zip([0, 0, 1, -1], [1, -1, 0, 0]):
                nx = x+dx
                ny = y+dy
                if 0 <= nx < self.inputs.N and 0 <= ny < self.inputs.N:
                    if self.is_broken[ny][nx] == Response.BROKEN:
                        self.uf.unite(Pos(ny, nx).idx, Pos(y, x).idx)

        self.check_finish()

        return res, q



def MST(N, edges):
    """
    要UnionFind
    N頂点の最小全域木の長さ
    edges = [[u, v, cost], ....] (0-index)
    """
    uf = UnionFind(N)
    edges.sort(key=lambda x: x[-1])
    res = []
    for a, b, c in edges:
        if uf.is_same(a, b):
            continue
        else:
            res.append([a, b, c])
            uf.unite(a, b)
    return res, uf


def adjlist(n, edges, directed=False, in_origin=1):
    if len(edges) == 0:
        return [[] for _ in range(n)]

    weighted = True if len(edges[0]) > 2 else False
    if in_origin == 1:
        if weighted:
            edges = [[x-1, y-1, w] for x, y, w in edges]
        else:
            edges = [[x-1, y-1] for x, y in edges]

    res = [[] for _ in range(n)]

    if weighted:
        for u, v, c in edges:
            res[u].append([v, c])
            if not directed:
                res[v].append([u, c])

    else:
        for u, v in edges:
            res[u].append(v)
            if not directed:
                res[v].append(u)

    return res


class Dijkstra():
    """ ダイクストラ法
    重み付きグラフにおける単一始点最短路アルゴリズム

    * 使用条件
        - 負のコストがないこと
        - 有向グラフ、無向グラフともにOK

    * 計算量はO(E*log(V))

    * ベルマンフォード法より高速なので、負のコストがないならばこちらを使うとよい
    """

    class Edge():
        """ 重み付き有向辺 """

        def __init__(self, _to, _cost):
            self.to = _to
            self.cost = _cost

    def __init__(self, V):
        """ 重み付き有向辺
        無向辺を表現したいときは、_fromと_toを逆にした有向辺を加えればよい

        Args:
            V(int): 頂点の数
        """
        self.G = [[] for i in range(V)]  # 隣接リストG[u][i] := 頂点uのi個目の隣接辺
        self._E = 0  # 辺の数
        self._V = V  # 頂点の数

    @property
    def E(self):
        """ 辺数
        無向グラフのときは、辺数は有向グラフの倍になる
        """
        return self._E

    @property
    def V(self):
        """ 頂点数 """
        return self._V

    def add(self, _from, _to, _cost):
        """ 2頂点と、辺のコストを追加する """
        self.G[_from].append(self.Edge(_to, _cost))
        self._E += 1

    def shortest_path(self, s):
        """ 始点sから頂点iまでの最短路を格納したリストを返す
        Args:
            s(int): 始点s
        Returns:
            d(list): d[i] := 始点sから頂点iまでの最短コストを格納したリスト。
                     到達不可の場合、値はfloat("inf")
        """
        import heapq
        que = []  # プライオリティキュー（ヒープ木）
        d = [float("inf")] * self.V
        d[s] = 0
        heapq.heappush(que, (0, s, self.V))  # 始点の(最短距離, 頂点番号)をヒープに追加する

        pars = [self.V] * self.V

        while len(que) != 0:
            cost, v, par = heapq.heappop(que)
            # キューに格納されている最短経路の候補がdの距離よりも大きければ、他の経路で最短経路が存在するので、処理をスキップ
            if d[v] < cost: continue
            # print(d[v], cost, v, par)

            for i in range(len(self.G[v])):
                # 頂点vに隣接する各頂点に関して、頂点vを経由した場合の距離を計算し、今までの距離(d)よりも小さければ更新する
                e = self.G[v][i]  # vのi個目の隣接辺e
                if d[e.to] > d[v] + e.cost:
                    d[e.to] = d[v] + e.cost  # dの更新
                    pars[e.to] = v
                    # print("#", d[e.to], d[v] + e.cost, e.to, v)
                    heapq.heappush(que, (d[e.to], e.to, v))  # キューに新たな最短経路の候補(最短距離, 頂点番号)の情報をpush
        return d, pars

    def reconstruct(self, dists, pars, s, t):
        assert dists[s] == 0
        assert pars[s] == self.V
        res = []
        while pars[t] != self.V:
            res.append([pars[t], t])
            t = pars[t]
        return res


class Solver:
    def __init__(self, inputs: Input):
        self.inputs = inputs
        self.field = Field(inputs)
        self.ans = Ans()


    def check_gameover(self):
        if self.field.status == Response.FINISH:
            return True
        else:
            return False


    def solve_first_water(self):
        # self.carpet_knock(dist=10, power=100)

        for pos_h in self.inputs.house_pos:
            self.move(self.inputs.source_pos[0], pos_h, 100)
            if self.check_gameover():
                return

    def solve(self, dist, power, k):
        # spots = self.carpet_knock(dist=dist, power=100)
        spots = self.arround_knock(dist=dist, power=100, k=k)
        V_base = len(spots)
        edges = []
        spots += self.inputs.house_pos[:]
        spots += self.inputs.source_pos[:]

        for i in range(len(spots)):
            for j in range(i+1, len(spots)):
                pos1, pos2 = spots[i], spots[j]
                cost = abs(pos1.x - pos2.x) + abs(pos1.y - pos2.y)
                edges.append([i, j, cost])

        V = len(spots)
        D = Dijkstra(V)

        p = 2 if self.inputs.C < 4 else 4

        for i, j, cost in edges:
            D.add(i, j, cost**p)
            D.add(j, i, cost**p)

        for h in range(V_base, V_base + self.inputs.K):
            dists, pars = D.shortest_path(h)
            target_src = -1
            target_dist = 10**20
            for t in range(V_base + self.inputs.K, V):
                if target_dist > dists[t]:
                    target_dist = dists[t]
                    target_src = t

            res = D.reconstruct(dists, pars, h, target_src)[::-1]
            print("#", res)

            for i, j in res:
                self.move_zigzag(spots[i], spots[j], power)
                D.add(i, j, 0)
                D.add(j, i, 0)
                if self.check_gameover():
                    return


    def destruct(self, y, x, power):
        status = self.field.is_broken[y][x]
        while status == Response.NOT_BROKEN:
            status, q = self.field.query(y, x, power)
            self.ans.append(q)

    def move(self, pos_from: Pos, pos_to: Pos, power):
        # たて
        if pos_to.y - pos_from.y != 0:
            sgn = (pos_to.y - pos_from.y) // abs(pos_to.y - pos_from.y)
            for y in range(pos_from.y, pos_to.y + sgn, sgn):
                self.destruct(y, pos_from.x, power)
                if self.check_gameover():
                    return
        # よこ
        if pos_to.x - pos_from.x != 0:
            sgn = (pos_to.x - pos_from.x) // abs(pos_to.x - pos_from.x)
            for x in range(pos_from.x, pos_to.x + sgn, sgn):
                self.destruct(pos_to.y, x, power)
                if self.check_gameover():
                    return


    def move_zigzag(self, pos_from: Pos, pos_to: Pos, power):
        y, x = pos_from.y, pos_from.x
        self.destruct(y, x, power)
        if self.check_gameover():
            return


        while y != pos_to.y or x != pos_to.x:
            # たて
            if y != pos_to.y:
                sgn = (pos_to.y - y) // abs(pos_to.y - y)
                self.destruct(y+sgn, x, power)
                y += sgn
                if self.check_gameover():
                    return
            # よこ
            if x != pos_to.x:
                sgn = (pos_to.x - x) // abs(pos_to.x - x)
                self.destruct(y, x+sgn, power)
                x += sgn
                if self.check_gameover():
                    return


    def carpet_knock(self, dist: int, power: int):
        broken_pos = []

        for y in range(dist, self.inputs.N, dist):
            for x in range(dist, self.inputs.N, dist):
                res, q = self.field.query(y, x, power)
                self.ans.append(q)
                if res == Response.BROKEN:
                    broken_pos.append(Pos(y, x))

        return broken_pos


    def arround_knock(self, dist: int, power: int, k: int):
        broken_pos = set()

        for pos in self.inputs.source_pos + self.inputs.house_pos:
            for i in range(-k, k+1):
                for j in range(-k, k+1):
                    nx = pos.x // dist * dist + i * dist
                    ny = pos.y // dist * dist + j * dist

                    if (ny, nx) in broken_pos:
                        continue

                    if 0 <= nx < self.inputs.N and 0 <= ny < self.inputs.N:
                        res, q = self.field.query(ny, nx, power)
                        self.ans.append(q)
                        if res == Response.BROKEN:
                            broken_pos.add((ny, nx))

        broken_pos = [Pos(y, x) for y, x in broken_pos]
        return broken_pos


    def output(self, dst_path):
        with open(dst_path, mode="w") as f:
            f.write(f"# score {self.field.total_cost}\n")

            for row in self.ans.ans:
                y, x, p = row
                f.write(f"{y} {x} {p}\n")


def main():

    if IS_LOCAL:
        scores = {}

        for dist in [10]:
            for power in [100]:
                for k in [4]:

                    res = []
                    for fi in range(100):
                        filename = f"{str(fi).zfill(4)}.txt"
                        src_path = Path(f"./in/{filename}")
                        dst_path = Path(f"./out/{filename}")

                        I = Input(src_path)
                        print(I)

                        solver = Solver(I)
                        solver.solve(dist, power, k)
                        solver.output(dst_path)
                        res.append(solver.field.total_cost)

                    scores[(dist, power, k)] = sum(res) / len(res)

        print("#", scores)

    else:
        I = Input()
        print(I)
        solver = Solver(I)
        solver.solve(10, 100, 4)


if __name__ == "__main__":
    main()
