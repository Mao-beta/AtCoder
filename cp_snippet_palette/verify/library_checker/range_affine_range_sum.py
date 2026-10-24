# verification-helper: PROBLEM https://judge.yosupo.jp/problem/range_affine_range_sum
import sys
from cp_snippet_palette.library.structures.lazy_segtree_actions import range_affine_sum


def main():
    read = sys.stdin.buffer.readline
    n, q = map(int, read().split())
    a = list(map(int, read().split()))
    seg = range_affine_sum(a)
    answer = []
    for _ in range(q):
        query = list(map(int, read().split()))
        if query[0] == 0:
            _, l, r, b, c = query
            seg.apply(l, r, (b, c))
        else:
            answer.append(str(seg.prod(query[1], query[2])))
    print("\n".join(answer))


if __name__ == "__main__":
    main()
