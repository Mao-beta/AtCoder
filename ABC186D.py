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
    A = sorted(NLI())
    ans = 0
    gap = 0
    for i in range(N-1):
        gap = gap + (A[i+1]-A[i]) * (i+1)
        ans += gap
    print(ans)


if __name__ == "__main__":
    main()
