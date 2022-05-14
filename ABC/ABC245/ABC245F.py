import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations

if "PyPy" in sys.version:
    import pypyjit

    pypyjit.set_param('max_unroll_recursion=-1')

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

# 縮約後のグラフを構築
def construct(N, G, label, group):
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


def adjlist_d_1to0(n, edges):
    res = [[] for _ in range(n)]
    for a, b in edges:
        a, b = a - 1, b - 1
        res[a].append(b)
    return res


def main():
    N, M = NMI()
    UV = [NLI() for _ in range(M)]
    VU = [(v, u) for u, v in UV]
    graph = adjlist_d_1to0(N, UV)
    inv_g = adjlist_d_1to0(N, VU)
    L, G = scc(N, graph, inv_g)
    # print(L)
    # print(G)
    G0, GP = construct(N, inv_g, L, G)
    # print(G0)
    # print(GP)

    ans = set()
    seen = set()
    for gi in range(len(GP)):
        if len(GP[gi]) <= 1:
            continue

        if gi in seen:
            continue

        D = deque([gi])
        seen.add(gi)
        while D:
            now = D.pop()
            ans |= set(GP[now])
            for goto in G0[now]:
                if goto in seen:
                    continue
                seen.add(goto)
                D.append(goto)

    print(len(ans))


if __name__ == "__main__":
    main()
