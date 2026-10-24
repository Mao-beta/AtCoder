"""隣接リスト・最短路。出典: _test.py, _Graph_Algorithm.py。
0-indexed。重み付き隣接リストはgraph[u]=[(v,cost), ...]。

到達不能はinf（指定可）。Codonでは有限距離と加算の途中を64bit以内にする。

使い方（このファイルを解答の先頭に貼り付けてから実行）
    adjlist(3, [(1, 2), (2, 3)], first_index=1)  # => [[1], [0, 2], [1]]
    g = weighted_adjlist(3, [(0, 1, 2), (1, 2, 3)], directed=True)
    dist, parent = dijkstra(g, 0)
    dist, restore_path(parent, 0, 2)  # => ([0, 2, 5], [0, 1, 2])
    zero_one_bfs([[(1, 0)], [(2, 1)], []], 0)  # => [0, 0, 1]
    bellman_ford(3, [(0, 1, -2), (1, 2, 3)], 0)  # => ([0, -2, 1], [False, False, False])
    floyd_warshall(2, [(0, 1, 4)], directed=False)  # => [[0, 4], [4, 0]]
    topological_sort([[1], [2], []])  # => [0, 1, 2]
"""

from heapq import heappush, heappop
from collections import deque


def adjlist(n, edges, directed=False, first_index=0):
    """edges=[(u,v),...]から長さnの隣接リストを作る。
    directed=Falseは両方向、Trueはu→vのみ。first_index=1なら入力の頂点番号から1を引く。
    結果の頂点番号は常に0-indexed。
    nは頂点数の非負整数。E=len(edges)。時間・出力空間O(n+E)。first_indexは入力の頂点番号の開始値（0または1）。
    """
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
    """edges=[(u,v,weight),...]からgraph[u]=[(v,weight),...]を作る。
    directed=Falseは両方向。first_index=1で1-indexedの入力を0-indexedへ変換する。
    nは頂点数の非負整数。E=len(edges)。時間・出力空間O(n+E)。first_indexは入力の頂点番号の開始値（0または1）。
    """
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
    """graph[u]=[(v,非負重み),...]と始点sourceを受け取り(dist,parent)を返す。
    未到達dist=inf、parent=-1。有限な最短距離の上限より大きなinfを指定する。
    経路はrestore_path(parent,source,target)で復元。O((V+E)log(V+E+2))。
    入力: graphはgraph[u]=[(v,cost),...]の重み付き隣接リスト。頂点番号は0..N-1、N=len(graph)、Mは格納した有向辺の総数。
     sourceは始点。計算量のV/EはN/Mと同じ。追加空間はDijkstraがO(N+M)、0-1 BFSがO(N+M)以内。
    """
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
    """到達不能なら[]。source自身への経路は[source]。
    入力: parentはDijkstraなどが返した長さNの親頂点配列（始点・未到達=-1）。source/targetは始点/終点の頂点番号。
    時間・出力空間O(経路長)、最悪O(N)。
    """
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
    """graph[u]=[(v,重み),...]で全重みが0か1の場合の距離list。未到達はinf。
    頂点は0-indexed、経路復元用の親は返さない。O(V+E)。
    入力: graphはgraph[u]=[(v,cost),...]の重み付き隣接リスト。頂点番号は0..N-1、N=len(graph)、Mは格納した有向辺の総数。
     sourceは始点。計算量のV/EはN/Mと同じ。追加空間はDijkstraがO(N+M)、0-1 BFSがO(N+M)以内。
    """
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
    """有向辺edges=[(u,v,cost),...]と始点sourceから(dist,negative)を返す。O(VE)。
    negative[v]は始点から到達可能な負閉路の影響を受けるか。Trueのdistは使わない。
    未到達はinf。無向辺は両方向の辺を入力する。
    nは頂点数、V=n、E=len(edges)。edgesのu/v/sourceは0-indexed、costは整数で負も可。infは全ての有限な最短距離より大きい番兵。
    追加空間O(V+E)。
    """
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
    """edges=[(u,v,cost),...]から全点対距離の二次元listを返す。O(V³)。
    directed=Falseなら両方向を追加。未到達はinf、多重辺は最小重み。
    dist[v][v]<0なら負閉路があり、影響を受ける距離を最短距離として使えない。
    nは頂点数、V=n、E=len(edges)。edgesのu/v/sourceは0-indexed、costは整数で負も可。infは全ての有限な最短距離より大きい番兵。
    空間O(V²)。directedは有向辺として扱うかを表すbool。
    """
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
    """有向隣接リストgraph[u]=[v,...]のトポロジカル順（頂点のlist）。O(V+E)。
    閉路があればValueError。同順位の頂点間の辞書順最小性は保証しない。
    入力: graphはgraph[u]=[v,...]の隣接リスト（長さNのlist of lists）。
    頂点番号は0..N-1、N=len(graph)、M=sum(map(len,graph))。 計算量のV/EはN/M。追加空間O(N)。
    """
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
