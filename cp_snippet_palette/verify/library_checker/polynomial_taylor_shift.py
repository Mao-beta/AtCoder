# verification-helper: PROBLEM https://judge.yosupo.jp/problem/polynomial_taylor_shift
import sys
from cp_snippet_palette.library.math.polynomial import FPS


def main():
    read = sys.stdin.buffer.readline
    n, c = map(int, read().split())
    f = FPS(list(map(int, read().split())))
    print(*f.taylor_shift(c).resize(n).Func)


if __name__ == "__main__":
    main()
