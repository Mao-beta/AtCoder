# verification-helper: PROBLEM https://judge.yosupo.jp/problem/system_of_linear_equations
import sys
from cp_snippet_palette.library.math.linear_algebra import linear_equations


def main():
    read = sys.stdin.buffer.readline
    n, m = map(int, read().split())
    a = [list(map(int, read().split())) for _ in range(n)]
    b = list(map(int, read().split()))
    answer = linear_equations(a, b, variables=m)
    if answer is None:
        print(-1)
    else:
        solution, basis = answer
        print(len(basis))
        print(*solution)
        for row in basis:
            print(*row)


if __name__ == "__main__":
    main()
