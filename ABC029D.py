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
    N = SI()
    K = len(N)
    # dp[i][j][k] i桁まで確定 jは未満フラグ 1がk個
    dp = [[[0]*10 for _ in range(2)] for _ in range(K+1)]
    dp[0][0][0] = 1

    for i in range(K):
        for j in range(2):
            for k in range(9):
                lim = 9 if j == 1 else int(N[i])
                for x in range(lim+1):
                    nj = j | (x < lim)
                    nk = k + (x == 1)
                    dp[i+1][nj][nk] += dp[i][j][k]

    ans = 0
    for j in range(2):
        for k in range(10):
            ans += dp[K][j][k] * k
    print(ans)


if __name__ == "__main__":
    main()
