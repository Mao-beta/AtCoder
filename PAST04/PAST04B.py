import sys
import math
from collections import defaultdict
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def solve(X, Y):
    if Y == 0:
        print("ERROR")
        return 0

    ans = str(X * 100 // Y)
    L = len(ans)
    if L >= 4:
        print(ans[:-2] + "." + ans[-2:])
    elif L == 3:
        print(ans[:-2] + "." + ans[-2:])
    elif L == 2:
        print("0." + ans)
    else:
        print("0.0" + ans)


def main():
    X, Y = NMI()

    # for X in range(101):
    #     for Y in range(101):
    #         print(X, Y, " ", end="")
    solve(X, Y)


if __name__ == "__main__":
    main()
