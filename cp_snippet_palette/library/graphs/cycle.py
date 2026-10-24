"""有向・無向グラフから閉路を1つ復元する。非再帰DFS、O(N+M)。
自己ループ・多重辺に対応。0-indexed。PyPy向け、Codon未確認。

使い方（このファイルを解答の先頭に貼り付けてから実行）
    vertices, edge_ids = find_cycle(3, [(0, 1), (1, 2), (2, 0)])
    vertices, edge_ids  # => ([0, 1, 2], [0, 1, 2])
    find_cycle(2, [(0, 1)], directed=False) is None  # => True
    find_cycle(2, [(0, 1), (0, 1)], directed=False)  # => ([0, 1], [0, 1])
"""


def find_cycle(n, edges, directed=True):
    """edges=[(u,v),...]から(vertices,edge_ids)を返す。閉路がなければNone。
    edge_ids[i]はvertices[i]からvertices[(i+1)%L]への辺。始点を末尾に重ねない。
    directed=Falseでは辺を無向として扱う。辺IDは入力順。O(N+M)。
    nは頂点数N、M=len(edges)。u/vは0..n-1。自己ループ・多重辺も可。空間O(N+M)。
    """
    graph = [[] for _ in range(n)]
    for i, (u, v) in enumerate(edges):
        graph[u].append((v, i))
        if not directed:
            graph[v].append((u, i))
    color, parent, parent_edge = [0] * n, [-1] * n, [-1] * n
    for start in range(n):
        if color[start]:
            continue
        color[start] = 1
        stack = [(start, 0)]
        while stack:
            u, index = stack[-1]
            if index == len(graph[u]):
                color[u] = 2
                stack.pop()
                continue
            v, eid = graph[u][index]
            stack[-1] = u, index + 1
            if not directed and eid == parent_edge[u]:
                continue
            if not color[v]:
                color[v], parent[v], parent_edge[v] = 1, u, eid
                stack.append((v, 0))
            elif color[v] == 1:
                vertices, ids, x = [u], [eid], u
                while x != v:
                    ids.append(parent_edge[x])
                    x = parent[x]
                    vertices.append(x)
                return vertices[::-1], ids[:0:-1] + ids[:1]
    return None
