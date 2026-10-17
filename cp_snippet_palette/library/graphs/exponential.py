"""小さいグラフ向けの厳密解法。
出典: AOJ/DPL_2_A.py, AOJ/DPL_2_B.py, yuki_0114.py,
code_thanks_festival_2017_g.py, ARC171D。PyPy向け。整数bitsetは任意精度。
大きなnに使用しない。指数配列の大きさは各関数の説明を参照。
"""

from heapq import heapify, heappush, heappop


def tsp_cycle(distance, start=0, inf=1 << 60):
    """O(n²2^n)時間・O(n2^n)空間。全頂点を一度ずつ通りstartへ戻る最小コスト。
    到達不能の辺はinf。空グラフ・1頂点は0。解なしはinf。
    """
    n = len(distance)
    if n <= 1:
        return 0
    if not 0 <= start < n or any(len(row) != n for row in distance):
        raise ValueError("invalid distance matrix or start")
    dp = [[inf] * n for _ in range(1 << n)]
    dp[1 << start][start] = 0
    for mask in range(1 << n):
        for u, cost in enumerate(dp[mask]):
            if cost == inf:
                continue
            rest = ((1 << n) - 1) ^ mask
            while rest:
                bit = rest & -rest
                v = bit.bit_length() - 1
                if distance[u][v] != inf:
                    dp[mask | bit][v] = min(dp[mask | bit][v], cost + distance[u][v])
                rest ^= bit
    return min(
        (
            dp[-1][u] + distance[u][start]
            for u in range(n)
            if dp[-1][u] != inf and distance[u][start] != inf
        ),
        default=inf,
    )


def steiner_tree(n, edges, terminals, inf=1 << 60):
    """非負重み無向グラフ。O(3^t*n+2^t*(n+m)log n)、空間O(2^t*n)。
    多重辺可。端点が0/1個なら0。接続不能はinf。端点数tが小さい場合専用。
    """
    terminals = list(dict.fromkeys(terminals))
    if any(not 0 <= v < n for v in terminals):
        raise IndexError("invalid terminal")
    if len(terminals) <= 1:
        return 0
    graph = [[] for _ in range(n)]
    for u, v, cost in edges:
        if cost < 0:
            raise ValueError("negative edge")
        graph[u].append((v, cost))
        graph[v].append((u, cost))
    dp = [[inf] * n for _ in range(1 << len(terminals))]
    for i, v in enumerate(terminals):
        dp[1 << i][v] = 0
    for mask in range(1, len(dp)):
        sub = (mask - 1) & mask
        while sub:
            other = mask ^ sub
            if sub < other:
                for v in range(n):
                    dp[mask][v] = min(dp[mask][v], dp[sub][v] + dp[other][v])
            sub = (sub - 1) & mask
        q = [(d, v) for v, d in enumerate(dp[mask]) if d != inf]
        heapify(q)
        while q:
            d, u = heappop(q)
            if d != dp[mask][u]:
                continue
            for v, cost in graph[u]:
                if d + cost < dp[mask][v]:
                    dp[mask][v] = d + cost
                    heappush(q, (d + cost, v))
    return min(dp[-1])


def chinese_postman(n, edges, inf=1 << 60):
    """非負重み無向グラフの全辺を通る最短閉路。O(n³+k²2^k)、kは奇数次数頂点数。
    孤立点は無視。辺のある成分が非連結ならinf。空辺集合は0。
    """
    dist = [[inf] * n for _ in range(n)]
    degree = [0] * n
    total = 0
    for v in range(n):
        dist[v][v] = 0
    for u, v, cost in edges:
        if cost < 0:
            raise ValueError("negative edge")
        degree[u] += 1
        degree[v] += 1
        dist[u][v] = dist[v][u] = min(dist[u][v], cost)
        total += cost
    for k in range(n):
        for i in range(n):
            if dist[i][k] == inf:
                continue
            for j in range(n):
                if dist[k][j] != inf:
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    active = [v for v, d in enumerate(degree) if d]
    if active and any(dist[active[0]][v] == inf for v in active):
        return inf
    odds = [v for v, d in enumerate(degree) if d & 1]
    dp = [inf] * (1 << len(odds))
    dp[0] = 0
    for mask in range(1, len(dp)):
        first = mask & -mask
        i = first.bit_length() - 1
        rest = mask ^ first
        remaining = rest
        while remaining:
            bit = remaining & -remaining
            j = bit.bit_length() - 1
            dp[mask] = min(dp[mask], dp[rest ^ bit] + dist[odds[i]][odds[j]])
            remaining ^= bit
    return total + dp[-1]


def maximum_independent_set(graph):
    """分枝探索、最悪O(2^n)。無向・自己ループなし。解の頂点リストを返す。"""
    n = len(graph)
    adjacency = [sum(1 << v for v in set(row)) for row in graph]
    if any(adjacency[u] & (1 << u) for u in range(n)):
        raise ValueError("self loops not supported")
    best = []
    stack = [((1 << n) - 1, [])]
    while stack:
        mask, chosen = stack.pop()
        if len(chosen) + mask.bit_count() <= len(best):
            continue
        if not mask:
            best = chosen
            continue
        vertices = [v for v in range(n) if (mask >> v) & 1]
        u = max(vertices, key=lambda v: (adjacency[v] & mask).bit_count())
        rest = mask & ~(1 << u)
        if adjacency[u] & mask:
            stack.append((rest, chosen))
        stack.append((rest & ~adjacency[u], chosen + [u]))
    return best


def chromatic_number(graph):
    """独立集合DP＋包除原理。O(n*2^n)回の整数演算、空間O(2^n)。
    無向・自己ループなし。巨大な中間整数を正確に扱うためPyPy専用。
    """
    n = len(graph)
    adjacency = [sum(1 << v for v in set(row)) for row in graph]
    if any(adjacency[u] & (1 << u) for u in range(n)):
        raise ValueError("self loops not supported")
    if n == 0:
        return 0
    independent = [0] * (1 << n)
    independent[0] = 1
    for mask in range(1, 1 << n):
        bit = mask & -mask
        u = bit.bit_length() - 1
        rest = mask ^ bit
        independent[mask] = independent[rest] + independent[rest & ~adjacency[u]]
    terms = [-1 if (n - mask.bit_count()) & 1 else 1 for mask in range(1 << n)]
    for colors in range(1, n + 1):
        total = 0
        for mask in range(1 << n):
            terms[mask] *= independent[mask]
            total += terms[mask]
        if total:
            return colors
    return n
