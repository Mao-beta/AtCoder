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
    T = NI()
    for _ in range(T):
        X, Y, P, Q = NMI()
        Z = 2*(X+Y) % (P+Q)
        X_mod = X % (P+Q)
        X_2 = (X_mod+Z) % (P+Q)
        X_gap = X_2 - X_mod

        ok_l = P - Y + 1

        if X_mod >= ok_l:
            print(X)
            continue

        if X_gap == 0:
            print("infinity")
            continue


        if X_gap > 0:
            if (ok_l - X_mod) % X_gap:
                n = (ok_l - X_mod) // X_gap + 1
            else:
                n = (ok_l - X_mod) // X_gap
            now_X = (X_mod + n * X_gap) % (P+Q)

        if X_gap < 0:
            if (X_mod - ok_l + (P+Q)) % abs(X_gap):
                n = (X_mod - ok_l + (P+Q)) // abs(X_gap) + 1
            else:
                n = (X_mod - ok_l + (P+Q)) // abs(X_gap)
            now_X = (X_mod + n * X_gap) % (P+Q)

        print(X + n * 2*(X+Y))



if __name__ == "__main__":
    main()
