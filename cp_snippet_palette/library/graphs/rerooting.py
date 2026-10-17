"""全方位木DP。出典: _Rerooting.py。非再帰O(n)。
mergeは結合的、identityは不変な単位元。lift(value, from_vertex, to_vertex)で辺を跨ぐ。
戻り値は各頂点での隣接方向からの寄与のmerge。辺の順序を保持する。
PyPy向け。Codonでのコールバックの型推論は未確認。
"""


def rerooting(graph, merge, identity, lift, root=0):
    n = len(graph)
    if n == 0:
        return []
    parent = [-2] * n
    parent[root] = -1
    order = [root]
    for u in order:
        for v in graph[u]:
            if v == parent[u]:
                continue
            if parent[v] != -2:
                raise ValueError("graph must be a tree")
            parent[v] = u
            order.append(v)
    if len(order) != n:
        raise ValueError("graph must be connected")
    down = [identity] * n
    for u in reversed(order):
        value = identity
        for v in graph[u]:
            if v != parent[u]:
                value = merge(value, lift(down[v], v, u))
        down[u] = value
    up = [identity] * n
    answer = [identity] * n
    for u in order:
        values = [up[u] if v == parent[u] else lift(down[v], v, u) for v in graph[u]]
        prefix = [identity]
        for value in values:
            prefix.append(merge(prefix[-1], value))
        answer[u] = prefix[-1]
        suffix = identity
        for i in range(len(values) - 1, -1, -1):
            v = graph[u][i]
            if v != parent[u]:
                up[v] = lift(merge(prefix[i], suffix), u, v)
            suffix = merge(values[i], suffix)
    return answer
