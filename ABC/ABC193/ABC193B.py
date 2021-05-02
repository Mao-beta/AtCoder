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
    M = [NLI() for _ in range(N)]
    ans = 10**10
    for a, p, x in M:
        if x - a > 0:
            ans = min(ans, p)
    if ans == 10**10:
        print(-1)
    else:
        print(ans)


if __name__ == "__main__":
    main()
