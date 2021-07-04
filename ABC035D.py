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



class Dijkstra:
    """ ダイクストラ法
    重み付きグラフにおける単一始点最短路アルゴリズム

    * 使用条件
        - 負のコストがないこと
        - 有向グラフ、無向グラフともにOK

    * 計算量はO(E*log(V))

    * ベルマンフォード法より高速なので、負のコストがないならばこちらを使うとよい
    """

    def __init__(self, n, edges, is_one_index=False):
        """
        :param n: 頂点数 頂点は数字じゃなくてもよい
        :param edges: [from, to, cost]の形の辺のList
        :param is_one_index: 1-indexならTrue
        """
        from collections import defaultdict

        self.n = n
        self.edges = edges
        self.INF = 10**20

        self.graph = defaultdict(list)
        for a, b, c in edges:
            if is_one_index:
                a, b = a-1, b-1
            self.graph[a].append((b, c))

    def get_mincost(self, start):
        from collections import defaultdict
        import heapq

        hq = []
        heapq.heappush(hq, (0, start))

        res = defaultdict(lambda: self.INF)
        temp_costs = defaultdict(lambda: self.INF)

        while hq:
            now_c, now = heapq.heappop(hq)
            if res[now] < now_c:
                continue

            res[now] = now_c
            for goto, cost in self.graph[now]:
                goto_c = now_c + cost

                if temp_costs[goto] > goto_c:
                    heapq.heappush(hq, (goto_c, goto))
                    temp_costs[goto] = goto_c

        return res


def main():
    N, M, T = NMI()
    A = NLI()
    edges = [NLI() for _ in range(M)]
    rev_edges = [[b, a, c] for a, b, c in edges]
    D = Dijkstra(N, edges, is_one_index=True)
    D_rev = Dijkstra(N, rev_edges, is_one_index=True)

    min_cost = D.get_mincost(0)
    rev_cost = D_rev.get_mincost(0)

    ans = 0
    for i in range(N):
        m = min_cost[i]
        r = rev_cost[i]
        if m + r > T:
            continue
        ans = max(ans, (T-m-r)*A[i])
    print(ans)


if __name__ == "__main__":
    main()
