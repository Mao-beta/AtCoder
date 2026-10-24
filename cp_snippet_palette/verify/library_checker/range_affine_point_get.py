# verification-helper: PROBLEM https://judge.yosupo.jp/problem/range_affine_point_get
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
            answer.append(str(seg.get(query[1])))
    print("\n".join(answer))


if __name__ == "__main__":
    main()
