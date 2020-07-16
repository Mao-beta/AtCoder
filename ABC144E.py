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
    A = NLI()
    F = NLI()
    A.sort()
    F.sort(reverse=True)
    ok = 10**13
    ng = 0
    for i in range(100):
        mid = (ok+ng) // 2
        limits = [mid//f for f in F]
        ks = [max(a-l, 0) for a, l in zip(A, limits)]
        if sum(ks) <= K:
            ok = mid
        else:
            ng = mid

    print(ok)


if __name__ == "__main__":
    main()