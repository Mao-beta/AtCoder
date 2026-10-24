# verification-helper: PROBLEM https://judge.yosupo.jp/problem/pow_of_formal_power_series
import sys
from cp_snippet_palette.library.math.polynomial import fps_power


def main():
    read = sys.stdin.buffer.readline
    n, k = map(int, read().split())
    print(*fps_power(list(map(int, read().split())), k, n))


if __name__ == "__main__":
    main()
