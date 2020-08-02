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
    N = NI()
    infos = [NLI() for _ in range(N)]
    colors = [0] * 1000005
    imos = [0] * 1000002
    for info in infos:
        l, r = info
        imos[l] += 1
        imos[r+1] -= 1
    for i in range(len(imos)):
        if i == 0:
            colors[i] = imos[i]
            continue
        colors[i] = colors[i-1] + imos[i]

    print(max(colors))


if __name__ == "__main__":
    main()