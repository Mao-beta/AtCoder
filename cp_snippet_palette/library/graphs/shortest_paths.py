"""隣接リスト・最短路。出典: _test.py, _Graph_Algorithm.py。
0-indexed。重み付き隣接リストはgraph[u]=[(v,cost), ...]。
到達不能はinf（指定可）。Codonでは有限距離と加算の途中を64bit以内にする。
"""

from heapq import heappush, heappop
from collections import deque


def adjlist(n, edges, directed=False, first_index=0):
    graph = [[] for _ in range(n)]
    for u, v in edges:
        u -= first_index
        v -= first_index
        if not (0 <= u < n and 0 <= v < n):
            raise IndexError("invalid endpoint")
        graph[u].append(v)
        if not directed:
            graph[v].append(u)
    return graph


def weighted_adjlist(n, edges, directed=False, first_index=0):
    graph = [[] for _ in range(n)]
    for u, v, cost in edges:
        u -= first_index
        v -= first_index
        if not (0 <= u < n and 0 <= v < n):
            raise IndexError("invalid endpoint")
        graph[u].append((v, cost))
        if not directed:
            graph[v].append((u, cost))
    return graph


def dijkstra(graph, source, inf=1 << 60):
    """非負辺。O((V+E)log V)。距離配列と経路復元用の親配列を返す。"""
    n = len(graph)
    if not 0 <= source < n:
        raise IndexError(source)
    dist, parent = [inf] * n, [-1] * n
    dist[source] = 0
    heap = [(0, source)]
    while heap:
        d, u = heappop(heap)
        if d != dist[u]:
            continue
        for v, cost in graph[u]:
            if cost < 0:
                raise ValueError("Dijkstra requires nonnegative costs")
            nd = d + cost
            if nd < dist[v]:
                dist[v] = nd
                parent[v] = u
                heappush(heap, (nd, v))
    return dist, parent


def restore_path(parent, source, target):
    """到達不能なら[]。source自身への経路は[source]。"""
    path = []
    for _ in range(len(parent)):
        path.append(target)
        if target == source:
            return path[::-1]
        target = parent[target]
        if target == -1:
            return []
    raise ValueError("parent array contains a cycle")


def zero_one_bfs(graph, source, inf=1 << 60):
    """辺重み0/1専用。O(V+E)。距離配列を返す。"""
    if not 0 <= source < len(graph):
        raise IndexError(source)
    dist = [inf] * len(graph)
    dist[source] = 0
    q = deque([(source, 0)])
    while q:
        u, d = q.popleft()
        if d != dist[u]:
            continue
        for v, cost in graph[u]:
            if cost not in (0, 1):
                raise ValueError("cost must be 0 or 1")
            if d + cost < dist[v]:
                dist[v] = d + cost
                if cost:
                    q.append((v, d + cost))
                else:
                    q.appendleft((v, d))
    return dist


def bellman_ford(n, edges, source, inf=1 << 60):
    """O(VE)。distと、到達可能な負閉路の影響を受ける頂点のbool配列。"""
    if not 0 <= source < n:
        raise IndexError(source)
    dist = [inf] * n
    dist[source] = 0
    for _ in range(n - 1):
        updated = False
        for u, v, cost in edges:
            if dist[u] != inf and dist[u] + cost < dist[v]:
                dist[v] = dist[u] + cost
                updated = True
        if not updated:
            break
    graph = [[] for _ in range(n)]
    negative = [False] * n
    todo = []
    for u, v, cost in edges:
        graph[u].append(v)
        if dist[u] != inf and dist[u] + cost < dist[v] and not negative[v]:
            negative[v] = True
            todo.append(v)
    for u in todo:
        for v in graph[u]:
            if not negative[v]:
                negative[v] = True
                todo.append(v)
    return dist, negative


def floyd_warshall(n, edges, directed=True, inf=1 << 60):
    """O(V³)。多重辺対応。負閉路はdist[v][v]<0で判定。"""
    dist = [[inf] * n for _ in range(n)]
    for v in range(n):
        dist[v][v] = 0
    for u, v, cost in edges:
        dist[u][v] = min(dist[u][v], cost)
        if not directed:
            dist[v][u] = min(dist[v][u], cost)
    for k in range(n):
        for i in range(n):
            if dist[i][k] == inf:
                continue
            d = dist[i][k]
            for j in range(n):
                if dist[k][j] != inf:
                    dist[i][j] = min(dist[i][j], d + dist[k][j])
    return dist


def topological_sort(graph):
    """O(V+E)。閉路がある場合はValueError。"""
    indegree = [0] * len(graph)
    for row in graph:
        for v in row:
            indegree[v] += 1
    order = [v for v, degree in enumerate(indegree) if degree == 0]
    for u in order:
        for v in graph[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                order.append(v)
    if len(order) != len(graph):
        raise ValueError("graph contains a cycle")
    return order
