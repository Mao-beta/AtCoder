# verification-helper: PROBLEM https://judge.yosupo.jp/problem/convolution_mod
import sys
from cp_snippet_palette.library.math.polynomial import FFT


def main():
    read = sys.stdin.buffer.readline
    n, m = map(int, read().split())
    a = list(map(int, read().split()))
    b = list(map(int, read().split()))
    print(*FFT(998244353).convolution(a, b))


if __name__ == "__main__":
    main()
