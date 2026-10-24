# verification-helper: PROBLEM https://judge.yosupo.jp/problem/static_range_count_distinct
import sys
from cp_snippet_palette.library.structures.offline_queries import range_count_distinct


def main():
    read = sys.stdin.buffer.readline
    n, q = map(int, read().split())
    a = list(map(int, read().split()))
    queries = [tuple(map(int, read().split())) for _ in range(q)]
    print("\n".join(map(str, range_count_distinct(a, queries))))


if __name__ == "__main__":
    main()
