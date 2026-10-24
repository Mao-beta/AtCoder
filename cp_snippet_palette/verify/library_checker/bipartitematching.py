# verification-helper: PROBLEM https://judge.yosupo.jp/problem/bipartitematching
import sys
from cp_snippet_palette.library.graphs.bipartite_matching import bipartite_matching


def main():
    read = sys.stdin.buffer.readline
    l, r, m = map(int, read().split())
    graph = [[] for _ in range(l)]
    for _ in range(m):
        u, v = map(int, read().split())
        graph[u].append(v)
    left, right = bipartite_matching(graph, r)
    print(sum(v != -1 for v in left))
    for u, v in enumerate(left):
        if v != -1:
            print(u, v)


if __name__ == "__main__":
    main()
