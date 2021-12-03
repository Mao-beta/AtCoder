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
    K = SI()
    D = NI()
    N = len(K)
    # dp[less][i][j] less==1で下回っている確定で、i桁目まで見て余りがj
    dp = [[[0]*D for _ in range(N+1)] for _ in range(2)]
    dp[0][0][0] = 1
    for i in range(N):
        # 下回っている確定のやつからの遷移
        # 次の桁は何でもいい
        for j in range(D):
            for x in range(10):
                next_j = (j + x) % D
                dp[1][i+1][next_j] += dp[1][i][j]
                dp[1][i + 1][next_j] %= MOD

        # 下回っている確定でないやつからの遷移
        # 次の桁はnowまで、nowの場合はまだ確定しないまま
        # now未満の時はless=1
        now = int(K[i])
        for j in range(D):
            for x in range(now+1):
                next_j = (j + x) % D
                if x < now:
                    dp[1][i+1][next_j] += dp[0][i][j]
                    dp[1][i + 1][next_j] %= MOD
                else:
                    dp[0][i+1][next_j] += dp[0][i][j]
                    dp[0][i + 1][next_j] %= MOD

    print((dp[0][N][0] + dp[1][N][0] - 1)%MOD)



if __name__ == "__main__":
    main()
