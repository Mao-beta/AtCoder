# verification-helper: PROBLEM https://judge.yosupo.jp/problem/point_set_range_composite
import sys
from cp_snippet_palette.library.structures.segtree_monoids import range_affine_composite


def main():
    read = sys.stdin.buffer.readline
    mod = 998244353

    n, q = map(int, read().split())
    seg = range_affine_composite(
        [tuple(map(int, read().split())) for _ in range(n)], mod
    )
    answer = []
    for _ in range(q):
        t, l, r, x = map(int, read().split())
        if t == 0:
            seg.set(l, (r, x))
        else:
            a, b = seg.prod(l, r)
            answer.append(str((a * x + b) % mod))
    print("\n".join(answer))


if __name__ == "__main__":
    main()
