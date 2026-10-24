# https://atcoder.jp/contests/abc281/tasks/abc281_e
from cp_snippet_palette.library.structures.fenwick_multiset import FenwickMultiset
import sys


def main():
    input = sys.stdin.readline
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    bag = FenwickMultiset(a, a[:m])
    answer = [bag.sum_smallest(k)]
    for i in range(m, n):
        bag.discard(a[i - m])
        bag.add(a[i])
        answer.append(bag.sum_smallest(k))
    print(*answer)


if __name__ == "__main__":
    main()
