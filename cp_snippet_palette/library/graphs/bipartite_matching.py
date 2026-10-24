"""二部最大マッチング。Hopcroft–Karp法。

非再帰の層別増加路探索。O((V+E)√V)。左側graph[u]に右側頂点IDを並べる。

戻り値は(left_match,right_match)。未対応は-1。PyPy向け。

使い方（このファイルを解答の先頭に貼り付けてから実行）
    left, right = bipartite_matching([[0], [0, 1]], 2)
    left, right, sum(v != -1 for v in left)  # => ([0, 1], [0, 1], 2)
"""

from collections import deque


def bipartite_matching(graph, right_size):
    """graph[u]に左頂点uと接続する右頂点IDを並べる。左右はそれぞれ0-indexed。
    right_sizeは右頂点数。戻り値(left_match,right_match)は相手側のID、未対応は-1。
    マッチング数はsum(v!=-1 for v in left_match)。入力非破壊。非再帰Hopcroft–Karp法、O((V+E)√V)。
    graphは左頂点数L個のlist of lists、right_sizeは右頂点数Rの非負整数。V=L+R、E=sum(map(len,graph))。空間O(V+E)以内。
    """
    n = len(graph)
    if any(not 0 <= v < right_size for row in graph for v in row):
        raise IndexError("invalid right vertex")
    left_match, right_match = [-1] * n, [-1] * right_size
    while True:
        distance = [-1] * n
        queue = deque()
        for u in range(n):
            if left_match[u] == -1:
                distance[u] = 0
                queue.append(u)
        shortest = n + 1
        while queue:
            u = queue.popleft()
            if distance[u] + 1 > shortest:
                continue
            for v in graph[u]:
                mate = right_match[v]
                if mate == -1:
                    shortest = distance[u] + 1
                elif distance[mate] == -1 and distance[u] + 1 < shortest:
                    distance[mate] = distance[u] + 1
                    queue.append(mate)
        if shortest == n + 1:
            break
        cursor = [0] * n
        for start in range(n):
            if left_match[start] != -1 or distance[start] < 0:
                continue
            stack = [start]
            while stack:
                u = stack[-1]
                found = False
                while cursor[u] < len(graph[u]):
                    v = graph[u][cursor[u]]
                    cursor[u] += 1
                    mate = right_match[v]
                    if mate == -1 and distance[u] + 1 == shortest:
                        for vertex in reversed(stack):
                            old = left_match[vertex]
                            left_match[vertex], right_match[v] = v, vertex
                            distance[vertex] = -1
                            v = old
                        stack.clear()
                        found = True
                        break
                    if mate != -1 and distance[mate] == distance[u] + 1:
                        stack.append(mate)
                        found = True
                        break
                if not found:
                    distance[u] = -1
                    stack.pop()
    return left_match, right_match
