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


class CentroidDecomposition:
    """
    # 重心分解 O(NlogN)
    # 1. 重心をみつける
    #    - 適当な根からdfsし、各点における上下の部分木サイズの大きいほうが最小の点
    # 2. 重心を取り除く
    # 3. 取り除いた後の各連結成分に対して再帰的に1->2をおこなう(実装は非再帰)

    CDtree = CentroidDecomposition(N, G).cd_parents
    木構造として各点から見た親を返す。根(全体の重心)は親が-1
    """
    def __init__(self, N, G):
        """
        :param N: 頂点数
        :param G: 隣接グラフ(0-index)
        """
        self.N = N
        self.G = G
        self.subsizes = [0] * N
        self.is_removed = [0] * N
        self.cd_parents = [-1] * N  # 分解後の親

        self._build()

    def _build(self):
        # ある部分木について探索開始する点、サイズ、前回のcentroid
        roots = deque([[0, self.N, -1]])

        while roots:
            root, total, cd_par = roots.popleft()

            # 部分木の中でDFS
            stack = deque()
            stack.append([~root, -1])
            stack.append([root, -1])

            while stack:
                # print(stack)
                now, par = stack.pop()

                # 行きがけ
                if now >= 0:
                    # print("now", now)
                    self.subsizes[now] = 1

                    for goto in self.G[now]:
                        if goto == par or self.is_removed[goto]:
                            continue

                        stack.append([~goto, now])
                        stack.append([goto, now])

                # 帰りがけ
                else:
                    now = ~now
                    # 親のサイズに自分のサイズを加算
                    if par != -1:
                        self.subsizes[par] += self.subsizes[now]

                    # 自分を根としたときの部分木サイズの最大が、合計サイズの半分以下なら重心
                    subsize_max = -1
                    for goto in self.G[now]:
                        if goto == par or self.is_removed[goto]:
                            continue
                        subsize_max = max(subsize_max, self.subsizes[goto])

                    subsize_max = max(subsize_max, total - self.subsizes[now])

                    # 重心だったら新たなrootを追加
                    if subsize_max <= total // 2:
                        # 親の部分木サイズを便宜的に処理（自分を根としたときのサイズ）
                        if par != -1:
                            self.subsizes[par] = total - self.subsizes[now]

                        self.cd_parents[now] = cd_par
                        self.is_removed[now] = 1
                        for goto in self.G[now]:
                            if self.is_removed[goto]:
                                continue
                            # 自分の隣接点を新たな探索開始点とし、そのサイズはsubsizes[goto]
                            roots.append([goto, self.subsizes[goto], now])
                        break


def main():
    N = NI()
    AB = EI(N-1)
    G = adjlist(N, AB)

    CDtree = CentroidDecomposition(N, G).cd_parents
    res = [x + 1 if x > -1 else -1 for x in CDtree]
    print(*res)


if __name__ == "__main__":
    main()
