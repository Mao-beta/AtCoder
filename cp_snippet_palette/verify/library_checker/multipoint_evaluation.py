# verification-helper: PROBLEM https://judge.yosupo.jp/problem/multipoint_evaluation
import sys
from cp_snippet_palette.library.math.polynomial import FPS


def main():
    read = sys.stdin.buffer.readline
    n, m = map(int, read().split())
    f = FPS(list(map(int, read().split())))
    print(*f.multipoint_evaluation(list(map(int, read().split()))))


if __name__ == "__main__":
    main()
