# verification-helper: PROBLEM https://atcoder.jp/contests/abc223/tasks/abc223_f
import sys
from cp_snippet_palette.library.structures.segtree_monoids import range_brackets


def main():
    read = sys.stdin.buffer.readline
    n, q = map(int, read().split())
    seg = range_brackets(read().decode().strip())
    answer = []
    for _ in range(q):
        t, l, r = map(int, read().split())
        if t == 1:
            x, y = seg.get(l - 1), seg.get(r - 1)
            seg.set(l - 1, y)
            seg.set(r - 1, x)
        else:
            answer.append("Yes" if seg.balanced(l - 1, r) else "No")
    print("\n".join(answer))


if __name__ == "__main__":
    main()
