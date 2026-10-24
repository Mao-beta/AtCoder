# verification-helper: PROBLEM https://judge.yosupo.jp/problem/find_linear_recurrence
import sys
from cp_snippet_palette.library.math.linear_recurrence import berlekamp_massey


def main():
    read = sys.stdin.buffer.readline
    n = int(read())
    c = berlekamp_massey(list(map(int, read().split())))
    print(len(c))
    print(*c)


if __name__ == "__main__":
    main()
