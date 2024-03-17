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


# 強連結成分分解(SCC): グラフGに対するSCCを行う
# 入力: <N>: 頂点サイズ, <G>: 順方向の有向グラフ, <RG>: 逆方向の有向グラフ
# 出力: (<ラベル数>, <各頂点のラベル番号>) トポロジカルソート済
# 計算量: O(V+E)
def scc(N, G, RG):
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


def construct(N, G, label, group):
    """
    縮約後のグラフを構築: トポソ済み
    G0: 各強連結成分の遷移先の集合
    GP: 各強連結成分内の元の頂点のリスト
    """
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


def make_adjlist_d(n, edges):
    res = [[] for _ in range(n)]
    for edge in edges:
        res[edge[0]].append(edge[1])
    return res


def main():
    N = NI()
    L = []
    G = [[] for _ in range(N)]
    RG = [[] for _ in range(N)]
    for i in range(N):
        l, s = NMI()
        s -= 1
        L.append(l)
        G[s].append(i)
        RG[i].append(s)
    label, group = scc(N, G, RG)
    G0, GP = construct(N, G, label, group)
    ans = 0
    dims = [0] * len(G0)
    for i, (g0, gp) in enumerate(zip(G0, GP)):
        for g in g0:
            dims[g] = 1
        ls = [L[g] for g in gp]
        ls.sort()
        ans += sum(ls)
        if dims[i] == 0:
            ans += ls[0]
    print(f"{ans / 2:.1f}")


if __name__ == "__main__":
    main()
