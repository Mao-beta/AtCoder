# verification-helper: PROBLEM https://judge.yosupo.jp/problem/inverse_matrix
import sys
from cp_snippet_palette.library.math.linear_algebra import inverse_matrix


def main():
    read = sys.stdin.buffer.readline
    a = [list(map(int, read().split())) for _ in range(int(read()))]
    answer = inverse_matrix(a)
    if answer is None:
        print(-1)
    else:
        for row in answer:
            print(*row)


if __name__ == "__main__":
    main()
