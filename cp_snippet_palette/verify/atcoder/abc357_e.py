# https://atcoder.jp/contests/abc357/tasks/abc357_e
from cp_snippet_palette.library.graphs.functional_graph import FunctionalGraph
import sys


def main():
    input = sys.stdin.readline
    n = int(input())
    a = [int(x) - 1 for x in input().split()]
    fg = FunctionalGraph(a)
    print(sum(fg.reachable_count(v) for v in range(n)))


if __name__ == "__main__":
    main()
