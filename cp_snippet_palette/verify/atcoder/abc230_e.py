# https://atcoder.jp/contests/abc230/tasks/abc230_e
from cp_snippet_palette.library.math.integer_count import sum_floor_quotients
import sys


def main():
    input = sys.stdin.readline
    print(sum_floor_quotients(int(input())))


if __name__ == "__main__":
    main()
