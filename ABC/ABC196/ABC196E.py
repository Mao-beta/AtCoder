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


def main():
    N = NI()
    AT = [NLI() for _ in range(N)]
    Q = NI()
    X = NLI()

    low = -10**20
    high = 10**20
    gap = 0
    for a, t in AT:
        if t == 1:
            low += a
            high += a
            gap += a
        elif t == 2:
            low = max(low, a)
            if low >= high:
                high = low
        else:
            high = min(high, a)
            if low >= high:
                low = high

    for x in X:
        x += gap
        x = max(low, x)
        x = min(high, x)
        print(x)


if __name__ == "__main__":
    main()
