# verification-helper: PROBLEM https://judge.yosupo.jp/problem/assignment
import sys
from cp_snippet_palette.library.graphs.assignment import assignment


def main():
    read = sys.stdin.buffer.readline
    cost = [list(map(int, read().split())) for _ in range(int(read()))]
    value, permutation = assignment(cost)
    print(value)
    print(*permutation)


if __name__ == "__main__":
    main()
