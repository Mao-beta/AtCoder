import sys
import math
from collections import defaultdict
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    N, W = NMI()
    items = [[0, 0]] + [NLI() for _ in range(N)]
    dp = [[0]*(W+1) for _ in range(N+1)]

    for i in range(N):
        w, v = items[i+1]
        for j in range(W+1):
            if j + w <= W:
                dp[i+1][j+w] = max(dp[i+1][j+w], dp[i][j] + v)
            dp[i+1][j] = max(dp[i+1][j], dp[i][j])

    print(max(dp[N]))


if __name__ == "__main__":
    main()
