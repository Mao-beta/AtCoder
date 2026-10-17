# verification-helper: PROBLEM https://judge.yosupo.jp/problem/matrix_rank
import sys
from cp_snippet_palette.library.math.linear_algebra import matrix_rank


def main():
    read = sys.stdin.buffer.readline
    n, m = map(int, read().split())
    a = [list(map(int, read().split())) for _ in range(n)]
    print(matrix_rank(a))


if __name__ == "__main__":
    main()
