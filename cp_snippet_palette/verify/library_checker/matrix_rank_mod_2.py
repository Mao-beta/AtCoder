# verification-helper: PROBLEM https://judge.yosupo.jp/problem/matrix_rank_mod_2
import sys
from cp_snippet_palette.library.math.gf2_matrix import matrix_rank_gf2


def main():
    read = sys.stdin.buffer.readline
    n, m = map(int, read().split())
    print(matrix_rank_gf2([int(read().strip()[::-1] or b"0", 2) for _ in range(n)], m))


if __name__ == "__main__":
    main()
