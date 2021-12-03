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
    K = NI()

    if K % 9:
        print(0)
        exit()

    dp = [0] * (K+10)
    dp[0] = 1

    for i in range(K+1):
        for j in range(1, 10):
            if i-j < 0: continue
            dp[i] += dp[i-j]
            dp[i] %= MOD

    print(dp[K])


if __name__ == "__main__":
    main()
