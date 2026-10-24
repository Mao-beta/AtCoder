# verification-helper: PROBLEM https://judge.yosupo.jp/problem/division_of_polynomials
import sys
from cp_snippet_palette.library.math.polynomial import polynomial_divmod


def main():
    read = sys.stdin.buffer.readline
    n, m = map(int, read().split())
    a = list(map(int, read().split()))
    b = list(map(int, read().split()))
    q, r = polynomial_divmod(a, b)
    print(len(q), len(r))
    print(*q)
    print(*r)


if __name__ == "__main__":
    main()
