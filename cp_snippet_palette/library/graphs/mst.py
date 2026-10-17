"""Kruskal法。出典: ARC076D, ABC282E。O(E log E)、0-indexed。
多重辺・負辺・非連結に対応。最小全域森の(重み, 採用辺ID, 成分数)を返す。
PyPy向け。Codonでは重みの総和を64bit以内にする。
"""


def minimum_spanning_forest(n, edges):
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
