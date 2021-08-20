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
    N, M = NMI()
    A = NLI()
    dp = [0] * N
    ans = N
    for i, a in enumerate(A, start=1):
        if i - dp[a] > M:
            ans = min(ans, a)
        dp[a] = i

    for a in range(N):
        if N+1 - dp[a] > M:
            ans = min(ans, a)

    print(ans)


if __name__ == "__main__":
    main()
