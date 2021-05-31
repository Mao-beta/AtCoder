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


def main():
    N = NI()
    tasks = [NLI() for _ in range(N)]
    tasks.sort()
    # dp[i][j] i個目の仕事まで見てj日過ぎたときの最大金額
    # 答えはmax(dp[N])
    dp = [[0]*5010 for _ in range(N+5)]
    for i in range(N):
        for j in range(5005):
            d, c, s = tasks[i]
            if d - c >= j:
                dp[i+1][j+c] = max(dp[i+1][j+c], dp[i][j] + s)
            dp[i+1][j] = max(dp[i+1][j], dp[i][j])
    print(max(dp[N]))


if __name__ == "__main__":
    main()
