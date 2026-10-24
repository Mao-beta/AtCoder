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

# ライブラリ https://github.com/Mao-beta/AtCoder

'dijkstra — graph[u]=[(v,非負重み),...]と始点sourceを受け取り(dist,parent)を返す。'

from heapq import heappush, heappop


def dijkstra(graph, source, inf=1 << 60):
    """graph[u]=[(v,非負重み),...]と始点sourceを受け取り(dist,parent)を返す。
    未到達dist=inf、parent=-1。有限な最短距離の上限より大きなinfを指定する。
    経路はrestore_path(parent,source,target)で復元。O((V+E)log(V+E+2))。
    入力: graphはgraph[u]=[(v,cost),...]の重み付き隣接リスト。頂点番号は0..N-1、N=len(graph)、Mは格納した有向辺の総数。
     sourceは始点。計算量のV/EはN/Mと同じ。追加空間はDijkstraがO(N+M)、0-1 BFSがO(N+M)以内。
    """
    n = len(graph)
    if not 0 <= source < n:
        raise IndexError(source)
    dist, parent = [inf] * n, [-1] * n
    dist[source] = 0
    heap = [(0, source)]
    while heap:
        d, u = heappop(heap)
        if d != dist[u]:
            continue
        for v, cost in graph[u]:
            if cost < 0:
                raise ValueError("Dijkstra requires nonnegative costs")
            nd = d + cost
            if nd < dist[v]:
                dist[v] = nd
                parent[v] = u
                heappush(heap, (nd, v))
    return dist, parent



def main():
    N, M, S, T = NMI()
    AB = EI(M)
    AB = [[x-1, y-1] for x, y in AB]
    G = [[] for _ in range(N)]
    for u, v in AB:
        G[u].append(v)
    for u in range(N):
        G[u].sort()
        G[u] = [[v, int(i!=0)] for i, v in enumerate(G[u])]
    D, P = dijkstra(G, S-1)
    ans = D[T-1]
    print(ans if ans < (1<<60) else -1)


if __name__ == "__main__":
    main()
