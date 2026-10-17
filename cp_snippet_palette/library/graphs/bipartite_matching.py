"""二部最大マッチング。出典: tessoku-book/A69.py。
非再帰の増加路探索。O(L*E)。左側graph[u]に右側頂点IDを並べる。
戻り値は(left_match,right_match)。未対応は-1。PyPy向け。
"""

from collections import deque


def bipartite_matching(graph, right_size):
    left_match = [-1] * len(graph)
    right_match = [-1] * right_size
    for start in range(len(graph)):
        seen = [False] * len(graph)
        parent_right = [-1] * right_size
        seen[start] = True
        q = deque([start])
        free = -1
        while q and free == -1:
            u = q.popleft()
            for v in graph[u]:
                if not 0 <= v < right_size:
                    raise IndexError("invalid right vertex")
                if parent_right[v] != -1:
                    continue
                parent_right[v] = u
                mate = right_match[v]
                if mate == -1:
                    free = v
                    break
                if not seen[mate]:
                    seen[mate] = True
                    q.append(mate)
        while free != -1:
            u = parent_right[free]
            previous = left_match[u]
            left_match[u], right_match[free] = free, u
            free = previous
    return left_match, right_match
