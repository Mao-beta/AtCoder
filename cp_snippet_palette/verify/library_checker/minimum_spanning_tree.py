# verification-helper: PROBLEM https://judge.yosupo.jp/problem/minimum_spanning_tree
import sys
from cp_snippet_palette.library.graphs.mst import minimum_spanning_forest


def main():
    read = sys.stdin.buffer.readline
    n, m = map(int, read().split())
    weight, ids, components = minimum_spanning_forest(
        n, [tuple(map(int, read().split())) for _ in range(m)]
    )
    print(weight)
    print(*ids)


if __name__ == "__main__":
    main()
