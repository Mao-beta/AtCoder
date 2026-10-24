# verification-helper: PROBLEM https://judge.yosupo.jp/problem/tree_diameter
import sys
from cp_snippet_palette.library.graphs.tree import weighted_tree_diameter


def main():
    read = sys.stdin.buffer.readline
    n = int(read())
    graph = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v, w = map(int, read().split())
        graph[u].append((v, w))
        graph[v].append((u, w))
    length, path = weighted_tree_diameter(graph)
    print(length, len(path))
    print(*path)


if __name__ == "__main__":
    main()
