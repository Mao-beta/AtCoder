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
    N, K = NMI()
    H = [0] + NLI() + [0]*200
    dp = [10**10] * (N+110)
    dp[1] = 0
    for i in range(1, N):
        for k in range(1, K+1):
            dp[i+k] = min(dp[i+k], dp[i] + abs(H[i]-H[i+k]))
    print(dp[N])

if __name__ == "__main__":
    main()
