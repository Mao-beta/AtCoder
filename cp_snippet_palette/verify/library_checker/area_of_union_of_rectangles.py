# verification-helper: PROBLEM https://judge.yosupo.jp/problem/area_of_union_of_rectangles
import sys
from cp_snippet_palette.library.geometry.rectangle_union import rectangle_union_area


def main():
    read = sys.stdin.buffer.readline
    n = int(read())
    print(rectangle_union_area([tuple(map(int, read().split())) for _ in range(n)]))


if __name__ == "__main__":
    main()
