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


def main():
    X, Y, A, B, C = NMI()
    P = NLI()
    Q = NLI()
    R = NLI()
    reds = [[1, p] for p in P]
    greens = [[2, q] for q in Q]
    skels = [[0, r] for r in R]
    apples = reds + greens + skels
    apples.sort(key=lambda x: x[1], reverse=True)

    colors = [0, 0, 0]
    limits = [10**9, X, Y]
    ans = 0
    for color, a in apples:
        if sum(colors) >= X + Y:
            break

        if colors[color] <= limits[color] - 1:
            colors[color] += 1
            ans += a
            continue

    print(ans)


if __name__ == "__main__":
    main()