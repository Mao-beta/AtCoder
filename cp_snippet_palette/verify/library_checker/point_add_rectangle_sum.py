# verification-helper: PROBLEM https://judge.yosupo.jp/problem/point_add_rectangle_sum
import sys
from cp_snippet_palette.library.structures.fenwick_2d import OfflineFenwick2D


def main():
    read = sys.stdin.buffer.readline
    n, q = map(int, read().split())
    points = [tuple(map(int, read().split())) for _ in range(n)]
    queries = [tuple(map(int, read().split())) for _ in range(q)]
    coords = [(x, y) for x, y, w in points] + [
        (row[1], row[2]) for row in queries if row[0] == 0
    ]
    bit = OfflineFenwick2D(coords)
    for x, y, w in points:
        bit.add(x, y, w)
    answer = []
    for row in queries:
        if row[0] == 0:
            bit.add(*row[1:])
        else:
            answer.append(str(bit.sum(*row[1:])))
    print("\n".join(answer))


if __name__ == "__main__":
    main()
