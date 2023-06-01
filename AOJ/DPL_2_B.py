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


def chinese_postman_problem(N: int, E: list):
    """
    中国人郵便配達問題
    重み付き無向グラフの全ての辺を1度以上通って始点に帰る最短経路長
    多重辺OK 負のコストはたぶんダメ ワーシャルフロイド+bitDP
    O(len(E) + N^3 + 2^N*N^2)
    :param N: 頂点数
    :param E: 辺のリスト [[u, v, w],...]
    :return: 最短経路長
    """
    INF = 10**20
    dims = [0] * N
    D = [[INF]*N for _ in range(N)]

    for u, v, w in E:
        D[u][v] = min(D[u][v], w)
        D[v][u] = min(D[v][u], w)
        dims[u] += 1
        dims[v] += 1

    # ワーシャルフロイド
    for k in range(N):
        for i in range(N):
            for j in range(N):
                D[i][j] = min(D[i][j], D[i][k] + D[k][j])

    # 奇点どうしを2個ずつマッチング
    odds = [i for i, d in enumerate(dims) if d % 2]
    n = len(odds)
    assert n % 2 == 0

    costs = [INF] * (1<<n)
    costs[0] = 0

    for case in range(1<<n):
        now = costs[case]
        for i in range(n):
            if (case >> i) & 1:
                continue

            for j in range(i+1, n):
                if (case >> j) & 1:
                    continue

                new_c = case | (1<<i) | (1<<j)
                d = D[odds[i]][odds[j]]
                if now + d < costs[new_c]:
                    costs[new_c] = now + d
            break

    # 奇点どうしのコスト＋全ての辺のコスト
    return costs[-1] + sum([w for _, _, w in E])


def main():
    N, M = NMI()
    edges = EI(M)
    edges = [[x-1, y-1, w] for x, y, w in edges]
    ans = chinese_postman_problem(N, edges)
    print(ans)


if __name__ == "__main__":
    main()
