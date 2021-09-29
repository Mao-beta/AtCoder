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
    K = NI()
    L = len(N)

    # dp[i][j][k] i桁まで確定 jは未満フラグ kは0でない桁の数
    dp = [[[0]*(K+1) for _ in range(2)] for _ in range(L+1)]
    dp[0][0][0] = 1

    for i in range(L):
        for j in range(2):
            for k in range(K+1):
                if dp[i][j][k] == 0: continue
                lim = 9 if j == 1 else int(N[i])
                for x in range(lim+1):
                    nj = j | (x < lim)
                    nk = k + (x != 0)
                    if nk > K: continue
                    dp[i+1][nj][nk] += dp[i][j][k]

    print(dp[L][0][K] + dp[L][1][K])


if __name__ == "__main__":
    main()
