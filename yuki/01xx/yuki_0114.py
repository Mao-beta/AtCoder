import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

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


def min_steiner_tree(N, ABC, V):
    """
    最小シュタイナー木のコスト、N<=35, M<=N**2
    len(V)が14以下のときはO(N*3^T + N^2*2^T)、
    N-Vが21以下のときはO(M * 2^(N-len(V)))
    :param N: 頂点数
    :param ABC: [u, v, cost]のlist(0-index)
    :param V: 通る頂点のlist(0-index)
    :return: cost
    """
    INF = 10 ** 15
    M = len(ABC)
    T = len(V)

    if T <= 14:
        # 最小シュタイナー木
        # ワーシャルフロイド
        D = [[INF] * N for _ in range(N)]
        for i in range(N):
            D[i][i] = 0
        for a, b, c in ABC:
            D[a][b] = c
            D[b][a] = c
        for k in range(N):
            for i in range(N):
                for j in range(N):
                    D[i][j] = min(D[i][j], D[i][k] + D[k][j])
        # dp[i][S]: iを端点に持ち、Vの部分集合S(T-bit)を含むシュタイナー木の重み
        dp = [[INF] * (1 << T) for _ in range(N)]
        # 各vについて、端点がiのときの初期値
        for vi in range(T):
            for i in range(N):
                dp[i][1 << vi] = D[i][V[vi]]
            dp[V[vi]][1 << vi] = 0
        for i in range(N):
            dp[i][0] = 0

        def gen_subset(S):
            s = (S - 1) & S
            while s > 0:
                yield s
                s = (s - 1) & S

        # O(3^T)の部分集合DP
        # トータルでO(N*3^T + N^2*2^T)
        for S in range(1, 1 << T):
            for i in range(N):
                for E in gen_subset(S):
                    dp[i][S] = min(dp[i][S], dp[i][S - E] + dp[i][E])
            for i in range(N):
                for j in range(N):
                    dp[i][S] = min(dp[i][S], dp[j][S] + D[i][j])

        ans = INF
        for i in range(N):
            for S in range(1 << T):
                ans = min(ans, dp[i][S] + dp[i][(1 << T) - 1 - S])
        return ans

    else:
        # N-T <= 21
        # 使わない頂点の集合を全探索してMST

        class UnionFind:
            def __init__(self, n):
                # 親要素のノード番号を格納　xが根のとき-(サイズ)を格納
                self.par = [-1 for i in range(n)]
                self.n = n
                self.group_num = n

            def rebuild(self):
                for i in range(self.n):
                    self.par[i] = -1
                self.group_num = self.n

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

                self.par[x] += self.par[y]
                self.par[y] = x

        def MST(N, edges, target, uf, cnt):
            """
            要UnionFind
            N頂点のうち、target[i]==1の点のみの最小全域木の長さ
            edges = [[u, v, cost], ....] (0-index) (sort済み)
            """
            uf.rebuild()
            # edges.sort(key=lambda x: x[-1])
            res = 0
            for a, b, c in edges:
                if target[a] == 0 or target[b] == 0:
                    continue
                if uf.is_same(a, b):
                    continue
                else:
                    res += c
                    cnt -= 1
                    uf.unite(a, b)
                if cnt == 1:
                    return res

            return INF

        ABC.sort(key=lambda x: x[-1])
        mincost = sum(ABC[i][-1] for i in range(T-1))
        Vbar = [i for i in range(N) if i not in V]
        Vbn = len(Vbar)
        target = [1] * N
        uf = UnionFind(N)

        ans = INF
        for case in range(1 << Vbn):
            cnt = T
            for i in range(Vbn):
                if (case >> i) & 1:
                    target[Vbar[i]] = 1
                    cnt += 1
                else:
                    target[Vbar[i]] = 0

            res = MST(N, ABC, target, uf, cnt)
            ans = min(ans, res)
            if ans == mincost:
                return ans

        return ans

def main():
    N, M, T = NMI()
    ABC = EI(M)
    ABC = [[x-1, y-1, z] for x, y, z in ABC]
    V = [NI() for _ in range(T)]
    V = [x-1 for x in V]
    ans = min_steiner_tree(N, ABC, V)
    print(ans)


if __name__ == "__main__":
    main()
