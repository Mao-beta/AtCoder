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
    N, K = NMI()

    for k in range(K):
        g1 = int("".join(sorted(list(str(N)), reverse=True)))
        g2 = int("".join(sorted(list(str(N)))))
        N = g1 - g2
    print(N)


if __name__ == "__main__":
    main()
