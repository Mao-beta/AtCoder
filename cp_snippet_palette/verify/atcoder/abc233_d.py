# https://atcoder.jp/contests/abc233/tasks/abc233_d
from cp_snippet_palette.library.basic.subarray_count import count_subarrays_sum
import sys


def main():
    input = sys.stdin.readline
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(count_subarrays_sum(a, k))


if __name__ == "__main__":
    main()
