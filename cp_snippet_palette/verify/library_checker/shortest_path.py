# verification-helper: PROBLEM https://judge.yosupo.jp/problem/shortest_path
import sys
from cp_snippet_palette.library.graphs.shortest_paths import (
    weighted_adjlist,
    dijkstra,
    restore_path,
)


def main():
    read = sys.stdin.buffer.readline
    n, m, s, t = map(int, read().split())
    graph = weighted_adjlist(
        n, [tuple(map(int, read().split())) for _ in range(m)], directed=True
    )
    distance, parent = dijkstra(graph, s)
    path = restore_path(parent, s, t)
    if not path:
        print(-1)
    else:
        print(distance[t], len(path) - 1)
        for u, v in zip(path, path[1:]):
            print(u, v)


if __name__ == "__main__":
    main()
