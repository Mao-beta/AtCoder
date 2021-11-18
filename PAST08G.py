import sys
import bisect
from itertools import accumulate


sys.setrecursionlimit(100000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    N, K = NMI()
    ABC = [NLI() for _ in range(N)]

    # X以下の数がK個以上か？
    # X >= ans: True else False
    ok = 10**20
    ng = 0

    while abs(ok-ng) > 1:
        X = (ok+ng) // 2

        num = 0
        for a, b, c in ABC:
            # b + c*(i-1) <= X
            # 1 <= i <= (X-b) // c + 1
            num += min(max((X-b)//c + 1, 0), a)

        if num >= K:
            ok = X
        else:
            ng = X

    print(ok)


if __name__ == "__main__":
    main()
