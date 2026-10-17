# verification-helper: PROBLEM https://judge.yosupo.jp/problem/biconnected_components
import sys
from cp_snippet_palette.library.graphs.lowlink import LowLink


def main():
    read = sys.stdin.buffer.readline
    n, m = map(int, read().split())
    edges = [tuple(map(int, read().split())) for _ in range(m)]
    components = LowLink(n, edges).biconnected_components()
    print(len(components))
    for component in components:
        print(len(component), *component)


if __name__ == "__main__":
    main()
