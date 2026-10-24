# https://atcoder.jp/contests/abc247/tasks/abc247_e
from cp_snippet_palette.library.basic.subarray_count import count_subarrays_minmax
import sys


def main():
    input = sys.stdin.readline
    n, x, y = map(int, input().split())
    a = list(map(int, input().split()))
    print(count_subarrays_minmax(a, y, x))


if __name__ == "__main__":
    main()
