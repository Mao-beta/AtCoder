# https://atcoder.jp/contests/abc271/tasks/abc271_d
from cp_snippet_palette.library.basic.knapsack_extra import two_choice_sum
import sys


def main():
    input = sys.stdin.readline
    n, target = map(int, input().split())
    choices = [tuple(map(int, input().split())) for _ in range(n)]
    result = two_choice_sum(choices, target)
    if result is None:
        print("No")
    else:
        print("Yes")
        print("".join("HT"[x] for x in result))


if __name__ == "__main__":
    main()
