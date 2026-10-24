"""重みなしグラフの複数始点BFS・最短路数・二部判定・DAG到達判定。
graph[v]は行き先頂点のlist、0-indexed。無向辺は両方向へ登録する。
各関数は入力を変更しない。整数bitsetのDAG到達判定はPyPy向け。

使い方（このファイル全体を貼り付けてから実行）
    g = [[1, 2], [0, 3], [0, 3], [1, 2]]
    multi_source_bfs(g, [0, 3])[0]  # => [0, 1, 1, 0]
    bfs_path_count(g, 0)  # => ([0, 1, 1, 2], [1, 1, 1, 2])
    bipartite_coloring(g)[1]  # => [(2, 2)]
    dag_reachability([[1, 2], [3], [3], []], [(0, 3), (3, 0), (2, 2)])
    # => [True, False, True]
"""

from collections import deque


def multi_source_bfs(graph, sources):
    """(dist,parent)を返す。各始点の距離0、未到達dist=-1、始点/未到達parent=-1。
    始点の重複は無視。O(N+M)。parentを辿ると最寄りの始点への最短路を復元できる。
    入力: graphはgraph[u]=[v,...]の隣接リスト（長さNのlist of lists）。
    頂点番号は0..N-1、N=len(graph)、M=sum(map(len,graph))。
    sourcesは始点の頂点番号を並べた列。空間O(N)、始点数Sの読み込みを含む時間O(N+M+S)。
    """
    dist, parent = [-1] * len(graph), [-1] * len(graph)
    queue = deque()
    for s in sources:
        assert 0 <= s < len(graph)
        if dist[s] < 0:
            dist[s] = 0
            queue.append(s)
    while queue:
        v = queue.popleft()
        for w in graph[v]:
            if dist[w] < 0:
                dist[w], parent[w] = dist[v] + 1, v
                queue.append(w)
    return dist, parent


def bfs_path_count(graph, source, mod=1000000007):
    """(最短距離list,最短経路数list)。未到達は(-1,0)、始点への空路は1通り。
    O(N+M)。平行辺は異なる経路として数える。mod=0なら厳密整数。
    入力: graphはgraph[u]=[v,...]の隣接リスト（長さNのlist of lists）。
    頂点番号は0..N-1、N=len(graph)、M=sum(map(len,graph))。
    sourceは始点の頂点番号、modは非負整数の法（0は剰余なし）。空間O(N)。
    """
    assert mod >= 0 and 0 <= source < len(graph)
    dist, ways = [-1] * len(graph), [0] * len(graph)
    dist[source], ways[source] = 0, 1 % mod if mod else 1
    queue = deque([source])
    while queue:
        v = queue.popleft()
        for w in graph[v]:
            if dist[w] < 0:
                dist[w] = dist[v] + 1
                queue.append(w)
            if dist[w] == dist[v] + 1:
                ways[w] += ways[v]
                if mod:
                    ways[w] %= mod
    return dist, ways


def bipartite_coloring(graph):
    """無向グラフの(0/1の色list,成分ごとの(色0数,色1数))。奇閉路があればNone。
    孤立点も1成分、自己ループは失敗。O(N+M)。graphは両方向の辺を含める。
    入力: graphはgraph[u]=[v,...]の隣接リスト（長さNのlist of lists）。
    頂点番号は0..N-1、N=len(graph)、M=sum(map(len,graph))。
    空間O(N)。無向辺(u,v)はgraph[u]にv、graph[v]にuを入れる。
    """
    color = [-1] * len(graph)
    counts = []
    for start in range(len(graph)):
        if color[start] >= 0:
            continue
        color[start] = 0
        count = [1, 0]
        queue = deque([start])
        while queue:
            v = queue.popleft()
            for w in graph[v]:
                if color[w] < 0:
                    color[w] = color[v] ^ 1
                    count[color[w]] += 1
                    queue.append(w)
                elif color[w] == color[v]:
                    return None
        counts.append(tuple(count))
    return color, counts


def dag_reachability(graph, queries, block_size=1024):
    """DAG上の(u,v)到達判定を入力順のbool listで返す。自分自身へはTrue。
    閉路があればValueError。Q件をB件ずつ整数bitsetでまとめて伝播する。
    O(ceil(Q/B)*(N+M)*ceil(B/w)+Q)程度、追加空間O(N*ceil(B/w)+Q)。
    wは多倍長整数の内部ワード幅。Bを増やすとループが減る一方、メモリが増える。
    入力: graphはgraph[u]=[v,...]の隣接リスト（長さNのlist of lists）。
    頂点番号は0..N-1、N=len(graph)、M=sum(map(len,graph))。
    queries=[(u,v),...]、Q=len(queries)。block_sizeは正の整数Bで、一度に処理する問い合わせ数。
    """
    assert block_size > 0
    n = len(graph)
    indeg = [0] * n
    for row in graph:
        for v in row:
            indeg[v] += 1
    order = [v for v in range(n) if indeg[v] == 0]
    for v in order:
        for w in graph[v]:
            indeg[w] -= 1
            if indeg[w] == 0:
                order.append(w)
    if len(order) != n:
        raise ValueError("graph must be acyclic")
    queries = list(queries)
    result = []
    for start in range(0, len(queries), block_size):
        block = queries[start : start + block_size]
        bits = [0] * n
        for i, (u, v) in enumerate(block):
            assert 0 <= u < n and 0 <= v < n
            bits[u] |= 1 << i
        for v in order:
            mask = bits[v]
            if mask:
                for w in graph[v]:
                    bits[w] |= mask
        result.extend(bool(bits[v] >> i & 1) for i, (_, v) in enumerate(block))
    return result
