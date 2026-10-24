# verification-helper: PROBLEM https://judge.yosupo.jp/problem/exp_of_formal_power_series
import sys
from cp_snippet_palette.library.math.polynomial import fps_exp


def main():
    read = sys.stdin.buffer.readline
    n = int(read())
    a = list(map(int, read().split()))
    answer = fps_exp(a, n)
    if answer is None:
        print(-1)
    else:
        print(*answer)


if __name__ == "__main__":
    main()
