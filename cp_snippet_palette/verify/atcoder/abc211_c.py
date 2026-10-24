# https://atcoder.jp/contests/abc211/tasks/abc211_c
from cp_snippet_palette.library.strings.subsequence import count_subsequence
import sys


def main():
    input = sys.stdin.readline
    s = input().strip()
    print(count_subsequence(s, "chokudai"))


if __name__ == "__main__":
    main()
