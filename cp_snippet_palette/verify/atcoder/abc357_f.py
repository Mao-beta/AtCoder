# verification-helper: PROBLEM https://atcoder.jp/contests/abc357/tasks/abc357_f
import sys
from cp_snippet_palette.library.structures.lazy_segtree_actions import (
    range_pair_add_product,
)


def main():
    read = sys.stdin.buffer.readline
    n, q = map(int, read().split())
    a = list(map(int, read().split()))
    b = list(map(int, read().split()))
    seg = range_pair_add_product(list(zip(a, b)))
    answer = []
    for _ in range(q):
        query = list(map(int, read().split()))
        t, l, r = query[:3]
        if t == 3:
            answer.append(str(seg.prod(l - 1, r)[2]))
        elif t == 1:
            seg.apply(l - 1, r, (query[3], 0))
        else:
            seg.apply(l - 1, r, (0, query[3]))
    print("\n".join(answer))


if __name__ == "__main__":
    main()
