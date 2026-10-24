# https://atcoder.jp/contests/abc214/tasks/abc214_e
from cp_snippet_palette.library.basic.intervals import assign_distinct_in_intervals
import sys


def main():
    input = sys.stdin.readline
    t = int(input())
    for _ in range(t):
        n = int(input())
        ranges = [tuple(map(int, input().split())) for _ in range(n)]
        print("Yes" if assign_distinct_in_intervals(ranges) is not None else "No")


if __name__ == "__main__":
    main()
