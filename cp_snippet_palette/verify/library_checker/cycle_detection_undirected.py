# verification-helper: PROBLEM https://judge.yosupo.jp/problem/cycle_detection_undirected
import sys
from cp_snippet_palette.library.graphs.cycle import find_cycle


def main():
    read = sys.stdin.buffer.readline
    n, m = map(int, read().split())
    edges = [tuple(map(int, read().split())) for _ in range(m)]
    result = find_cycle(n, edges, directed=False)
    if result is None:
        print(-1)
    else:
        vertices, ids = result
        print(len(ids))
        print(*vertices)
        print(*ids)


if __name__ == "__main__":
    main()
