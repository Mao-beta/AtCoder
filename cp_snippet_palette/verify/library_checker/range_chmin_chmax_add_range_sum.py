# verification-helper: PROBLEM https://judge.yosupo.jp/problem/range_chmin_chmax_add_range_sum
import sys
from cp_snippet_palette.snippets.structures.SegmentTreeBeats import SegmentTreeBeats


def main():
    read = sys.stdin.buffer.readline
    n, q = map(int, read().split())
    seg = SegmentTreeBeats(list(map(int, read().split())))
    answer = []
    for _ in range(q):
        query = list(map(int, read().split()))
        if query[0] == 0:
            seg.chmin(*query[1:])
        elif query[0] == 1:
            seg.chmax(*query[1:])
        elif query[0] == 2:
            seg.add(*query[1:])
        else:
            answer.append(str(seg.sum(*query[1:])))
    print("\n".join(answer))


if __name__ == "__main__":
    main()
