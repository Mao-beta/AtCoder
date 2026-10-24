# verification-helper: PROBLEM https://atcoder.jp/contests/abc343/tasks/abc343_f
import sys
from cp_snippet_palette.library.structures.segtree_monoids import range_top2


def main():
    read = sys.stdin.buffer.readline
    n, q = map(int, read().split())
    seg = range_top2(list(map(int, read().split())))
    answer = []
    for _ in range(q):
        t, l, r = map(int, read().split())
        if t == 1:
            seg.set(l - 1, r)
        else:
            answer.append(str(seg.prod(l - 1, r)[3]))
    print("\n".join(answer))


if __name__ == "__main__":
    main()
