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
    H = NLI() + [0, 0, 0]
    dp = [10**10]*(N+3)
    dp[1] = 0
    for i in range(1, N):
        dp[i+1] = min(dp[i+1], dp[i] + abs(H[i-1] - H[i]))
        dp[i+2] = min(dp[i+2], dp[i] + abs(H[i-1] - H[i+1]))
    print(dp[N])


if __name__ == "__main__":
    main()
