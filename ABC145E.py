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
    N, T = NMI()
    AB = [NLI() for _ in range(N)]
    AB.sort(key=lambda x: (x[0], -x[1]))
    dp = [[0]*(T+1) for _ in range(N+1)]
    ans = 0
    for i in range(N):
        a, b = AB[i]
        for j in range(T+1):
            dp[i+1][j] = max(dp[i+1][j], dp[i][j])
            if j+a < T:
                dp[i+1][j+a] = max(dp[i+1][j+a], dp[i][j] + b)
            else:
                ans = max(ans, dp[i][j] + b)

    for j in range(T+1):
        ans = max(ans, dp[-1][j])

    print(ans)


if __name__ == "__main__":
    main()
