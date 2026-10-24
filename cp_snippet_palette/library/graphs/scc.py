"""強連結成分分解・2-SAT。shakayami/ACL-for-pythonと同じ関数API。
非再帰、O(N+M)。このファイルだけで使用可能。PyPy向け、Codon未確認。

使い方（このファイルを解答の先頭に貼り付けてから実行）
    edges = [(0, 1), (1, 0), (1, 2)]
    scc(3, edges)  # => [[0, 1], [2]]
    scc_ids(3, edges), scc_dag(3, edges)  # => ([0, 0, 1], [[1], []])
    clause = [(0, True, 0, True), (0, False, 1, True)]
    two_sat(2, clause)  # => [True, True]
    two_sat(2, clause + [(1, False, 1, False)]) is None  # => True
"""


def scc_ids(N, edges):
    """独自拡張: 頂点ごとの成分番号。異なる成分への辺u→vではids[u]<ids[v]。
    Nは頂点数、edgesは0-indexedの有向辺(u,v)の列。非再帰O(N+M)。
    Nは頂点数の非負整数、M=len(edges)。edges=[(u,v),...]は有向辺列で0<=u,v<N。空間O(N+M)。
    """
    assert N >= 0
    g = [[] for _ in range(N)]
    rg = [[] for _ in range(N)]
    for u, v in edges:
        assert 0 <= u < N and 0 <= v < N
        g[u].append(v)
        rg[v].append(u)
    seen = [False] * N
    cursor = [0] * N
    order = []
    for root in range(N):
        if seen[root]:
            continue
        seen[root] = True
        stack = [root]
        while stack:
            v = stack[-1]
            if cursor[v] == len(g[v]):
                order.append(stack.pop())
                continue
            to = g[v][cursor[v]]
            cursor[v] += 1
            if not seen[to]:
                seen[to] = True
                stack.append(to)
    ids = [-1] * N
    count = 0
    for root in reversed(order):
        if ids[root] != -1:
            continue
        ids[root] = count
        stack = [root]
        while stack:
            for to in rg[stack.pop()]:
                if ids[to] == -1:
                    ids[to] = count
                    stack.append(to)
        count += 1
    return ids


def scc(N, edges):
    """scc(N,edges)で各成分の頂点listをトポロジカル順に返す。O(N+M)。
    edges=[(始点,終点),...]。各成分内の頂点は昇順、独立成分間の順序は未指定。
    Nは頂点数の非負整数、M=len(edges)。edges=[(u,v),...]は有向辺列で0<=u,v<N。空間O(N+M)。
    """
    ids = scc_ids(N, edges)
    groups = [[] for _ in range(max(ids, default=-1) + 1)]
    for v, group in enumerate(ids):
        groups[group].append(v)
    return groups


def scc_dag(N, edges):
    """独自拡張: SCCを縮約したDAGの隣接リスト。自己辺・多重辺を除く。
    成分番号はscc_idsと同じ。edgesは再走査可能な列。O(N+M)。
    Nは頂点数の非負整数、M=len(edges)。edges=[(u,v),...]は有向辺列で0<=u,v<N。空間O(N+M)。
    """
    ids = scc_ids(N, edges)
    dag = [set() for _ in range(max(ids, default=-1) + 1)]
    for u, v in edges:
        if ids[u] != ids[v]:
            dag[ids[u]].add(ids[v])
    return [list(neighbors) for neighbors in dag]


def two_sat(n, clause):
    """two_sat(n,clause)で解のboolリストを返す。充足不能ならNone。O(n+節数)。
    clause=[(i,f,j,g),...]は(x[i]==f) OR (x[j]==g)のAND。i,jは0-indexed。
    空の解[]も有効なので、結果はif answer is Noneで判定する。
    nはbool変数の個数、f/gはbool、0<=i,j<n。K=len(clause)。時間・空間O(n+K)。
    """
    edges = []
    for i, f, j, g in clause:
        assert 0 <= i < n and 0 <= j < n
        a, b = 2 * i + int(bool(f)), 2 * j + int(bool(g))
        edges.extend([(a ^ 1, b), (b ^ 1, a)])
    ids = scc_ids(2 * n, edges)
    if any(ids[2 * i] == ids[2 * i + 1] for i in range(n)):
        return None
    return [ids[2 * i] < ids[2 * i + 1] for i in range(n)]
