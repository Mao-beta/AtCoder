# verification-helper: PROBLEM https://judge.yosupo.jp/problem/vertex_add_path_sum
import sys
from cp_snippet_palette.library.graphs.hld import HLD, BiSegTree, path_prod


def main():
    read = sys.stdin.buffer.readline
    n, q = map(int, read().split())
    values = list(map(int, read().split()))

    graph = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = map(int, read().split())
        graph[u].append(v)
        graph[v].append(u)
    hld = HLD(n, graph)

    seg = BiSegTree(hld.reorder_by_pos_from_node_values(values), lambda a, b: a + b, 0)
    answer = []
    for _ in range(q):
        t, u, v = map(int, read().split())
        if t == 0:
            seg.set(hld.pos[u], seg.get(hld.pos[u]) + v)
        else:
            answer.append(str(path_prod(hld, seg, u, v)))
    print("\n".join(answer))


if __name__ == "__main__":
    main()
