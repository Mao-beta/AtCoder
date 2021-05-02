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
    S = [SI() for _ in range(N)]
    dp = [[0, 0] for _ in range(N+1)]
    dp[0][0] = 1
    dp[0][1] = 1
    for i, s in enumerate(S):
        if s == "AND":
            dp[i+1][0] = dp[i][0]*2 + dp[i][1]
            dp[i+1][1] = dp[i][1]
        else:
            dp[i+1][0] = dp[i][0]
            dp[i+1][1] = dp[i][1]*2 + dp[i][0]
    print(dp[N][1])


if __name__ == "__main__":
    main()
