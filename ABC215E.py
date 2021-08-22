import sys
import math
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 998244353
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    N = NI()
    S = SI()
    S = [ord(s) - ord("A") for s in S]

    # dp[i][b][j]: i文字目まで見て、今まで出た種類がbで、最後に出たのがj(未出場はj=10)
    dp = [[[0]*11 for _ in range(1<<10)] for _ in range(N+1)]
    dp[0][0][10] = 1

    for i in range(1, N+1):
        s = S[i-1]
        for b in range(1<<10):
            for j in range(11):
                # 出ない
                dp[i][b][j] += dp[i-1][b][j]
                # 出る（直前にも出てた）
                if s == j:
                    dp[i][b][j] += dp[i-1][b][j]
                # 出る（今回初めて）
                if s != j and ((b>>s)&1):
                    dp[i][b][s] += dp[i-1][b^(1<<s)][j]

                dp[i][b][j] %= MOD

    dpn = dp[N]
    ans = 0
    for dpnb in dpn:
        ans += sum(dpnb)

    ans -= 1
    print(ans % MOD)



if __name__ == "__main__":
    main()
