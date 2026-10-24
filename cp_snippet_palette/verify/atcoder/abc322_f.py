# verification-helper: PROBLEM https://atcoder.jp/contests/abc322/tasks/abc322_f
import sys
from cp_snippet_palette.library.structures.lazy_segtree_actions import range_binary_runs


def main():
    read = sys.stdin.buffer.readline
    n, q = map(int, read().split())
    seg = range_binary_runs(read().decode().strip())
    answer = []
    for _ in range(q):
        t, l, r = map(int, read().split())
        if t == 1:
            seg.flip(l - 1, r)
        else:
            answer.append(str(seg.longest(l - 1, r)))
    print("\n".join(answer))


if __name__ == "__main__":
    main()
