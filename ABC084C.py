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
    trains = [NLI() for _ in range(N-1)]
    if N == 1:
        print(0)
        exit()

    for start in range(N-1):
        t = 0
        for now in range(start, N-1):
            C, S, F = trains[now]
            if t < S:
                t = S + C
            else:
                k = math.ceil((t-S)/F)
                t = S + k * F + C
        print(t)

    print(0)


if __name__ == "__main__":
    main()