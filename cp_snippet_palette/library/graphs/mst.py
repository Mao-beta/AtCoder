"""Kruskal法。出典: ARC076D, ABC282E。O(E log E)、0-indexed。

多重辺・負辺・非連結に対応。最小全域森の(重み, 採用辺ID, 成分数)を返す。
PyPy向け。Codonでは重みの総和を64bit以内にする。

使い方（このファイルを解答の先頭に貼り付けてから実行）
    minimum_spanning_forest(3, [(0, 1, 4), (1, 2, 2), (0, 2, 9)])  # => (6, [1, 0], 1)
"""


def minimum_spanning_forest(n, edges):
    """n頂点・無向辺edges=[(u,v,cost),...]の最小全域森。0-indexed。
    戻り値(重み合計,採用した入力辺IDのlist,成分数)。成分数1なら全域木。
    非連結・負辺・多重辺可。入力非破壊、O(E log E)。
    nは非負整数の頂点数、E=len(edges)。costは整数。孤立点も含め時間O(n+E log(E+1))、空間O(n+E)。
    """
    parent = [-1] * n

    def leader(v):
        while parent[v] >= 0:
            p = parent[v]
            if parent[p] >= 0:
                parent[v] = parent[p]
            v = p
        return v

    total, components, selected = 0, n, []
    for eid in sorted(range(len(edges)), key=lambda i: edges[i][2]):
        u, v, cost = edges[eid]
        u, v = leader(u), leader(v)
        if u == v:
            continue
        if parent[u] > parent[v]:
            u, v = v, u
        parent[u] += parent[v]
        parent[v] = u
        components -= 1
        total += cost
        selected.append(eid)
    return total, selected, components
