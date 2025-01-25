import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.set_int_max_str_digits(10**6)
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


class SCC:
    def __init__(self, N, edges, in_origin=1):
        """
        強連結成分分解(SCC): N, edgesからグラフGに対するSCCを行う
        入力: <N>: 頂点サイズ, <G>: 順方向の有向グラフ, <RG>: 逆方向の有向グラフ
        出力: (<ラベル数>, <各頂点のラベル番号>) トポロジカルソート済
        計算量: O(V+E)
        縮約後のグラフを構築: トポソ済み
        G0: 各強連結成分の遷移先の集合
        GP: 各強連結成分内の元の頂点のリスト
        """
        assert N == len(edges)
        assert 0 <= in_origin <= 1
        self.N = N
        self.edges = edges
        self.G, self.RG = self.make_G_RG(N, edges, in_origin=in_origin)
        self.label, self.group = self.scc(self.N, self.G, self.RG)
        self.G0, self.GP = self.construct(self.N, self.G, self.label, self.group)

    def make_G_RG(self, N, edges, in_origin=1):
        G = [[] for _ in range(N)]
        RG = [[] for _ in range(N)]
        for u, v in edges:
            u -= in_origin
            v -= in_origin
            G[u].append(v)
            RG[v].append(u)
        return G, RG


    def scc(self, N, G, RG):
        order = []
        used = [0]*N
        group = [None]*N
        def dfs(s):
            used[s] = 1
            for t in G[s]:
                if not used[t]:
                    dfs(t)
            order.append(s)
        def rdfs(s, col):
            group[s] = col
            used[s] = 1
            for t in RG[s]:
                if not used[t]:
                    rdfs(t, col)
        for i in range(N):
            if not used[i]:
                dfs(i)
        used = [0]*N
        label = 0
        for s in reversed(order):
            if not used[s]:
                rdfs(s, label)
                label += 1
        return label, group


    def construct(self, N, G, label, group):
        G0 = [set() for i in range(label)]
        GP = [[] for i in range(label)]
        for v in range(N):
            lbs = group[v]
            for w in G[v]:
                lbt = group[w]
                if lbs == lbt:
                    continue
                G0[lbs].add(lbt)
            GP[lbs].append(v)
        return G0, GP


class StronglyConnectedComponents:
    def __init__(self, number_of_vertices, directed_edges, input_origin_offset=1):
        """
        強連結成分分解 (SCC: Strongly Connected Components) を実行するクラス。
        与えられた頂点数 (number_of_vertices) および有向辺リスト (directed_edges) から、
        グラフに対して強連結成分分解を行う。

        Parameters
        ----------
        number_of_vertices : int
            頂点数。グラフに含まれる頂点の総数。
        directed_edges : list of list
            (u, v) という形のタプルを要素としたリスト。
            u から v への有向辺を表す。
        input_origin_offset : int
            入力頂点番号が 0-index ではなく 1-index で与えられる場合に使用するオフセット。
            デフォルトは 1。

        Attributes
        ----------
        number_of_vertices : int
            頂点数。
        directed_edges : list of list
            (u, v) という形のタプルを要素としたリスト。u から v への有向辺を表す。
        adjacency_list : list of list
            グラフの順方向の隣接リスト。
        reverse_adjacency_list : list of list
            グラフの逆方向の隣接リスト。
        label_count : int
            強連結成分の総数 (ラベル数)。
        component_labels : list of int
            各頂点が属する強連結成分のラベル番号。0 から label_count-1 のいずれか。
        condensed_graph : list of set
            強連結成分同士の遷移を表現したグラフ。重複を排除するために set を使用。
        components_original_vertices : list of list
            各強連結成分に含まれる元の頂点のリスト。

        Notes
        -----
        - 計算量は O(V + E) (V: 頂点数, E: 辺数)。
        - 返される強連結成分はトポロジカルソート済みの順序に従ってラベル付けされる。
        - 強連結成分に縮約後のグラフ (condensed_graph) は、強連結成分を頂点とみなしたときの
          トポロジカルソートが可能な DAG (有向非巡回グラフ) となる。
        - components_original_vertices[component_label] により、component_label に対応する
          強連結成分内の元の頂点を取得できる。
        """
        assert number_of_vertices == len(directed_edges), \
            "number_of_vertices と directed_edges のサイズが一致しません。"
        assert 0 <= input_origin_offset <= 1, \
            "input_origin_offset は 0 または 1 を指定してください。"

        self.number_of_vertices = number_of_vertices
        self.directed_edges = directed_edges

        # グラフの作成 (順方向 / 逆方向)
        self.adjacency_list, self.reverse_adjacency_list = self.construct_forward_and_reverse_graphs(
            self.number_of_vertices,
            self.directed_edges,
            input_origin_offset
        )

        # 強連結成分分解の実行 (非再帰 DFS 版)
        self.label_count, self.component_labels = self.perform_scc_decomposition(
            self.number_of_vertices,
            self.adjacency_list,
            self.reverse_adjacency_list
        )

        # SCC 縮約後のグラフと、各 SCC が含む元の頂点のリストを作成
        self.condensed_graph, self.components_original_vertices = self.construct_condensed_graph(
            self.number_of_vertices,
            self.adjacency_list,
            self.label_count,
            self.component_labels
        )

    def construct_forward_and_reverse_graphs(self, number_of_vertices, directed_edges, input_origin_offset):
        """
        順方向および逆方向の隣接リストを構築する。

        Parameters
        ----------
        number_of_vertices : int
            頂点数。
        directed_edges : list of list
            有向辺を (u, v) という形のタプルで格納したリスト。
        input_origin_offset : int
            頂点番号が 1 から始まる場合に考慮するオフセット。

        Returns
        -------
        tuple of (list of list, list of list)
            - 順方向の隣接リスト (adjacency_list)
            - 逆方向の隣接リスト (reverse_adjacency_list)
        """
        adjacency_list = [[] for _ in range(number_of_vertices)]
        reverse_adjacency_list = [[] for _ in range(number_of_vertices)]

        for start_vertex, end_vertex in directed_edges:
            start_vertex_adjusted = start_vertex - input_origin_offset
            end_vertex_adjusted = end_vertex - input_origin_offset

            adjacency_list[start_vertex_adjusted].append(end_vertex_adjusted)
            reverse_adjacency_list[end_vertex_adjusted].append(start_vertex_adjusted)

        return adjacency_list, reverse_adjacency_list

    def perform_scc_decomposition(self, number_of_vertices, adjacency_list, reverse_adjacency_list):
        """
        強連結成分分解 (SCC) を実行し、各頂点に対して強連結成分ラベルを付与する。
        DFS はすべて非再帰 (イテレーティブ) 実装を用いる。

        Parameters
        ----------
        number_of_vertices : int
            頂点数。
        adjacency_list : list of list
            グラフの順方向の隣接リスト。
        reverse_adjacency_list : list of list
            グラフの逆方向の隣接リスト。

        Returns
        -------
        tuple of (int, list of (int or None))
            - 強連結成分の総数 (label_count)
            - 各頂点が属する強連結成分のラベル番号のリスト (component_labels)
        """
        visited_order = []
        visited_flag = [False] * number_of_vertices
        component_labels = [None] * number_of_vertices

        # 非再帰DFS (順方向): 帰りがけ順のリスト (visited_order) を構築する
        for vertex_index in range(number_of_vertices):
            if not visited_flag[vertex_index]:
                self._iterative_dfs_for_postorder(
                    vertex_index,
                    adjacency_list,
                    visited_flag,
                    visited_order
                )

        # 帰りがけ順を逆にしたリストを使って、逆グラフで再度 DFS (非再帰)
        visited_flag = [False] * number_of_vertices
        current_label = 0

        for vertex_index in reversed(visited_order):
            if not visited_flag[vertex_index]:
                self._iterative_dfs_for_labeling(
                    vertex_index,
                    reverse_adjacency_list,
                    visited_flag,
                    component_labels,
                    current_label
                )
                current_label += 1

        return current_label, component_labels

    def _iterative_dfs_for_postorder(self, start_vertex, adjacency_list, visited_flag, visited_order):
        """
        非再帰 DFS を用いて、start_vertex から到達可能な頂点群の
        帰りがけ順 (ポストオーダー) を visited_order に格納する。

        Parameters
        ----------
        start_vertex : int
            探索を開始する頂点。
        adjacency_list : list of list
            グラフの隣接リスト (順方向)。
        visited_flag : list of bool
            各頂点の訪問状況を示すフラグ。
        visited_order : list of int
            帰りがけ順に頂点を追加するためのリスト。
        """
        stack = [start_vertex]
        # 探索の進捗を管理するための補助スタック (ポストオーダー取得用)
        # 「一度訪問した頂点を二度目に pop するときに順序リストに追加する」方式
        path_stack = []

        while stack:
            current_vertex = stack.pop()
            if not visited_flag[current_vertex]:
                visited_flag[current_vertex] = True
                # 子の探索が終わったら帰りがけ順に追加するため、path_stack に積む
                path_stack.append(current_vertex)

                # 隣接する頂点をスタックに積む
                for next_vertex in adjacency_list[current_vertex]:
                    if not visited_flag[next_vertex]:
                        stack.append(next_vertex)

        # path_stack から逆順に取り出すことで、帰りがけ順を確定させる
        while path_stack:
            visited_order.append(path_stack.pop())

    def _iterative_dfs_for_labeling(self, start_vertex, reverse_adjacency_list, visited_flag,
                                    component_labels, label):
        """
        非再帰 DFS を用いて、start_vertex から到達可能な頂点群に
        同じラベルを付与する。

        Parameters
        ----------
        start_vertex : int
            探索を開始する頂点。
        reverse_adjacency_list : list of list
            グラフの隣接リスト (逆方向)。
        visited_flag : list of bool
            各頂点の訪問状況を示すフラグ。
        component_labels : list of int
            頂点のラベルを格納するリスト。
        label : int
            現在割り当てる強連結成分ラベル。
        """
        stack = [start_vertex]
        while stack:
            current_vertex = stack.pop()
            if not visited_flag[current_vertex]:
                visited_flag[current_vertex] = True
                component_labels[current_vertex] = label
                for next_vertex in reverse_adjacency_list[current_vertex]:
                    if not visited_flag[next_vertex]:
                        stack.append(next_vertex)

    def construct_condensed_graph(
            self,
            number_of_vertices,
            adjacency_list,
            label_count,
            component_labels
    ):
        """
        強連結成分に縮約した後のグラフを生成する。

        Parameters
        ----------
        number_of_vertices : int
            元のグラフの頂点数。
        adjacency_list : list of list
            元のグラフの順方向の隣接リスト。
        label_count : int
            強連結成分の総数 (ラベル数)。
        component_labels : list of int
            各頂点が属する強連結成分のラベル番号。

        Returns
        -------
        tuple of (list of set, list of list)
            - 強連結成分を頂点とした縮約グラフ (condensed_graph)
              (重複を排除するために set を使用)
            - 各強連結成分に含まれる元の頂点のリスト (components_original_vertices)
        """
        condensed_graph = [set() for _ in range(label_count)]
        components_original_vertices = [[] for _ in range(label_count)]

        for original_vertex in range(number_of_vertices):
            from_label = component_labels[original_vertex]

            # 同じ強連結成分に属さない頂点への辺のみを追加
            for adjacent_vertex in adjacency_list[original_vertex]:
                to_label = component_labels[adjacent_vertex]
                if from_label != to_label:
                    condensed_graph[from_label].add(to_label)

            # 強連結成分内に元の頂点を追加
            components_original_vertices[from_label].append(original_vertex)

        return condensed_graph, components_original_vertices


def main():
    N, M = NMI()
    A = NLI()
    edges = [[i, a] for i, a in enumerate(A, start=1)]
    scc = StronglyConnectedComponents(N, edges, input_origin_offset=1)
    K = scc.label_count
    G = [[] for _ in range(K)]
    roots = []
    for c, V in enumerate(scc.condensed_graph):
        if len(V) == 0:
            roots.append(c)
        for p in V:
            G[p].append(c)
    print(G, roots)
    # 点
    dp = [[0]*(M+1) for _ in range(K)]
    stack = deque()



if __name__ == "__main__":
    main()
