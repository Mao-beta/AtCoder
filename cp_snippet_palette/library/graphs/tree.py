"""木のEuler順・直径・巡回列復元。出典: _test.py, _Graph_Algorithm.py。
0-indexed、非再帰。無向木を前提とする。PyPy向け。
"""


def euler_tour(graph, root=0):
    """O(n)。order,tin,tout,parent。部分木はorder[tin[v]:tout[v]]。"""
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
    """重みなし無向木。O(n)。直径の長さと、その経路を返す。"""
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
    _, path = tree_diameter(graph)
    if not path:
        return []
    return path[(len(path) - 1) // 2 : len(path) // 2 + 1]


def postorder_from_preorder_inorder(preorder, inorder):
    """要素は重複しない。O(n)。前順・中順から後順を復元。"""
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
