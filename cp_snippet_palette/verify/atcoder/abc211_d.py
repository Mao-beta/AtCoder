# https://atcoder.jp/contests/abc211/tasks/abc211_d
from cp_snippet_palette.library.graphs.graph_recipes import bfs_path_count
import sys


def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    g = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        g[a - 1].append(b - 1)
        g[b - 1].append(a - 1)
    print(bfs_path_count(g, 0)[1][-1])


if __name__ == "__main__":
    main()
