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
    N, D = NMI()
    P = [NLI() for _ in range(N)]
    ans = 0
    for x, y in P:
        if x**2 + y**2 <= D**2:
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()