# verification-helper: PROBLEM https://judge.yosupo.jp/problem/inverse_matrix_mod_2
import sys
from cp_snippet_palette.library.math.gf2_matrix import inverse_matrix_gf2


def main():
    read = sys.stdin.buffer.readline
    n = int(read())
    answer = inverse_matrix_gf2([int(read().strip()[::-1], 2) for _ in range(n)])
    if answer is None:
        print(-1)
    else:
        for row in answer:
            print(format(row, f"0{n}b")[::-1])


if __name__ == "__main__":
    main()
