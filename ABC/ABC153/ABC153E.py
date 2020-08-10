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
    H, N = NMI()
    M = [NLI() for _ in range(N)]
    # dp[i] はiダメージ与えたときの最小の魔力
    dp = [10**10] * (H+10)
    dp[0] = 0
    for i in range(H):
        for m in M:
            dp[min(i+m[0], H)] = min(dp[min(i+m[0], H)], dp[i] + m[1])
    print(dp[H])



if __name__ == "__main__":
    main()