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
    D = NI()
    N = SI()
    K = len(N)

    # dp[i][j][k]
    # i桁まで確定[0, K] j:未満フラグ k:各位の和 mod D

    dp = [[[0]*D for _ in range(2)] for _ in range(K+1)]
    dp[0][0][0] = 1

    for i in range(K):
        for j in range(2):
            for k in range(D):
                lim = 9 if j == 1 else int(N[i])
                for x in range(lim+1):
                    nj = j | (x < lim)
                    nk = (k + x) % D

                    dp[i+1][nj][nk] += dp[i][j][k]
                    dp[i+1][nj][nk] %= MOD

    print(dp[K][0][0] + dp[K][1][0] - 1)


if __name__ == "__main__":
    main()
