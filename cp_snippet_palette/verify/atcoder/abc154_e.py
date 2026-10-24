# https://atcoder.jp/contests/abc154/tasks/abc154_e
from cp_snippet_palette.library.basic.digit_dp import count_nonzero_digits
import sys


def main():
    input = sys.stdin.readline
    n = input().strip()
    k = int(input())
    print(count_nonzero_digits(n, k))


if __name__ == "__main__":
    main()
