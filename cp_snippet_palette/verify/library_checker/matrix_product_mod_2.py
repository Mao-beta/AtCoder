# verification-helper: PROBLEM https://judge.yosupo.jp/problem/matrix_product_mod_2
import sys
from cp_snippet_palette.library.math.gf2_matrix import matrix_product_gf2


def main():
    read = sys.stdin.buffer.readline
    n, m, k = map(int, read().split())
    a = [int(read().strip()[::-1], 2) for _ in range(n)]
    b = [int(read().strip()[::-1], 2) for _ in range(m)]
    for row in matrix_product_gf2(a, b, k):
        print(format(row, f"0{k}b")[::-1])


if __name__ == "__main__":
    main()
