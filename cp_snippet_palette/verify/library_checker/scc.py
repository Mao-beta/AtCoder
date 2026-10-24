# verification-helper: PROBLEM https://judge.yosupo.jp/problem/scc
import sys
from cp_snippet_palette.library.graphs.scc import scc


def main():
    read = sys.stdin.buffer.readline
    n, m = map(int, read().split())
    edges = [tuple(map(int, read().split())) for _ in range(m)]
    groups = scc(n, edges)
    print(len(groups))
    for group in groups:
        print(len(group), *group)


if __name__ == "__main__":
    main()
