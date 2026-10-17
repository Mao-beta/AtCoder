# verification-helper: PROBLEM https://judge.yosupo.jp/problem/matrix_det
import sys
from cp_snippet_palette.library.math.linear_algebra import matrix_det


def main():
    read = sys.stdin.buffer.readline
    a = [list(map(int, read().split())) for _ in range(int(read()))]
    print(matrix_det(a))


if __name__ == "__main__":
    main()
