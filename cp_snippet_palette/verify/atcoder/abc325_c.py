# https://atcoder.jp/contests/abc325/tasks/abc325_c
from cp_snippet_palette.library.basic.grid_search import grid_components
import sys


def main():
    input = sys.stdin.readline
    h, w = map(int, input().split())
    grid = [input().strip() for _ in range(h)]
    print(len(grid_components(grid, filled="#", diagonal=True)[1]))


if __name__ == "__main__":
    main()
