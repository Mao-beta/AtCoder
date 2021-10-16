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

INF = 10**20

def main():
    T = NI()
    for _ in range(T):
        r, g, b = NMI()
        N = r + g + b
        X = r * 0 + g * 1 + b * 2
        Target = [0, N, 2*N]
        ans = INF
        for i, t in enumerate(Target):
            tmp = 0
            if (X - t) % 3:
                continue

            if i == 0:
                x, y, z = r, g, b
            elif i == 1:
                x, y, z = g, r, b
            else:
                x, y, z = b, r, g

            y, z = max(y, z), min(y, z)
            tmp += z
            x += 2 * z
            y -= z
            tmp += y
            ans = min(ans, tmp)

        print(ans if ans < INF else -1)


if __name__ == "__main__":
    main()
