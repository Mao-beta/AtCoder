# verification-helper: PROBLEM https://atcoder.jp/contests/abl/tasks/abl_e
import sys
from cp_snippet_palette.library.structures.lazy_segtree_actions import (
    range_digit_assign,
)


def main():
    read = sys.stdin.buffer.readline
    n, q = map(int, read().split())
    seg = range_digit_assign([1] * n)
    answer = []
    for _ in range(q):
        l, r, digit = map(int, read().split())
        seg.apply(l - 1, r, digit)
        answer.append(str(seg.all_prod()))
    print("\n".join(answer))


if __name__ == "__main__":
    main()
