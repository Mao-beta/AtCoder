# verification-helper: PROBLEM https://judge.yosupo.jp/problem/bitwise_xor_convolution
import sys
from cp_snippet_palette.library.math.bit_transforms import xor_convolution


def main():
    read = sys.stdin.buffer.readline
    read()  # 指数N。配列長は2**N。
    a = list(map(int, read().split()))
    b = list(map(int, read().split()))
    print(*xor_convolution(a, b))


if __name__ == "__main__":
    main()
