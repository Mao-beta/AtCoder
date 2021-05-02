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
    S = SI()[::-1]
    N = len(S)
    # dp[k][i] は下からi桁目(0~N)まで見て繰上りがある/ない（k=1or0）ときの支払う最低枚数
    dp = [[0]*(N+1) for _ in range(2)]
    dp[1][0] = 10**20
    for i in range(N):
        s = int(S[i])
        if 1 <= s < 9:
            dp[0][i+1] = min(
                dp[0][i] + s,
                dp[1][i] + s+1
            )
            dp[1][i+1] = min(
                dp[0][i] + 10-s,
                dp[1][i] + 10-(s+1)
            )
        elif s == 0:
            dp[0][i+1] = min(
                dp[0][i],
                dp[1][i] + 1
            )
            dp[1][i+1] = dp[1][i] + 9
        else:  # s==9
            dp[0][i+1] = dp[0][i] + 9
            dp[1][i+1] = min(
                dp[0][i] + 1,
                dp[1][i]
            )

    print(min(dp[0][N], dp[1][N]+1))


if __name__ == "__main__":
    main()
