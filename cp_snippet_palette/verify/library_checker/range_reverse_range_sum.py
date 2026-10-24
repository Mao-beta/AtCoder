# verification-helper: PROBLEM https://judge.yosupo.jp/problem/range_reverse_range_sum
import sys
from cp_snippet_palette.library.structures.dynamic_sequence import DynamicSequence


def main():
    read = sys.stdin.buffer.readline
    n, q = map(int, read().split())
    s = DynamicSequence(list(map(int, read().split())), mod=0)
    answer = []
    for _ in range(q):
        t, l, r = map(int, read().split())
        if t == 0:
            s.reverse(l, r)
        else:
            answer.append(str(s.prod(l, r)))
    print("\n".join(answer))


if __name__ == "__main__":
    main()
