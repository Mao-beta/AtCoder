# https://atcoder.jp/contests/abc396/tasks/abc396_e
from cp_snippet_palette.library.structures.xor_dsu import XorDSU
import sys


def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    uf = XorDSU(n)
    valid = True
    for _ in range(m):
        x, y, z = map(int, input().split())
        try:
            uf.merge(x - 1, y - 1, z)
        except ValueError:
            valid = False
    if valid:
        print(*uf.minimum_sum_values())
    else:
        print(-1)


if __name__ == "__main__":
    main()
