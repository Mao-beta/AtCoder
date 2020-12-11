import sys
import math
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def make_grid(h, w, num): return [[int(num)] * w for _ in range(h)]


def main():
    N = SI()
    L = [int(n) % 3 for n in N]
    S = sum(L)


    if S % 3 == 0:
        print(0)
        exit()

    if len(N) == 1:
        print(-1)
        exit()

    if len(N) == 2:
        if L.count(0) >= 1:
            print(1)
            exit()
        else:
            print(-1)
            exit()

    if S % 3 == 1:
        if L.count(1) >= 1:
            print(1)
        elif L.count(2) >= 2:
            print(2)
        else:
            print(-1)
    else:
        if L.count(2) >= 1:
            print(1)
        elif L.count(1) >= 2:
            print(2)
        else:
            print(-1)



if __name__ == "__main__":
    main()
