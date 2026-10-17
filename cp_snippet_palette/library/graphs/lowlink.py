"""無向グラフのLowLink。出典: _Low_Link.pyを多重辺・非連結対応に修正。
O(V+E)、非再帰、0-indexed。bridgesは入力辺ID、articulationは関節点集合。
biconnected_components()で頂点二重連結成分、block_cut_tree()で所属関係の森。
PyPy向け。Codonでは入力edgesを整数ペアのlistにする。
"""


class LowLink:
    def __init__(self, n, edges):
        edges = list(edges)
        graph = [[] for _ in range(n)]
        for eid, (u, v) in enumerate(edges):
            graph[u].append((v, eid))
            graph[v].append((u, eid))
        self.order = order = [-1] * n
        self.low = low = [0] * n
        self.bridges = []
        self.articulation = set()
        self._components = []
        edge_stack = []
        marked = [-1] * n
        parent = [-1] * n
        parent_edge = [-1] * n
        child_count = [0] * n
        cursor = [0] * n
        timer = 0
        for root in range(n):
            if order[root] != -1:
                continue
            order[root] = low[root] = timer
            timer += 1
            stack = [root]
            while stack:
                u = stack[-1]
                if cursor[u] == len(graph[u]):
                    stack.pop()
                    p = parent[u]
                    if p == -1:
                        if child_count[u] >= 2:
                            self.articulation.add(u)
                        if child_count[u] == 0:
                            self._components.append([u])
                    else:
                        low[p] = min(low[p], low[u])
                        if low[u] > order[p]:
                            self.bridges.append(parent_edge[u])
                        if parent[p] != -1 and low[u] >= order[p]:
                            self.articulation.add(p)
                        if low[u] >= order[p]:
                            component = []
                            cid = len(self._components)
                            while True:
                                eid = edge_stack.pop()
                                for vertex in edges[eid]:
                                    if marked[vertex] != cid:
                                        marked[vertex] = cid
                                        component.append(vertex)
                                if eid == parent_edge[u]:
                                    break
                            self._components.append(component)
                    continue
                v, eid = graph[u][cursor[u]]
                cursor[u] += 1
                if eid == parent_edge[u]:
                    continue
                if order[v] == -1:
                    edge_stack.append(eid)
                    parent[v], parent_edge[v] = u, eid
                    child_count[u] += 1
                    order[v] = low[v] = timer
                    timer += 1
                    stack.append(v)
                else:
                    low[u] = min(low[u], order[v])
                    if order[v] < order[u]:
                        edge_stack.append(eid)

    def biconnected_components(self):
        """頂点集合のリスト。関節点は複数成分に属し、孤立点も1成分。
        自己ループは頂点の連結性に影響しないものとして無視する。多重辺可。
        成分と内部の頂点の順序は保証しない。O(V+E)、返すリストはコピー。
        """
        return [component[:] for component in self._components]

    def block_cut_tree(self):
        """元頂点0..n-1と成分頂点n..n+k-1の所属関係を表す森の隣接リスト。
        連結グラフなら木。成分番号はbiconnected_components()と一致。O(V+E)。
        """
        n = len(self.order)
        graph = [[] for _ in range(n + len(self._components))]
        for i, component in enumerate(self._components):
            for vertex in component:
                graph[vertex].append(n + i)
                graph[n + i].append(vertex)
        return graph
