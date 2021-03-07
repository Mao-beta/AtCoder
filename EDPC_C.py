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
    N = NI()
    tasks = [[0,0,0]] + [NLI() for _ in range(N)]
    dp = [[0]*3 for _ in range(N+1)]
    for j in range(3):
        dp[1][j] = tasks[1][j]

    for i in range(2, N+1):
        a, b, c = tasks[i]
        dp[i][0] = max(dp[i-1][1], dp[i-1][2]) + a
        dp[i][1] = max(dp[i-1][0], dp[i-1][2]) + b
        dp[i][2] = max(dp[i-1][0], dp[i-1][1]) + c
    print(max(dp[N]))


if __name__ == "__main__":
    main()
