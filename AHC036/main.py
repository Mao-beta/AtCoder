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


def read_input_from_file(file_path: str):
    with open(file_path, 'r') as f:
        N, M, T, La, Lb = map(int, f.readline().split())

        edges = []
        for _ in range(M):
            ui, vi = map(int, f.readline().split())
            edges.append((ui, vi))

        tours = list(map(int, f.readline().split()))

        XY = []
        for _ in range(N):
            xi, yi = map(int, f.readline().split())
            XY.append((xi, yi))

    return N, M, T, La, Lb, edges, tours, XY


def read_input_from_stdin():
    N, M, T, La, Lb = map(int, input().split())

    edges = []
    for _ in range(M):
        ui, vi = map(int, input().split())
        edges.append((ui, vi))

    tours = list(map(int, input().split()))

    XY = []
    for _ in range(N):
        xi, yi = map(int, input().split())
        XY.append((xi, yi))

    return N, M, T, La, Lb, edges, tours, XY


class Input:
    def __init__(self, file_path: str = None):
        if file_path:
            self.N, self.M, self.T, self.La, self.Lb, self.edges, self.tours, self.XY = read_input_from_file(
                file_path)
        else:
            self.N, self.M, self.T, self.La, self.Lb, self.edges, self.tours, self.XY = read_input_from_stdin()

    def parse(self):
        return self.N, self.M, self.T, self.La, self.Lb, self.edges, self.tours, self.XY


def output_results(A: list[int], Actions: list[list[int]], file_path: str = None):
    # 1行目にリストAの中身をスペース区切りで出力
    output_lines = [" ".join(map(str, A))]

    # Actionsの各リストを1行ずつ出力
    for action in Actions:
        output_lines.append(" ".join(map(str, action)))

    # 標準出力に出力
    output_text = "\n".join(output_lines)
    print(output_text)

    # ファイルパスが指定されていれば、ファイルにも出力
    if file_path:
        output_file = file_path.replace("in/", "out/", 1)
        # ファイルに書き込む
        with open(output_file, 'w') as f:
            f.write(output_text + "\n")


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
        heapq.heappush(que, (0, s))  # 始点の(最短距離, 頂点番号)をヒープに追加する

        while len(que) != 0:
            cost, v = heapq.heappop(que)
            # キューに格納されている最短経路の候補がdの距離よりも大きければ、他の経路で最短経路が存在するので、処理をスキップ
            if d[v] < cost: continue

            for i in range(len(self.G[v])):
                # 頂点vに隣接する各頂点に関して、頂点vを経由した場合の距離を計算し、今までの距離(d)よりも小さければ更新する
                e = self.G[v][i]  # vのi個目の隣接辺e
                if d[e.to] > d[v] + e.cost:
                    d[e.to] = d[v] + e.cost  # dの更新
                    heapq.heappush(que, (d[e.to], e.to))  # キューに新たな最短経路の候補(最短距離, 頂点番号)の情報をpush
        return d


def solve(input_data):
    N, M, T, La, Lb, edges, tours, XY = input_data.parse()
    edges = [[x-1, y-1] for x, y in edges]
    print(f"# {N=} {M=} {T=} {La=} {Lb=}")
    INF = 10**5
    # ワーシャルフロイド
    G = Dijkstra(N)
    for u, v in edges:
        G.add(u, v, 1)
        G.add(v, u, 1)

    D = []
    for i in range(N):
        D.append(G.shortest_path(i)[:])

    TS = sorted(list(set(tours)))
    Ct = Counter()
    for ti in TS:
        for tj in TS:
            if ti >= tj:
                continue
            Ct[D[ti][tj]] += 1

    print(sorted(Ct.most_common()))


    A = []
    actions = []

    return A, actions



def T_check():
    # Tの分布 380/600くらい
    for case in range(100):
        file_path = f'in/{str(case).zfill(4)}.txt'  # 必要に応じてファイルパスを指定

        input_data = Input(file_path)
        print(len(set(input_data.tours)))


def main():
    for case in range(100):
        file_path = f'in/{str(case).zfill(4)}.txt'  # 必要に応じてファイルパスを指定

        input_data = Input(file_path)
        A, actions = solve(input_data)
        output_results(A, actions, file_path=file_path)


if __name__ == "__main__":
    # T_check()
    main()
