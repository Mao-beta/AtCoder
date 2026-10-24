# verification-helper: PROBLEM https://judge.yosupo.jp/problem/staticrmq
import sys
from cp_snippet_palette.library.structures.segtree_monoids import range_min


def main():
    read = sys.stdin.buffer.readline
    n, q = map(int, read().split())
    seg = range_min(list(map(int, read().split())))
    print("\n".join(str(seg.prod(*map(int, read().split()))) for _ in range(q)))


if __name__ == "__main__":
    main()
