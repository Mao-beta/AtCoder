# verification-helper: PROBLEM https://judge.yosupo.jp/problem/line_add_get_min
import sys
from cp_snippet_palette.library.structures.li_chao import LiChaoTree


def main():
    read = sys.stdin.buffer.readline
    n, q = map(int, read().split())
    lines = [tuple(map(int, read().split())) for _ in range(n)]
    queries = [tuple(map(int, read().split())) for _ in range(q)]
    tree = LiChaoTree([row[1] for row in queries if row[0] == 1])
    for a, b in lines:
        tree.add_line(a, b)
    answer = []
    for row in queries:
        if row[0] == 0:
            tree.add_line(row[1], row[2])
        else:
            answer.append(str(tree.query(row[1])))
    print("\n".join(answer))


if __name__ == "__main__":
    main()
