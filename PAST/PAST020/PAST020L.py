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


def get_tree_center_info(N, AB, in_origin=1):
    """
    木について、頂点数と辺のリストから頂点を倍加(2*N-1個に)して木の中心を返す O(V+E)
    元の辺の中点に点を作る(辺番号+N)ので中心は一点に定まる
    :return: 中心のindex, 直径, 中心を根とした各点の距離, 隣接グラフ(0-index)
    """
    N2 = 2 * N - 1
    G = [[] for _ in range(N2)]

    # グラフ構築: 辺の中点(i+N)を作って接続
    for i, (a, b) in enumerate(AB):
        a -= in_origin
        b -= in_origin
        v = i + N
        G[a].append(v)
        G[b].append(v)
        G[v].append(a)
        G[v].append(b)

    # BFS関数 (距離と最遠点を求める)
    def bfs(start_node):
        dists = [-1] * N2
        q = deque([start_node])
        dists[start_node] = 0
        max_dist = 0
        furthest_node = start_node

        while q:
            now = q.popleft()
            d = dists[now]
            if d > max_dist:
                max_dist = d
                furthest_node = now

            for nxt in G[now]:
                if dists[nxt] == -1:
                    dists[nxt] = d + 1
                    q.append(nxt)
        return furthest_node, max_dist, dists

    # 1. 適当な点(0)から最も遠い点 u を求める
    u, _, _ = bfs(0)

    # 2. uから最も遠い点 v を求める (u-vが直径)
    v, diameter, dists_from_u = bfs(u)

    # 3. 直径の中点を特定 (直径パス上で端点からの距離が半径と等しい点)
    _, _, dists_from_v = bfs(v)
    cent = -1
    radius = diameter // 2
    for i in range(N2):
        # 直径パス上にあり、かつuからの距離が半径と等しい点
        if dists_from_u[i] == radius and dists_from_v[i] == radius:
            cent = i
            break

    # 4. 中心からの距離を計算
    _, _, dists_from_center = bfs(cent)

    return cent, diameter, dists_from_center, G


def main():
    N = NI()
    AB = EI(N-1)
    cent, D, dists, G = get_tree_center_info(N, AB, in_origin=1)
    N2 = 2*N-1

    # centを根として木DP v以下の部分木における距離D/2の葉の数
    # print(cent, D, dists, G)
    dp = [0] * N2
    total = 0
    stack = deque()
    stack.append([~cent, N2])
    stack.append([cent, N2])
    while stack:
        now, par = stack.pop()
        if now >= 0:
            for nxt in G[now]:
                if nxt != par:
                    stack.append([~nxt, now])
                    stack.append([nxt, now])
        else:
            now = ~now
            if dists[now] == D//2:
                total += 1
                dp[now] = 1
            if par < N2:
                dp[par] += dp[now]
    ans = 0
    for v in G[now]:
        ans += dp[v] * (total - dp[v])
    print(ans // 2)


if __name__ == "__main__":
    main()
