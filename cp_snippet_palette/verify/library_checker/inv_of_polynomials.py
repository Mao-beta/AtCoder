# verification-helper: PROBLEM https://judge.yosupo.jp/problem/inv_of_polynomials
import sys
from cp_snippet_palette.library.math.polynomial import polynomial_inverse


def main():
    read = sys.stdin.buffer.readline
    n, m = map(int, read().split())
    a = list(map(int, read().split()))
    b = list(map(int, read().split()))
    answer = polynomial_inverse(a, b)
    if answer is None:
        print(-1)
    else:
        print(len(answer))
        print(*answer)


if __name__ == "__main__":
    main()
