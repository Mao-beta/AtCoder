import sys
import math
from collections import defaultdict
from collections import deque

sys.setrecursionlimit(100000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    N = SI()
    K = len(N)

    dp = [[0]*2 for _ in range(K+1)]
    dp[0][0] = 1

    for i in range(K):
        for j in range(2):
            lim = 1 if j == 1 else int(N[i])
            for x in range(lim+1):
                nj = j | (x < lim)
                c = 2 if x == 1 else 1
                dp[i+1][nj] += dp[i][j] * c
                dp[i+1][nj] %= MOD

    print((dp[K][0] + dp[K][1])%MOD)


if __name__ == "__main__":
    main()
