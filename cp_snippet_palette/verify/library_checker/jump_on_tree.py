# verification-helper: PROBLEM https://judge.yosupo.jp/problem/jump_on_tree
import sys
from cp_snippet_palette.library.graphs.hld import HLD


def main():
    read = sys.stdin.buffer.readline
    n, q = map(int, read().split())

    graph = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = map(int, read().split())
        graph[u].append(v)
        graph[v].append(u)
    hld = HLD(n, graph)

    print("\n".join(str(hld.jump(*map(int, read().split()))) for _ in range(q)))


if __name__ == "__main__":
    main()
