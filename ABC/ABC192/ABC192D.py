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
    X = SI()
    M = NI()

    min_p = int(max(X)) + 1
    n = len(X)

    if n == 1:
        if int(X) <= M:
            print(1)
            exit()
        else:
            print(0)
            exit()

    now_m = 0
    for i, xi in enumerate(X[::-1]):
        now_m += pow(min_p, i) * int(xi)
        if now_m > M:
            print(0)
            exit()

    ok = min_p
    ng = 10**18+1

    while abs(ok-ng) > 1:
        mid = (ok+ng)//2
        is_ng = False

        limit_keta = int(math.log(M, mid)) + 2
        if n >= limit_keta:
            is_ng = True

        now_m = 0
        for i, xi in enumerate(X[::-1]):
            now_m += pow(mid, i) * int(xi)
            if now_m > M:
                is_ng = True
                break

        if is_ng:
            ng = mid
        else:
            ok = mid

    print(ok - min_p + 1)


if __name__ == "__main__":
    main()
