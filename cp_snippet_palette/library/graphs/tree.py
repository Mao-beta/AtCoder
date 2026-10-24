"""木のEuler順・直径・巡回列復元。出典: _test.py, _Graph_Algorithm.py。
0-indexed、非再帰。無向木を前提とする。PyPy向け。

使い方（このファイルを解答の先頭に貼り付けてから実行）
    g = [[1], [0, 2], [1]]
    order, tin, tout, parent = euler_tour(g)
    order[tin[1]:tout[1]], parent  # => ([1, 2], [-1, 0, 1])
    length, path = tree_diameter(g)
    length, sorted(path), tree_centers(g)  # => (2, [0, 1, 2], [1])
    postorder_from_preorder_inorder([1, 2, 3], [2, 1, 3])  # => [2, 3, 1]
    weighted_tree_diameter([[(1, 5)], [(0, 5), (2, 7)], [(1, 7)]])[0]  # => 12
"""


def euler_tour(graph, root=0):
    """無向木graph（隣接頂点のlist）をrootからDFSし、(order,tin,tout,parent)を返す。
    各頂点はorderに一度だけ現れ、部分木はorder[tin[v]:tout[v]]。parent[root]=-1。
    出入りで2回ずつ記録するEuler tourとは異なる。0-indexed、O(n)。
    入力: graphはgraph[u]=[v,...]の隣接リスト（長さNのlist of lists）。
    頂点番号は0..N-1、N=len(graph)、M=sum(map(len,graph))。 無向木なので辺は両方向へ格納する。n=N、時間・空間O(N)。
    rootは根とする頂点番号（0-indexed）。
    """
    n = len(graph)
    if n == 0:
        return [], [], [], []
    parent = [-2] * n
    parent[root] = -1
    tin, tout, order = [0] * n, [0] * n, []
    stack = [root]
    while stack:
        u = stack.pop()
        if u < 0:
            tout[~u] = len(order)
            continue
        tin[u] = len(order)
        order.append(u)
        stack.append(~u)
        for v in reversed(graph[u]):
            if v == parent[u]:
                continue
            if parent[v] != -2:
                raise ValueError("graph must be a tree")
            parent[v] = u
            stack.append(v)
    if len(order) != n:
        raise ValueError("graph must be connected")
    return order, tin, tout, parent


def tree_diameter(graph):
    """重みなし無向木。O(n)。直径の長さと、その経路を返す。
    入力: graphはgraph[u]=[v,...]の隣接リスト（長さNのlist of lists）。
    頂点番号は0..N-1、N=len(graph)、M=sum(map(len,graph))。 無向木なので辺は両方向へ格納する。n=N、時間・空間O(N)。
    """
    if not graph:
        return 0, []

    def farthest(start):
        distance, parent = [-1] * len(graph), [-1] * len(graph)
        distance[start] = 0
        order = [start]
        for u in order:
            for v in graph[u]:
                if distance[v] == -1:
                    distance[v] = distance[u] + 1
                    parent[v] = u
                    order.append(v)
        if len(order) != len(graph):
            raise ValueError("graph must be connected")
        return order[-1], distance, parent

    s, _, _ = farthest(0)
    t, distance, parent = farthest(s)
    path = []
    v = t
    while v != -1:
        path.append(v)
        v = parent[v]
    return distance[t], path[::-1]


def tree_centers(graph):
    """重みなし無向木の中心頂点のlist（1個か2個）。空なら[]。
    中心は全頂点への最大距離を最小化する頂点。重心とは異なる。O(n)。
    入力: graphはgraph[u]=[v,...]の隣接リスト（長さNのlist of lists）。
    頂点番号は0..N-1、N=len(graph)、M=sum(map(len,graph))。 無向木なので辺は両方向へ格納する。n=N、時間・空間O(N)。
    """
    _, path = tree_diameter(graph)
    if not path:
        return []
    return path[(len(path) - 1) // 2 : len(path) // 2 + 1]


def weighted_tree_diameter(graph):
    """非負重みの無向木graph[u]=[(v,weight),...]の(直径長,頂点経路)を返す。
    空は(0,[])。重み0を許すが負重みは不可。O(N)、非再帰。
    入力: graphはgraph[u]=[(v,cost),...]の重み付き隣接リスト。頂点番号は0..N-1、N=len(graph)、Mは格納した有向辺の総数。
     木の辺は同じcostで両方向へ格納する。空間O(N)。
    """
    n = len(graph)
    if not n:
        return 0, []

    def farthest(start):
        distance, parent = [0] * n, [-2] * n
        parent[start] = -1
        order = [start]
        for u in order:
            for v, w in graph[u]:
                if w < 0:
                    raise ValueError("negative tree weight")
                if v == parent[u]:
                    continue
                if parent[v] != -2:
                    raise ValueError("graph must be a tree")
                parent[v] = u
                distance[v] = distance[u] + w
                order.append(v)
        if len(order) != n:
            raise ValueError("graph must be connected")
        end = max(range(n), key=distance.__getitem__)
        return end, distance[end], parent

    s, _, _ = farthest(0)
    t, length, parent = farthest(s)
    path = []
    while t != -1:
        path.append(t)
        t = parent[t]
    return length, path[::-1]


def postorder_from_preorder_inorder(preorder, inorder):
    """要素は重複しない。O(n)。前順・中順から後順を復元。
    preorder/inorderは同じN個の相異なるhashableな頂点ラベルを前順/中順に並べた列。n=N。時間・空間O(N)。
    """
    if len(preorder) != len(inorder) or len(set(inorder)) != len(inorder):
        raise ValueError("distinct nodes and matching lengths required")
    positions = {x: i for i, x in enumerate(inorder)}
    if len(set(preorder)) != len(preorder) or set(preorder) != set(inorder):
        raise ValueError("node sets differ")
    result = []
    stack = [(0, 0, len(inorder), False)]
    while stack:
        p, left, right, done = stack.pop()
        if left == right:
            continue
        value = preorder[p]
        if done:
            result.append(value)
            continue
        mid = positions[value]
        if not left <= mid < right:
            raise ValueError("inconsistent traversals")
        stack.append((p, left, right, True))
        stack.append((p + mid - left + 1, mid + 1, right, False))
        stack.append((p + 1, left, mid, False))
    return result
