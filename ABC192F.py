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
    N, X = NMI()
    A = NLI()

    ans = 10**20
    # 全部でK個取ると固定して全探索
    for K in range(1, N+1):
        # dp[i][k][r]＝i個まで見た中でk個取ってて和のKでの剰余がrのときの和の最大
        # 到達可能でないときは-1←忘れてた
        dp = [[[-1]*K for _ in range(K+1)] for _ in range(N+1)]
        dp[0][0][0] = 0

        for i, a in enumerate(A):
            for k in range(K+1):
                for r in range(K):
                    # 既にK個取りきってなくて「到達可能な状態のとき」←忘れてた
                    # aを採用する場合、遷移先のrは(r+a)%K
                    if k != K and dp[i][k][r] >= 0:
                        dp[i+1][k+1][(r+a) % K] = max(dp[i+1][k+1][(r+a) % K], dp[i][k][r] + a)
                    # aを採用しない場合
                    dp[i+1][k][r] = max(dp[i+1][k][r], dp[i][k][r])

        s = dp[N][K][X%K]
        if s > 0:
            ans = min(ans, (X-s)//K)

    print(ans)


if __name__ == "__main__":
    main()
