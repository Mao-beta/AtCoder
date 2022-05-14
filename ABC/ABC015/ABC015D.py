import sys

MOD = 10 ** 9 + 7
MOD99 = 998244353

input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()
SMI = lambda: input().split()
SLI = lambda: list(SMI())


def main():
    W = NI()
    N, K = NMI()
    AB = [NLI() for _ in range(N)]

    # dp[j][k] 幅j使って、k枚使っているときの最大価値
    dp = [[0]*(W+1) for _ in range(K+1)]
    dp2 = [[0]*(W+1) for _ in range(K+1)]

    for i in range(N):
        a, b = AB[i]
        for j in range(W+1):
            nj = j + a
            for k in range(K+1):
                nk = k + 1
                # 使わない
                dp2[k][j] = max(dp2[k][j], dp[k][j])

                if nj > W or nk > K:
                    continue

                # 使う
                dp2[nk][nj] = max(dp2[nk][nj], dp[k][j] + b)

        dp, dp2 = dp2, dp

    ans = 0
    for j in range(W+1):
        for k in range(K+1):
            ans = max(ans, dp[k][j])

    print(ans)


if __name__ == "__main__":
    main()
