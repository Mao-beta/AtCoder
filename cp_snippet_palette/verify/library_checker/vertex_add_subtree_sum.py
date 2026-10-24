# verification-helper: PROBLEM https://judge.yosupo.jp/problem/vertex_add_subtree_sum
import sys
from cp_snippet_palette.library.graphs.hld import HLD
from cp_snippet_palette.snippets.structures.BIT import fenwick_tree


def main():
    read = sys.stdin.buffer.readline
    n, q = map(int, read().split())
    values = list(map(int, read().split()))

    graph = [[] for _ in range(n)]
    for u, p in enumerate(map(int, read().split()), 1):
        graph[u].append(p)
        graph[p].append(u)
    hld = HLD(n, graph)

    bit = fenwick_tree.from_list(hld.reorder_by_pos_from_node_values(values))
    answer = []
    for _ in range(q):
        row = list(map(int, read().split()))
        if row[0] == 0:
            bit.add(hld.pos[row[1]], row[2])
        else:
            answer.append(str(bit.sum(*hld.subtree_range(row[1]))))
    print("\n".join(answer))


if __name__ == "__main__":
    main()
