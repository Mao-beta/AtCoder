"""全方位木DP。出典: _Rerooting.py。非再帰O(n)。
mergeは結合的、identityは不変な単位元。lift(value, from_vertex, to_vertex)で辺を跨ぐ。

戻り値は各頂点での隣接方向からの寄与のmerge。辺の順序を保持する。
PyPy向け。Codonでのコールバックの型推論は未確認。

使い方（このファイルを解答の先頭に貼り付けてから実行）
    g = [[1], [0, 2], [1]]
    rerooting(g, max, 0, lambda value, src, dst: value + 1)  # => [2, 1, 2]

上の例は各頂点から最遠頂点への辺数。距離和なら(頂点数,距離和)を持つ。
    merge = lambda a, b: (a[0] + b[0], a[1] + b[1])
    lift = lambda value, src, dst: (value[0] + 1, value[1] + value[0] + 1)
    [total for count, total in rerooting(g, merge, (0, 0), lift)]  # => [3, 2, 3]
"""


def rerooting(graph, merge, identity, lift, root=0):
    """無向木の隣接リストgraphに対し、各頂点を根にしたDP値のlistを返す。
    merge(a,b)は結合的演算、identityは不変な単位元。
    lift(value,from_vertex,to_vertex)はfrom側の集約値を辺越しの寄与へ変換する。
    自身の頂点の寄与は自動では入らないためliftに含める。隣接順序を保持する。
    rootは処理順のための根（結果は全頂点分）。各コールバックO(1)なら全体O(n)。
    入力: graphはgraph[u]=[v,...]の隣接リスト（長さNのlist of lists）。
    頂点番号は0..N-1、N=len(graph)、M=sum(map(len,graph))。 無向木の各辺を両方向に格納する。rootは0..N-1。
    merge/liftは値を変更しない関数、identityはその集約型の単位元。空間O(N)。
    """
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
