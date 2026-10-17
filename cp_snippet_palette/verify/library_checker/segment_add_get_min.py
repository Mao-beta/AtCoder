# verification-helper: PROBLEM https://judge.yosupo.jp/problem/segment_add_get_min
import sys
from cp_snippet_palette.library.structures.li_chao import LiChaoTree


def main():
    read = sys.stdin.buffer.readline
    n, q = map(int, read().split())
    segments = [tuple(map(int, read().split())) for _ in range(n)]
    queries = [tuple(map(int, read().split())) for _ in range(q)]
    tree = LiChaoTree([query[1] for query in queries if query[0] == 1])
    for left, right, a, b in segments:
        tree.add_segment(left, right, a, b)
    output = []
    for query in queries:
        if query[0] == 0:
            tree.add_segment(*query[1:])
        else:
            value = tree.query(query[1])
            output.append("INFINITY" if value is None else str(value))
    sys.stdout.write("\n".join(output) + ("\n" if output else ""))


if __name__ == "__main__":
    main()
