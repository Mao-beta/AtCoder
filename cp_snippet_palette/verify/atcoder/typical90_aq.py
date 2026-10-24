# https://atcoder.jp/contests/typical90/tasks/typical90_aq
from cp_snippet_palette.library.basic.grid_search import grid_min_turns
import sys


def main():
    input = sys.stdin.readline
    h, w = map(int, input().split())
    sr, sc = map(int, input().split())
    gr, gc = map(int, input().split())
    grid = [input().strip() for _ in range(h)]
    print(grid_min_turns(grid, (sr - 1, sc - 1), (gr - 1, gc - 1)))


if __name__ == "__main__":
    main()
