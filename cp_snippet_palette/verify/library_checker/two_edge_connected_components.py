# verification-helper: PROBLEM https://judge.yosupo.jp/problem/two_edge_connected_components
import sys
from cp_snippet_palette.library.graphs.lowlink import LowLink


def main():
    read = sys.stdin.buffer.readline
    n, m = map(int, read().split())
    groups = LowLink(
        n, [tuple(map(int, read().split())) for _ in range(m)]
    ).two_edge_connected_components()
    print(len(groups))
    for group in groups:
        print(len(group), *group)


if __name__ == "__main__":
    main()
