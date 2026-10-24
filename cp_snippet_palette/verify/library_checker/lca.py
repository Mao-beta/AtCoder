# verification-helper: PROBLEM https://judge.yosupo.jp/problem/lca
import sys
from cp_snippet_palette.snippets.structures.LCATree import LCATree


def main():
    read = sys.stdin.buffer.readline
    n, q = map(int, read().split())

    edges = [(u, p) for u, p in enumerate(map(int, read().split()), 1)]
    tree = LCATree(n, edges)

    print("\n".join(str(tree.lca(*map(int, read().split()))) for _ in range(q)))


if __name__ == "__main__":
    main()
