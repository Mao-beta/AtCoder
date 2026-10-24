# verification-helper: PROBLEM https://judge.yosupo.jp/problem/dynamic_sequence_range_affine_range_sum
import sys
from cp_snippet_palette.library.structures.dynamic_sequence import DynamicSequence


def main():
    read = sys.stdin.buffer.readline
    n, q = map(int, read().split())
    s = DynamicSequence(list(map(int, read().split())))
    answer = []
    for _ in range(q):
        row = list(map(int, read().split()))
        t = row[0]
        if t == 0:
            s.insert(*row[1:])
        elif t == 1:
            s.erase(*row[1:])
        elif t == 2:
            s.reverse(*row[1:])
        elif t == 3:
            s.apply(*row[1:])
        else:
            answer.append(str(s.prod(*row[1:])))
    print("\n".join(answer))


if __name__ == "__main__":
    main()
