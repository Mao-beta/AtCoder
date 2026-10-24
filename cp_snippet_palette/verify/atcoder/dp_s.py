# https://atcoder.jp/contests/dp/tasks/dp_s
from cp_snippet_palette.library.basic.digit_dp import count_digit_sum_mod
import sys


def main():
    input = sys.stdin.readline
    k = input().strip()
    d = int(input())
    print(count_digit_sum_mod(k, d))


if __name__ == "__main__":
    main()
