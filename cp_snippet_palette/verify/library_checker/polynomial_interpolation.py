# verification-helper: PROBLEM https://judge.yosupo.jp/problem/polynomial_interpolation
import sys
from cp_snippet_palette.library.math.polynomial import polynomial_interpolation


def main():
    read = sys.stdin.buffer.readline
    n = int(read())
    x = list(map(int, read().split()))
    y = list(map(int, read().split()))
    print(*polynomial_interpolation(x, y).resize(n).Func)


if __name__ == "__main__":
    main()
