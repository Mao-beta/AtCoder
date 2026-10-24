# https://atcoder.jp/contests/abc367/tasks/abc367_e
from cp_snippet_palette.library.graphs.functional_graph import FunctionalGraph
import sys


def main():
    input = sys.stdin.readline
    n, k = map(int, input().split())
    x = [int(v) - 1 for v in input().split()]
    a = list(map(int, input().split()))
    fg = FunctionalGraph(x)
    print(*(a[fg.jump(i, k)] for i in range(n)))


if __name__ == "__main__":
    main()
