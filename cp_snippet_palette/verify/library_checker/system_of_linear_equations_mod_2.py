# verification-helper: PROBLEM https://judge.yosupo.jp/problem/system_of_linear_equations_mod_2
import sys
from cp_snippet_palette.library.math.bit_transforms import linear_equations_gf2


def main():
    read = sys.stdin.buffer.readline
    n, m = map(int, read().split())
    rows = [int(read().strip()[::-1], 2) for _ in range(n)]
    rhs = [int(x) for x in read().strip().decode()]
    answer = linear_equations_gf2(rows, rhs, m)
    if answer is None:
        print(-1)
    else:
        solution, basis = answer
        print(len(basis))
        for value in [solution, *basis]:
            print(format(value, f"0{m}b")[::-1])


if __name__ == "__main__":
    main()
