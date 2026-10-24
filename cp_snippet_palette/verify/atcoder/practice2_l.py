# verification-helper: PROBLEM https://atcoder.jp/contests/practice2/tasks/practice2_l
import sys
from cp_snippet_palette.library.structures.lazy_segtree_actions import (
    range_flip_inversions,
)


def main():
    read = sys.stdin.buffer.readline
    n, q = map(int, read().split())
    seg = range_flip_inversions(list(map(int, read().split())))
    answer = []
    for _ in range(q):
        t, l, r = map(int, read().split())
        if t == 1:
            seg.apply(l - 1, r, True)
        else:
            answer.append(str(seg.inversions(l - 1, r)))
    print("\n".join(answer))


if __name__ == "__main__":
    main()
