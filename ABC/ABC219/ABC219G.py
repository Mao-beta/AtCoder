import sys
import math
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def adjlist_nond_1to0(n, edges):
    res = [[] for _ in range(n)]
    for a, b in edges:
        a, b = a-1, b-1
        res[a].append(b)
        res[b].append(a)
    return res


def main():
    """解説AC"""
    N, M, Q = NMI()
    edges = [NLI() for _ in range(M)]
    graph = adjlist_nond_1to0(N, edges)
    X = NLI()
    X = [x-1 for x in X]

    # 次数B以上ならば書き換えを遅延させる
    B = int(M**0.5)
    # 各頂点が次数B以上かどうか
    is_large = [0] * N
    for i in range(N):
        if len(graph[i]) >= B:
            is_large[i] = 1

    # 頂点の値
    V = [i for i in range(N)]
    # その頂点を最後に書き換えたクエリ
    Last = [-1] * N
    # 隣接する点の中で次数B以上の集合
    large_neighbors = [[] for _ in range(N)]
    for i, adj in enumerate(graph):
        for goto in adj:
            if is_large[goto]:
                large_neighbors[i].append(goto)

    # 次数B以上の頂点に立てる「看板」
    # 看板のある頂点に隣接している点は、qによりvgになっていることとする
    # Xで指定された点がこれを見に来て、Last[x]より後のクエリを優先
    Lazy = [[-1, -1] for _ in range(N)] # [q, vg]

    for i, x in enumerate(X):
        v = V[x]
        l = Last[x]
        # 隣接する次数B以上の頂点にある看板を見に行く
        for goto in large_neighbors[x]:
            q, vg = Lazy[goto]
            if l < q:
                l = q
                v = vg

        # xの情報を正しく更新
        Last[x] = l
        V[x] = v

        # 次数B以上なら看板を立てるだけ
        if is_large[x]:
            Lazy[x][0] = i
            Lazy[x][1] = v

        # B未満なら全部ここで処理してしまう
        else:
            for goto in graph[x]:
                V[goto] = v
                Last[goto] = i

    # 最後に看板を全部見て正しくする
    for x in range(N):
        v = V[x]
        l = Last[x]
        for goto in large_neighbors[x]:
            q, vg = Lazy[goto]
            if l < q:
                l = q
                v = vg
        V[x] = v

    V = [v+1 for v in V]
    print(*V)


if __name__ == "__main__":
    main()
