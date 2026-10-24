# https://atcoder.jp/contests/abc386/tasks/abc386_f
from cp_snippet_palette.library.strings.subsequence import edit_distance_bounded
import sys


def main():
    input = sys.stdin.readline
    k = int(input())
    s = input().strip()
    t = input().strip()
    print("Yes" if edit_distance_bounded(s, t, k) <= k else "No")


if __name__ == "__main__":
    main()
