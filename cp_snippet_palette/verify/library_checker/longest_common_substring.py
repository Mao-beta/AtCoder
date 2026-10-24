# verification-helper: PROBLEM https://judge.yosupo.jp/problem/longest_common_substring
import sys
from cp_snippet_palette.library.strings.suffix_array import longest_common_substring


def main():
    read = sys.stdin.buffer.readline
    s, t = read().strip().decode(), read().strip().decode()
    print(*longest_common_substring(s, t))


if __name__ == "__main__":
    main()
