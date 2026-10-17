import sys
import math
from collections import deque

sys.setrecursionlimit(100000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    N = NI()
    X = [1]
    for i in range(29):
        X.append(X[-1]*3)

    try:
        print(30 - X.index(N - 3**30))
    except:
        print(-1)


if __name__ == "__main__":
    main()
