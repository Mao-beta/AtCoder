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
    A = NLI()
    B = [[0]*2 for _ in range(62)]
    for a in A:
        for i in range(62):
            B[i][(a >> i) & 1] += 1
    ans = 0
    for i, b in enumerate(B):
        ans += b[0] * b[1] * pow(2, i, MOD)
    print(ans % MOD)


if __name__ == "__main__":
    main()