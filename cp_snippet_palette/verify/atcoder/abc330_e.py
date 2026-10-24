# https://atcoder.jp/contests/abc330/tasks/abc330_e
from cp_snippet_palette.library.structures.dynamic_mex import DynamicMex
import sys


def main():
    input = sys.stdin.readline
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    mex = DynamicMex(n, a)
    answer = []
    for _ in range(q):
        i, x = map(int, input().split())
        i -= 1
        mex.discard(a[i])
        mex.add(x)
        a[i] = x
        answer.append(mex.mex())
    print(*answer, sep="\n")


if __name__ == "__main__":
    main()
