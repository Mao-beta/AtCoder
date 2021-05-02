import sys
import math
from collections import deque
import bisect
from functools import lru_cache

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    T = [3**i for i in range(12)]
    colors = set(["B", "W", "R"])

    N = NI()
    C = SI()

    @lru_cache(maxsize=None)
    def rec(x, y):
        if x == N:
            return C[y-1]

        idx = bisect.bisect_right(T, N - x)
        z = T[idx-1]

        ca = rec(x+z, y)
        cb = rec(x+z, y+z)

        if ca == cb:
            cz = ca
        else:
            cz = colors - set([ca, cb])
            cz = cz.pop()

        return cz

    print(rec(1, 1))


if __name__ == "__main__":
    main()
