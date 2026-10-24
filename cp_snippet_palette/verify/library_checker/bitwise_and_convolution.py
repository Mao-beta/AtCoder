# verification-helper: PROBLEM https://judge.yosupo.jp/problem/bitwise_and_convolution
import sys
from cp_snippet_palette.library.math.bit_transforms import and_convolution


def main():
    read = sys.stdin.buffer.readline
    n = int(read())
    a = list(map(int, read().split()))
    b = list(map(int, read().split()))
    print(*and_convolution(a, b))


if __name__ == "__main__":
    main()
