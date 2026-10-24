# verification-helper: PROBLEM https://judge.yosupo.jp/problem/kth_term_of_linearly_recurrent_sequence
import sys
from cp_snippet_palette.library.math.polynomial import linear_recurrence_ntt


def main():
    read = sys.stdin.buffer.readline
    d, k = map(int, read().split())
    a = list(map(int, read().split()))
    c = list(map(int, read().split()))
    print(linear_recurrence_ntt(a, c, k))


if __name__ == "__main__":
    main()
