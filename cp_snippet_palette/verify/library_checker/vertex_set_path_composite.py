# verification-helper: PROBLEM https://judge.yosupo.jp/problem/vertex_set_path_composite
import sys
from cp_snippet_palette.library.graphs.hld import HLD, BiSegTree, path_prod


def main():
    read = sys.stdin.buffer.readline
    mod = 998244353

    def op(f, g):
        return g[0] * f[0] % mod, (g[0] * f[1] + g[1]) % mod

    n, q = map(int, read().split())
    values = [tuple(map(int, read().split())) for _ in range(n)]

    graph = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = map(int, read().split())
        graph[u].append(v)
        graph[v].append(u)
    hld = HLD(n, graph)

    seg = BiSegTree(hld.reorder_by_pos_from_node_values(values), op, (1, 0))
    answer = []
    for _ in range(q):
        t, u, v, x = map(int, read().split())
        if t == 0:
            seg.set(hld.pos[u], (v, x))
        else:
            a, b = path_prod(hld, seg, u, v)
            answer.append(str((a * x + b) % mod))
    print("\n".join(answer))


if __name__ == "__main__":
    main()
